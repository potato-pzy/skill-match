from django.shortcuts import render
from authentication_app.models import CustomUser,JobSeeker 
# Create your views here.
# electrician_view
def electrician_view(request):
    electrician = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'electrician':electrician,
    }
    return render(request, 'indexcontent/electrician.html',context)
# plumber_view
def plumber_view(request):
    plumber = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'plumber':plumber,
    }
    return render(request, 'indexcontent/plumber.html',context)
#acservice_view
def acservice_view(request):
    acservice = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'acservice':acservice,
    }
    return render(request, 'indexcontent/acservice.html',context)
#homedeepcleaning_view
def homedeepcleaning_view(request):
    homedeepcleaning = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'homedeepcleaning':homedeepcleaning,
    }
    return render(request, 'indexcontent/homedeepcleaning.html',context)
#dogwalker_view
def dogwalker_view(request):
    dogwalker = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'dogwalker':dogwalker,
    }
    return render(request, 'indexcontent/dogwalker.html',context)
#driver_view
def driver_view(request):
    driver = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'driver':driver,
    }
    return render(request, 'indexcontent/driver.html',context)
#beautician_view
def beautician_view(request):
    beautician = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'beautician':beautician,
    }
    return render(request, 'indexcontent/beautician.html',context)
#lumberjack_view
def lumberjack_view(request):
    lumberjack = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'lumberjack':lumberjack,
    }
    return render(request, 'indexcontent/lumberjack.html',context)
#lawncare_view
def lawncare_view(request):
    lawncare = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
    context = {
        'lawncare':lawncare,
    }
    return render(request, 'indexcontent/lawncare.html',context)

