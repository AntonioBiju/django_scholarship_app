from django.db import models
from django.contrib.auth.models import User
import datetime
import os

class PersonalInformation(models.Model):
    def getFileName(request,filename):
        Now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
        new_filename ="%s%s"%(Now,filename)
        return os.path.join('profile_photos/',new_filename)
    
    CASTE_CHOICES = [
        ('General', 'General'),
        ('OBC', 'Other Backward Class (OBC)'),
        ('SC', 'Scheduled Caste (SC)'),
        ('ST', 'Scheduled Tribe (ST)'),
        ('Minorities', 'Minorities'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    NATIONALITY_CHOICES = [
        ('Indian', 'Indian'),
        ('OCI', 'Overseas Citizen of India'),
        ('Foreign', 'Foreign National'),
    ] 
    STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
    ('Other', 'Other'),
]

    RELIGION_CHOICES = [
        ('Buddhist', 'Buddhist'),
        ('Christian', 'Christian'),
        ('Hindu', 'Hindu'),
        ('Jain', 'Jain'),
        ('Muslim', 'Muslim'),
        ('Parsi', 'Parsi'),
        ('Sikh', 'Sikh'),
        ('Other', 'Other'),
    ]
# Undergraduate Degree Choices
    UG_DEGREE_CHOICES = [
        ("B.Sc.", "B.Sc."),
        ("B.A.", "B.A."),
        ("B.B.A.", "B.B.A."),
        ("B.Com.", "B.Com."),
        ("B.Voc.", "B.Voc."),
        ("B.S.W.", "Bachelor of Social Work (BSW)"),
    ]
   
# Undergraduate Branch Choices

    UG_BRANCH_CHOICES = [
    ("Physics", "Physics"),
    ("Zoology", "Zoology"),
    ("Mathematics", "Mathematics"),
    ("Information Technology", "Information Technology"),
    ("Environmental Sciences", "Environmental Sciences"),
    ("Bioinformatics", "Integrated Bioinformatics"),
    ("Biotechnology", "Biotechnology"),
    ("Computer Science", "Computer Science"),
    ("Actuarial Mathematical Science", "Actuarial Mathematical Science"),
    ("Tamil", "Tamil"),
    ("English", "English"),
    ("Economics", "Economics"),
    ("History", "History"),
    ("Commerce", "Commerce"),
    ("Commerce (Computer Applications)", "Commerce (Computer Applications)"),
    ("Commerce (Professional Accounting)", "Commerce (Professional Accounting)"),
    ("Commerce (International Accounting)", "Commerce (International Accounting)"),
    ("Commerce (Strategic Finance)", "Commerce (Strategic Finance)"),
    ("Commerce (FinTech)", "Commerce (FinTech)"),
    ("Commerce (Business Process Management)", "Commerce (Business Process Management)"),
    ("Commerce (Business Analytics)", "Commerce (Business Analytics)"),
    ("Accounting and Taxation", "Accounting and Taxation"),
    ("Social Work", "Social Work"),
]

# Postgraduate Degree Choices
    PG_DEGREE_CHOICES = [
        ("M.Sc.", "M.Sc."),
        ("M.A.", "M.A."),
        ("M.B.A.", "M.B.A."),
        ("M.Com.", "M.Com."),
        ("MSW", "Master of Social Work (MSW)"),
        ("PGDC", "Post-Graduate Diploma in Counselling"),
        ("DCFCD", "Diploma in Child Focused Community Development"),
    ]
# Postgraduate Branch Choices    
    PG_BRANCH_CHOICES = [
    ("Physics", "Physics"),
    ("Zoology", "Zoology"),
    ("Mathematics", "Mathematics"),
    ("Information Technology", "Information Technology"),
    ("Environmental Sciences", "Environmental Sciences"),
    ("Data Science", "Data Science"),
    ("Bioinformatics", "Integrated Bioinformatics"),
    ("Biotechnology", "Biotechnology"),
    ("Computer Science", "Computer Science"),
    ("Actuarial Science", "Actuarial Science"),
    ("Management", "Management"),
    ("Chemistry", "Chemistry"),
    ("Tamil", "Tamil"),
    ("English", "English"),
    ("Economics", "Economics"),
    ("History", "History"),
    ("Commerce", "Commerce"),
    ("Social Work", "Social Work"),
]

# Research Degree Choices
    RESEARCH_DEGREE_CHOICES = [
        ("M.Phil.", "M.Phil."),
        ("Ph.D.", "Ph.D."),
    ]

# Research Branch Choices
    RESEARCH_BRANCH_CHOICES = [
    ("Physics", "Physics"),
    ("Zoology", "Zoology"),
    ("Mathematics", "Mathematics"),
    ("Information Technology", "Information Technology"),
    ("Environmental Sciences", "Environmental Sciences"),
    ("Biotechnology", "Biotechnology"),
    ("Computer Science", "Computer Science"),
    ("Management", "Management"),
    ("Chemistry", "Chemistry"),
    ("Tamil", "Tamil"),
    ("English", "English"),
    ("Economics", "Economics"),
    ("History", "History"),
    ("Commerce", "Commerce"),
    ("Social Work", "Social Work"),
]

    CURRENT_QUALIFICATION_CHOICES = [
        ('UG', 'UG'),
        ('PG', 'PG'),
        ('Mphil/Ph.D', 'Mphil/Ph.D'),
    ]

    FUNDING_CHOICES = [
        ('Aided', 'Aided'),
        ('Self-Financed', 'Self-Financed'),
    ]


# Personal Details
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_information')
    profile_photo = models.ImageField(upload_to=getFileName, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    roll_number = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='Other')
    nationality = models.CharField(max_length=20, choices=NATIONALITY_CHOICES, default='Indian')
    state_of_residence = models.CharField(max_length=52, choices=STATE_CHOICES, default='Tamil Nadu')
    caste = models.CharField(max_length=52, choices=CASTE_CHOICES, default='General')
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, null=True, blank=True)
    # email = models.ForeignKey(User.email,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True, blank=True)

# Family details
    father_name = models.CharField(max_length=100, null=True, blank=True)
    father_occupation = models.CharField(max_length=100,  null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_occupation = models.CharField(max_length=100,  null=True, blank=True)
    annual_income = models.FloatField( null=True, blank=True)

# Academic Details
# Current Qulaification
    current_qualification = models.CharField(max_length=10, choices=CURRENT_QUALIFICATION_CHOICES)
# 10 details
    tenth_school_name = models.CharField(max_length=255)
    tenth_marks = models.FloatField(null=True, blank=True)
# 12 th details
    twelfth_school_name = models.CharField(max_length=255, null=True, blank=True)
    twelfth_marks = models.FloatField(null=True, blank=True)
# Ug details
    ug_college_name = models.CharField(max_length=255, null=True, blank=True)
    ug_degree = models.CharField(max_length=255, choices=UG_DEGREE_CHOICES, null=True, blank=True)
    ug_branch = models.CharField(max_length=255, choices=UG_BRANCH_CHOICES,null=True, blank=True)
    ug_percentage = models.FloatField(null=True, blank=True)
# pg details
    pg_college_name = models.CharField(max_length=255, null=True, blank=True)
    pg_degree = models.CharField(max_length=255,choices=PG_DEGREE_CHOICES, null=True, blank=True)
    pg_branch = models.CharField(max_length=255,choices=PG_BRANCH_CHOICES, null=True, blank=True)
    pg_percentage = models.FloatField(null=True, blank=True)
#Research details
    research_college_name = models.CharField(max_length=255, null=True, blank=True)
    research_degree = models.CharField(max_length=100, choices=RESEARCH_DEGREE_CHOICES,null=True, blank=True)
    research_program = models.CharField(max_length=100, choices=RESEARCH_BRANCH_CHOICES,null=True, blank=True)
    research_percentage = models.FloatField(null=True, blank=True)

#Aided or Self finance
    funding = models.CharField(max_length=15, choices=FUNDING_CHOICES, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"


class Scholarship_Information(models.Model):

    GENDER_CHOICES= [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('All', 'All'),
    ]
    RELIGION_CHOICES = [
        ('Buddhist', 'Buddhist'),
        ('Christian', 'Christian'),
        ('Hindu', 'Hindu'),
        ('Jain', 'Jain'),
        ('Muslim', 'Muslim'),
        ('Parsi', 'Parsi'),
        ('Sikh', 'Sikh'),
        ('All', 'All'),
    ]
    CASTE_CHOICES = [
        ('General', 'General'),
        ('OBC', 'Other Backward Class (OBC)'),
        ('SC', 'Scheduled Caste (SC)'),
        ('ST', 'Scheduled Tribe (ST)'),
        ('Minorities', 'Minorities'),
        ('All','All')
    ]
    category=[
        ('State', 'State'),
        ('Central', 'Central'),
        ('Institutional', 'Institutional'),
        ('Private', 'Private')
    ]
    FUNDING_CHOICES = [
        ('Aided', 'Aided'),
        ('Self-Financed', 'Self-Financed'),
        ('All','All'),
    ]
    CURRENT_QUALIFICATION_CHOICES = [
        ('UG', 'UG'),
        ('PG', 'PG'),
        ('Mphil/Ph.D', 'Mphil/Ph.D'),
        ('All','All')
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    gender_criteria = models.CharField(max_length=15, choices=GENDER_CHOICES, default='All')

    funding = models.CharField(max_length=15, choices=FUNDING_CHOICES,default='All')

    Minimum_Income_criteria = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    qualification = models.CharField(max_length=20, choices=CURRENT_QUALIFICATION_CHOICES, default='All')

    Relegion_criteria = models.CharField(max_length=20, choices=RELIGION_CHOICES, default='All')
    caste_criteria = models.CharField(max_length=52, choices=CASTE_CHOICES, default='All')
    minimum_Mark_criteria = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    benifits = models.CharField(max_length=100, null=False, blank=False)
    deadline = models.DateField()
    link = models.URLField()
    category= models.CharField(max_length=20,choices=category,default='State')


class Eligibility_Data(models.Model):
    user = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, db_index=True)
    scholarship = models.ForeignKey(Scholarship_Information, on_delete=models.CASCADE, db_index=True)
    is_notify= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name} - {self.scholarship.name}"