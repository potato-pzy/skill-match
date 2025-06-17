from django.urls import path
from .views import *
urlpatterns = [
    path('electrician/',electrician_view,name='electrician'),
    path('plumber/',plumber_view,name='plumber'),
    path('acservice/',acservice_view,name='acservice'),
    path('homedeepcleaning/',homedeepcleaning_view,name='homedeepcleaning'),
    path('dogwalker/',dogwalker_view,name='dogwalker'),
    path('driver/',driver_view,name='driver'),
    path('beautician/',beautician_view,name='beautician'),
    path('lumberjack/',lumberjack_view,name='lumberjack'),
    path('lawncare/',lawncare_view,name='lawncare'),
    path('welldigger/',welldigger_view,name='welldigger'),
    path('plantkeeper/',plantkeeper_view,name='plantkeeper'),
    path('welder/',welder_view,name='welder'),
    path('jobseeker/login/', login_jobseeker_view, name='login_jobseeker'),
    path('jobseeker/logout/', logout_jobseeker_view, name='logout_jobseeker'),
    path('jobseeker/register/', register_jobseeker_view, name='register_jobseeker'),
    path('jobseeker/profile/', profile_view, name='profile'),
    path('jobseeker/profile/edit/', edit_profile_view, name='edit_profile'),
    path('schedule/<int:jobseeker_id>/', schedule_appointment, name='schedule_appointment'),
    path('appointments/', view_appointments, name='view_appointments'),
    path('appointments/<int:appointment_id>/update/', update_appointment_status, name='update_appointment_status'),
]