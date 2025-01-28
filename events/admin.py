from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(PersonalInformation)

admin.site.register(Eligibility_Data)
class EligibilityDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'scholarship', 'is_notify')
    list_filter = ('is_notify',)


class ScholarshipInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender_criteria', 'deadline', 'Minimum_Income_criteria')  # Fields to display in the admin list view
    search_fields = ('name', 'category', 'gender_criteria')  # Fields for search functionality
    list_filter = ('category', 'gender_criteria', 'deadline','qualification')  # Filters for the admin panel
    ordering = ('-deadline',)  # Order by deadline descending

    # Fields to show in the form
    fields = (
        'name',
        'category',
        'gender_criteria',
        'Relegion_criteria',
        'caste_criteria',
        'funding',
        'qualification',
        'Minimum_Income_criteria',
        'minimum_Mark_criteria',
        'benifits',
        'deadline',
        'link',
    )

    # Readonly fields (if any)
    # readonly_fields = ('link',)  # Example: make the link field readonly if needed

admin.site.register(Scholarship_Information, ScholarshipInformationAdmin)



