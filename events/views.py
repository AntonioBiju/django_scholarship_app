from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import *
from .forms import *

# Create your views here.
def home(request):
    
    return render(request,"events/indext.html")


def about(request):

    return render(request,"events/about.html")


def contact(request):
     if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"""
                    The UserName : {name}

                    The User Email : {email}

                    The User Message : {message}
                """,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
     else:
        form = ContactForm()
     return render(request,"events/contact.html",{'form':form})


def loginpage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            email = request.POST.get('email')
            username = User.objects.get(email=email.lower()).username
            pwd = request.POST.get('password')
            print(username,pwd)
            user = authenticate(username=username,password=pwd)
            print(user)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Succesfully')
                return redirect('home')
            else:
                messages.warning(request,'invalid login')
        
        return render(request,'events/auth/loginpage.html')
    # return render(request,"events/auth/loginpage.html")


def register(request):
    form=Student_Login()
    if request.method=='POST':
        form=Student_Login(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registraion succesfull you can login now......")
            return redirect('loginpage')
    return render(request,"events/auth/register.html",{'form':form})


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfully')
        return redirect('home')



def dashboard(request):
    # Try to fetch the user's personal information
    personal_info_queryset = PersonalInformation.objects.filter(user=request.user)

    if personal_info_queryset.exists():
        # If personal information exists, render the dashboard with the first record
        student_info = personal_info_queryset.first()

        context = {
            'is_dashboard': True,
            'profile': student_info.profile_photo,
            'name': student_info.name,
            'email': request.user.email,
            'age': student_info.age,
            'dob': student_info.date_of_birth,
            'gender': student_info.gender,
            'fname': student_info.father_name,
            'focc': student_info.father_occupation,
            'mname': student_info.mother_name,
            'mocc': student_info.mother_occupation,
            'income': student_info.annual_income,
            'caste': student_info.caste,
            'religion': student_info.religion,
            'nationality': student_info.nationality,
            'phone': student_info.phone_number,
            'roll_no': student_info.roll_number,
            'current_qualification': student_info.current_qualification,
            '10grade': student_info.tenth_marks,
            '12grade': student_info.twelfth_marks,
            'ug_college': student_info.ug_college_name,
            'ug_degree': student_info.ug_degree,
            'ug_branch': student_info.ug_branch,
            'u_percent': student_info.ug_percentage,
            'pg_college': student_info.pg_college_name,
            'pg_degree': student_info.pg_degree,
            'pg_braanch': student_info.pg_branch,
            'p_percent': student_info.pg_percentage,
            'research_college': student_info.research_college_name,
            'research_degree': student_info.research_degree,
            'research_branch': student_info.research_program,
            'r_percent': student_info.research_percentage,
        }
        return render(request, "events/dashboard/index.html", context)

    else:
        # If no personal information exists, handle multi-step registration
        step = request.session.get('reg_step', 1)  # Default to step 1
        instance_id = request.session.get('reg_instance_id')
        instance = None

        if instance_id:
            instance = PersonalInformation.objects.filter(id=instance_id).first()

        if request.method == 'POST':
            # Determine the current form based on the step
            if step == 1:
                form = PersonalInfoForm(request.POST, request.FILES, instance=instance)
            elif step == 2:
                form = FamilyDetailsForm(request.POST, instance=instance)
            else:
                form = AcademicRecordsForm(request.POST, instance=instance)

            if form.is_valid():
                # Save the instance
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()

                # Store instance ID in the session
                if not request.session.get('reg_instance_id'):
                    request.session['reg_instance_id'] = instance.id

                if step < 3:
                    # Proceed to the next step
                    request.session['reg_step'] = step + 1
                    return redirect('dashboard')
                else:
                    # Clear session data after the final step
                    del request.session['reg_step']
                    del request.session['reg_instance_id']
                    return redirect('dashboard')

        else:
            # Initialize the appropriate form for the step
            if step == 1:
                form = PersonalInfoForm(instance=instance)
            elif step == 2:
                form = FamilyDetailsForm(instance=instance)
            else:
                form = AcademicRecordsForm(instance=instance)

        # Render the form for the current step
        return render(request, 'events/dashboard/dash_register.html', {
            'form': form,
            'step': step,
            'is_dashboard': True
        })

    



    

def edit_profile(request):
    student = get_object_or_404(PersonalInformation, user=request.user)
    
    if request.method == 'POST':
        personal_form = PersonalInfoForm(request.POST, request.FILES, instance=student, prefix='personal')
        family_form = FamilyDetailsForm(request.POST, instance=student, prefix='family')
        academic_form = AcademicRecordsForm(request.POST, instance=student, prefix='academic')
        
        if all([personal_form.is_valid(), family_form.is_valid(), academic_form.is_valid()]):
            personal_form.save()
            family_form.save()
            academic_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        personal_form = PersonalInfoForm(instance=student, prefix='personal')
        family_form = FamilyDetailsForm(instance=student, prefix='family')
        academic_form = AcademicRecordsForm(instance=student, prefix='academic')
    
    context = {
        'personal_form': personal_form,
        'family_form': family_form,
        'academic_form': academic_form,
        'student': student,
        'is_dashboard':True,
        'nav': True,
    }
    return render(request, 'events/dashboard/edit_profile.html', context)

def eligible_scholarships_view(request):
    user = request.user
    eligible_data = Eligibility_Data.objects.filter(user__user=user)
    scholarships = eligible_data.select_related("scholarship")

    # Categorize scholarships by type
    categorized_scholarships = {}
    for scholarship in scholarships:
        category = scholarship.scholarship.category
        if category not in categorized_scholarships:
            categorized_scholarships[category] = []
        categorized_scholarships[category].append(scholarship.scholarship)

    return render(request, "events/dashboard/eligible_scholarships.html", {
        "categorized_scholarships": categorized_scholarships
    })




