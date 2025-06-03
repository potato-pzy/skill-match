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
]