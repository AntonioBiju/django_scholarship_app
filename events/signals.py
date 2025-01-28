from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Scholarship_Information, PersonalInformation, Eligibility_Data, User
from django.core.mail import EmailMessage
from django.conf import settings
import pandas as pd
@receiver(post_save, sender=Scholarship_Information)
def classify_and_notify(sender, instance, created, **kwargs):
    if created:
        # Get all personal information of users
        users = PersonalInformation.objects.all()
        user_data = []

        # Prepare data for decision tree based on qualification level
        for user in users:
            # Initialize eligibility data
            print(user.name)
            data = {
                'id': user.id,
                'gender': 1 if user.gender == instance.gender_criteria or instance.gender_criteria == 'All' else 0,
                'caste': 1 if user.caste == instance.caste_criteria or instance.caste_criteria == 'All' else 0,
                'religion': 1 if user.religion == instance.Relegion_criteria or instance.Relegion_criteria == 'All' else 0,
                'funding': 1 if user.funding == instance.funding or instance.funding == 'All' else 0,
                'qualification': 1 if user.current_qualification == instance.qualification or instance.qualification == 'All' else 0,
                'minimum_marks': float(instance.minimum_Mark_criteria or 0),
                'minimum_income': float(instance.Minimum_Income_criteria or float('inf')),  # Added minimum income
                'annual_income': user.annual_income or float('inf'),
                'tenth_marks': user.tenth_marks if user.tenth_marks is not None else 0,
                'twelfth_marks': user.twelfth_marks if user.twelfth_marks is not None else 0,
                'ug_percentage': user.ug_percentage if user.ug_percentage is not None else 0,
                'pg_percentage': user.pg_percentage if user.pg_percentage is not None else 0,
                'research_percentage': user.research_percentage if user.research_percentage is not None else 0,

                'eligible': 0  # Default eligibility is 0 (not eligible)
            }

            user_data.append(data)
        
        # Create a DataFrame
        df = pd.DataFrame(user_data)

        # Define features (X) and eligibility logic
        def calculate_eligibility(row):
            # Check if annual income is below or equal to the scholarship's minimum income
            if row['annual_income'] > row['minimum_income']:
                return 0  # Mark as ineligible if income criteria fail
            
            # Check marks across relevant fields
            fields_to_check = [
                'tenth_marks', 'twelfth_marks', 'ug_percentage',
                'pg_percentage', 'research_percentage'
            ]
            for field in fields_to_check:
                if row[field] > 0:  # Only consider valid fields (non-zero)
                    if row[field] < row['minimum_marks']:  # If any valid field fails
                        return 0  # Ineligible
            return 1  # Eligible if all valid fields pass

        df['eligible'] = df.apply(calculate_eligibility, axis=1)
        
        # Save eligibility results and send notifications
        for _, row in df.iterrows():
            if row['eligible'] == 1:  # If eligible
                user = PersonalInformation.objects.get(id=row['id'])
                r_user = User.objects.get(username=user.user)
                Eligibility_Data.objects.create(user=user, scholarship=instance, is_notify=True)

                # Prepare the email content
                subject = f"Congratulations! You are eligible for the {instance.name} Scholarship"
                message = f"""
                Dear {user.name},

                We are excited to inform you that you are eligible for the "{instance.name}" scholarship.
                Please review the scholarship details and apply before the deadline: {instance.deadline}.
                Link: {instance.link}
                Best Regards,
                Scholarship Team
                """
                recipient_email = r_user.email

                try:
                    # Send email
                    email = EmailMessage(
                        subject=subject,
                        body=message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[recipient_email],
                    )
                    email.send()
                    print(f"Email sent to {recipient_email} for {instance.name}")

                except Exception as e:
                    print(f"Failed to send email to {recipient_email}: {e}")
