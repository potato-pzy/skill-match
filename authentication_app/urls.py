from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signUp,name='signup'),
    path('signup_job_seeker/',signUpJobSeeker,name='sign_up_job_seeker'),
    path('signup_provider/',signUpProvider,name='register_provider'),
    path('login/',signIn,name='login'),
    path('login_jobseaker/',signIn2,name='login_jobseaker'),
    path('login_provider/',signInProvider,name='login_provider'),
    path('',home,name='home'),
    path('logout/',logout_view,name='logout'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('who_are_you/',who_are_you,name='who_are_you'),
    path('services/<str:service_type>/', service_providers, name='service_providers'),
]