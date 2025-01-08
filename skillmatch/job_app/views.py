from django.shortcuts import render
from authentication_app.models import CustomUser,JobSeeker 
# Create your views here.
# electrician_view
from django.shortcuts import render
from authentication_app.models import JobSeeker

# def electrician_view(request):
#     electricians = JobSeeker.objects.select_related('user').filter(user__is_job_seeker=True)
#     context = {
#         'electricians': electricians,  # Updated key name to be plural for clarity
#     }
#     return render(request, 'indexcontent/electrician.html', context)
def electrician_view(request):
    electricians = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Electrician'  # Filter only electricians (case-insensitive)
    )
    print(electricians)
    context = {
        'electricians': electricians,
    }
    return render(request, 'indexcontent/electrician.html', context)


# plumber_view
def plumber_view(request):
    plumber = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Plumber'  # Filter only electricians (case-insensitive)
    )
    context = {
        'plumber':plumber,
    }
    return render(request, 'indexcontent/plumber.html',context)
#acservice_view
def acservice_view(request):
    acservice = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='AC service'  # Filter only ac service (case-insensitive)
    )
    context = {
        'acservice':acservice,
    }
    return render(request, 'indexcontent/acservice.html',context)
#homedeepcleaning_view
def homedeepcleaning_view(request):
    homedeepcleaning = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Home deep cleaning'  # Filter only ac service (case-insensitive)
    )
    context = {
        'homedeepcleaning':homedeepcleaning,
    }
    return render(request, 'indexcontent/homedeepcleaning.html',context)
#dogwalker_view
def dogwalker_view(request):
    dogwalker = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Dog walker'  # Filter only dogwalker (case-insensitive)
    )
    context = {
        'dogwalker':dogwalker,
    }
    return render(request, 'indexcontent/dogwalker.html',context)
#driver_view
def driver_view(request):
    driver = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Driver'  # Filter only driver (case-insensitive)
    )
    context = {
        'driver':driver,
    }
    return render(request, 'indexcontent/driver.html',context)
#beautician_view
def beautician_view(request):
    beautician = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Beautician'  # Filter only beautician (case-insensitive)
    )
    context = {
        'beautician':beautician,
    }
    return render(request, 'indexcontent/beautician.html',context)
#lumberjack_view
def lumberjack_view(request):
    lumberjack = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Lumberjack'  # Filter only lumberjack (case-insensitive)
    )
    context = {
        'lumberjack':lumberjack,
    }
    return render(request, 'indexcontent/lumberjack.html',context)
#lawncare_view
def lawncare_view(request):
    lawncare = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Lawncare'  # Filter lawncare (case-insensitive)
    )
    context = {
        'lawncare':lawncare,
    }
    return render(request, 'indexcontent/lawncare.html',context)
#welldigger_view
def welldigger_view(request):
    welldigger = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Welldigger'  # Filter only welldigger (case-insensitive)
    )
    context = {
        'welldigger':welldigger,
    }
    return render(request, 'indexcontent/welldigger.html',context)
#plantkeeper_view
def plantkeeper_view(request):
    plantkeeper = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='plantkeeper'  # Filter only plantkeeper (case-insensitive)
    )
    context = {
        'plantkeeper':plantkeeper,
    }
    return render(request, 'indexcontent/plantkeeper.html',context)
#welder_view
def welder_view(request):
    welder = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Welder'  # Filter only welder (case-insensitive)
    )
    context = {
        'welder':welder,
    }
    return render(request, 'indexcontent/welder.html',context)