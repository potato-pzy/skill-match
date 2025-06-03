from django.shortcuts import render, redirect
from authentication_app.models import CustomUser,JobSeeker 
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
# electrician_view
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
    context = {
        'service_type': 'Electrician',
        'providers': electricians,
    }
    return render(request, 'services/service_providers.html', context)


# plumber_view
def plumber_view(request):
    plumbers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Plumber'  # Filter only plumbers (case-insensitive)
    )
    context = {
        'service_type': 'Plumber',
        'providers': plumbers,
    }
    return render(request, 'services/service_providers.html', context)

#acservice_view
def acservice_view(request):
    ac_providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='AC service'  # Filter only ac service (case-insensitive)
    )
    context = {
        'service_type': 'AC Service',
        'providers': ac_providers,
    }
    return render(request, 'services/service_providers.html', context)

#homedeepcleaning_view
def homedeepcleaning_view(request):
    cleaning_providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Home deep cleaning'  # Filter only deep cleaning providers
    )
    context = {
        'service_type': 'Home Deep Cleaning',
        'providers': cleaning_providers,
    }
    return render(request, 'services/service_providers.html', context)

#dogwalker_view
def dogwalker_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Dogwalker'  # Filter only dogwalker (case-insensitive)
    )
    context = {
        'service_type': 'Dog Walker',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#driver_view
def driver_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Driver'  # Filter only driver (case-insensitive)
    )
    context = {
        'service_type': 'Driver',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#beautician_view
def beautician_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Beautician'  # Filter only beautician (case-insensitive)
    )
    context = {
        'service_type': 'Beautician',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#lumberjack_view
def lumberjack_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Lumberjack'  # Filter only lumberjack (case-insensitive)
    )
    context = {
        'service_type': 'Lumberjack',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#lawncare_view
def lawncare_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Lawncare'  # Filter lawncare (case-insensitive)
    )
    context = {
        'service_type': 'Lawn Care',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#welldigger_view
def welldigger_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Welldigger'  # Filter only welldigger (case-insensitive)
    )
    context = {
        'service_type': 'Well Digger',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#plantkeeper_view
def plantkeeper_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='plantkeeper'  # Filter only plantkeeper (case-insensitive)
    )
    context = {
        'service_type': 'Plant Keeper',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

#welder_view
def welder_view(request):
    providers = JobSeeker.objects.select_related('user').filter(
        user__is_job_seeker=True,
        job_role__iexact='Welder'  # Filter only welder (case-insensitive)
    )
    context = {
        'service_type': 'Welder',
        'providers': providers,
    }
    return render(request, 'services/service_providers.html', context)

def login_jobseeker_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password) and user.is_job_seeker:
                login(request, user)
                return redirect('profile')  # Redirect to profile page after login
            else:
                messages.error(request, 'Invalid credentials or not a job seeker')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist')
    return render(request, 'authentication/login_jobseeker.html')

def logout_jobseeker_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

def register_jobseeker_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        job_role = request.POST.get('job_role')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register_jobseeker')
            
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register_jobseeker')
            
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register_jobseeker')
            
        # Create the user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_job_seeker=True
        )
        
        # Create the job seeker profile
        JobSeeker.objects.create(
            user=user,
            job_role=job_role
        )
        
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login_jobseeker')
        
    return render(request, 'authentication/register_jobseeker.html')

def profile_view(request):
    """Display job seeker profile information"""
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to view your profile.')
        return redirect('login_jobseeker')
    
    if not request.user.is_job_seeker:
        messages.error(request, 'Access denied. Job seeker profile only.')
        return redirect('home')
    
    try:
        jobseeker = JobSeeker.objects.get(user=request.user)
        context = {
            'jobseeker': jobseeker,
            'user': request.user,
        }
        return render(request, 'job_app/profile.html', context)
    except JobSeeker.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('home')