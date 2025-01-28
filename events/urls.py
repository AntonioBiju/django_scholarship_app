from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name='home'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("login/",views.loginpage,name='loginpage'),
    path("register/",views.register,name='register'),
    path('logout/',views.logoutpage,name='logout'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path('edit/',views.edit_profile,name = 'edit'),
    path('eligibility/',views.eligible_scholarships_view,name='eligible'),
    # path("multi_registration/", views.registration_view, name="mul_reg"),

]