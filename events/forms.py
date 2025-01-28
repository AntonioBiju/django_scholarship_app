from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from datetime import date
from . models import *

class Student_Login(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"John Smith","class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline"
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
         "placeholder":"your@email.com","class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline"
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
         "placeholder":"Password","class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline"
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
         "placeholder":"Password","class":"shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline"
    }))
    class Meta:
        model=User
        fields=[ 'username','email','password1','password2']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:dark:ring-violet-600 dark:bg-gray-100", 'placeholder': 'Leroy Jenkins'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:dark:ring-violet-600 dark:bg-gray-100', 'placeholder': 'leroy@jenkins.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'block w-full rounded-md focus:ring focus:ring-opacity-75 focus:dark:ring-violet-600 dark:bg-gray-100', 'placeholder': 'Your Message', 'rows': 5}))




class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = [
            'profile_photo', 'name', 'roll_number', 'age', 'date_of_birth',
            'gender', 'nationality', 'state_of_residence', 'caste', 'religion',
            'phone_number'
        ]

    def clean_profile_photo(self):
        photo = self.cleaned_data.get("profile_photo")
        if not photo:
            raise forms.ValidationError("Profile photo is required.")
        if photo.size > 5 * 1024 * 1024:  # Limit size to 5 MB
            raise forms.ValidationError("Profile photo size must not exceed 5 MB.")
        return photo

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Name is required.")
        if len(name) > 30:
            raise forms.ValidationError("Name must not exceed 30 characters.")
        return name

    def clean_roll_number(self):
        roll_number = self.cleaned_data.get("roll_number")
        if not roll_number:
            raise forms.ValidationError("Roll number is required.")
        if len(str(roll_number)) > 10:
            raise forms.ValidationError("Roll number must not exceed 10 digits.")
        return roll_number

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get("date_of_birth")
        if not dob:
            raise forms.ValidationError("Date of birth is required.")
        today = date.today()
        if dob > today:
            raise forms.ValidationError("Date of birth cannot be in the future.")
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18 or age > 30:
            raise forms.ValidationError("Age must be between 18 and 35.")
        self.cleaned_data['age'] = age
        return dob

    def clean_gender(self):
        gender = self.cleaned_data.get("gender")
        if gender not in ["Male", "Female", "Other"]:
            raise forms.ValidationError("Invalid gender selection.")
        return gender

    def clean_nationality(self):
        nationality = self.cleaned_data.get("nationality")
        if not nationality:
            raise forms.ValidationError("Nationality is required.")
        return nationality

    def clean_state_of_residence(self):
        state = self.cleaned_data.get("state_of_residence")
        if not state:
            raise forms.ValidationError("State of residence is required.")
        if len(state) > 50:
            raise forms.ValidationError("State of residence must not exceed 50 characters.")
        return state

    def clean_caste(self):
        caste = self.cleaned_data.get("caste")
        if not caste:
            raise forms.ValidationError("Caste is required.")
        if len(caste) > 50:
            raise forms.ValidationError("Caste must not exceed 50 characters.")
        return caste

    def clean_religion(self):
        religion = self.cleaned_data.get("religion")
        if not religion:
            raise forms.ValidationError("Religion is required.")
        if len(religion) > 50:
            raise forms.ValidationError("Religion must not exceed 50 characters.")
        return religion

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be 10 digits long.")
        return phone_number



class FamilyDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = [
            'father_name', 'father_occupation', 'mother_name', 
            'mother_occupation', 'annual_income'
        ]

    def clean_father_name(self):
        father_name = self.cleaned_data.get("father_name")
        if not father_name:
            raise forms.ValidationError("Father's name is required.")
        if len(father_name) > 30:
            raise forms.ValidationError("Father's name must not exceed 30 characters.")
        return father_name

    def clean_father_occupation(self):
        father_occupation = self.cleaned_data.get("father_occupation")
        if not father_occupation:
            raise forms.ValidationError("Father's occupation is required.")
        return father_occupation

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get("mother_name")
        if not mother_name:
            raise forms.ValidationError("Mother's name is required.")
        
        if len(mother_name) > 30:
            raise forms.ValidationError("Mother's name must not exceed 30 characters.")
        return mother_name

    def clean_mother_occupation(self):
        mother_occupation = self.cleaned_data.get("mother_occupation")
        if not mother_occupation:
            raise forms.ValidationError("Mother's occupation is required.")
        return mother_occupation

    def clean_annual_income(self):
        annual_income = self.cleaned_data.get("annual_income")
        if not annual_income:
            raise forms.ValidationError("Annual income is required.")
        if not isinstance(annual_income, (int, float)):
            raise forms.ValidationError("Annual income must be a numeric value.")
        if annual_income < 0:
            raise forms.ValidationError("Annual income cannot be negative.")
        return annual_income


class AcademicRecordsForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = [
            'current_qualification', 'tenth_school_name', 'tenth_marks',
            'twelfth_school_name', 'twelfth_marks', 'ug_college_name',
            'ug_degree', 'ug_branch', 'ug_percentage', 'pg_college_name',
            'pg_degree', 'pg_branch', 'pg_percentage', 'research_college_name',
            'research_degree', 'research_program', 'research_percentage', 'funding'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting optional fields
        optional_fields = [
            'twelfth_school_name', 'twelfth_marks', 'ug_college_name', 
            'ug_degree', 'ug_branch', 'ug_percentage', 'pg_college_name',
            'pg_degree', 'pg_branch', 'pg_percentage', 'research_college_name',
            'research_degree', 'research_program', 'research_percentage'
        ]
        for field in optional_fields:
            self.fields[field].required = False

    def clean_current_qualification(self):
        qualification = self.cleaned_data.get('current_qualification')
        if qualification not in ['10th', '12th', 'UG', 'PG', 'Mphil/Ph.D']:
            raise forms.ValidationError("Invalid qualification. Must be one of '10th', '12th', 'UG', 'PG', or 'Mphil/Ph.D'.")
        return qualification

    def clean_tenth_marks(self):
        marks = self.cleaned_data.get('tenth_marks')
        if marks is None:
            raise forms.ValidationError("10th marks are required.")
        if not 0 <= marks <= 100:
            raise forms.ValidationError("10th marks must be between 0 and 100.")
        return marks

    def clean_twelfth_marks(self):
        marks = self.cleaned_data.get('twelfth_marks')
        if marks is not None and (marks < 0 or marks > 100):
            raise forms.ValidationError("12th marks must be between 0 and 100.")
        return marks

    def clean_ug_percentage(self):
        percentage = self.cleaned_data.get('ug_percentage')
        if percentage is not None and (percentage < 0 or percentage > 100):
            raise forms.ValidationError("UG percentage must be between 0 and 100.")
        return percentage

    def clean_pg_percentage(self):
        percentage = self.cleaned_data.get('pg_percentage')
        if percentage is not None and (percentage < 0 or percentage > 100):
            raise forms.ValidationError("PG percentage must be between 0 and 100.")
        return percentage

    def clean_research_percentage(self):
        percentage = self.cleaned_data.get('research_percentage')
        if percentage is not None and (percentage < 0 or percentage > 100):
            raise forms.ValidationError("Research percentage must be between 0 and 100.")
        return percentage

    def clean_funding(self):
        funding = self.cleaned_data.get('funding')
        if funding is not None:
            raise forms.ValidationError("Funding amount cannot be negative.")
        return funding

    def clean(self):
        cleaned_data = super().clean()
        current_qualification = cleaned_data.get('current_qualification')

        # Validate required fields based on the current qualification
        if current_qualification == "UG":
            if not cleaned_data.get('twelfth_school_name') or cleaned_data.get('twelfth_marks') is None:
                raise forms.ValidationError("12th details (school name and marks) are required for UG qualification.")
           
           
        cleaned_data.update({
                'pg_college_name': None,
                'pg_degree': None,
                'pg_branch': None,
                'pg_percentage': 0,
            })
        

        if current_qualification == "PG":
            for field in ['ug_college_name', 'ug_degree', 'ug_branch', 'ug_percentage']:
                if not cleaned_data.get(field):
                    raise forms.ValidationError("UG details are required for PG qualification.")
              
              
        cleaned_data.update({
                'research_college_name': None,
                'research_degree': None,
                'research_branch': None,
                'research_percentage': 0,
            })
        

        if current_qualification == "Mphil/Ph.D":
            for field in ['pg_college_name', 'pg_degree', 'pg_branch', 'pg_percentage']:
                if not cleaned_data.get(field):
                    raise forms.ValidationError("PG details are required for M.Phil/Ph.D qualification.")
                
        return cleaned_data


