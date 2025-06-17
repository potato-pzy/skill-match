from django.shortcuts import render, redirect, get_object_or_404
from authentication_app.models import CustomUser,JobSeeker, JobProvider
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Appointment
from datetime import datetime, time
from django.contrib.auth.decorators import login_required

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
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        job_role = request.POST.get('job_role')
        phone = request.POST.get('phone')
        available_days = request.POST.getlist('available_days')  # This returns a list of selected days
        availability = ', '.join(available_days)
        area = request.POST.get('area')
        profile = request.FILES.get('profile')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        # Store form data in context for re-populating the form if there's an error
        context = {
            'first_name': first_name,
            'email': email,
            'phone': phone,
            'area': area,
            'job_role': job_role,
        }
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'authentication/register_jobseeker.html', context)
            
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'authentication/register_jobseeker.html', context)
            
        # Create the user
        try:
            user = CustomUser.objects.create_user(
                username=email,  # Use email as username
                email=email,
                password=password,
                first_name=first_name,
                is_job_seeker=True
            )
            
            # Create the job seeker profile
            JobSeeker.objects.create(
                user=user,
                first_name=first_name,
                job_role=job_role,
                phone=phone,
                availability=availability,
                area=area,
                profile=profile,
                start_time=start_time,
                end_time=end_time
            )
            
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login_jobseeker')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return render(request, 'authentication/register_jobseeker.html', context)
        
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

def edit_profile_view(request):
    """Edit job seeker profile information"""
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to edit your profile.')
        return redirect('login_jobseeker')
    
    if not request.user.is_job_seeker:
        messages.error(request, 'Access denied. Job seeker profile only.')
        return redirect('home')
    
    try:
        jobseeker = JobSeeker.objects.get(user=request.user)
        
        if request.method == 'POST':
            # Update user information
            request.user.first_name = request.POST.get('first_name')
            request.user.email = request.POST.get('email')
            request.user.save()
            
            # Update job seeker information
            jobseeker.first_name = request.POST.get('first_name')
            jobseeker.phone = request.POST.get('phone')
            jobseeker.job_role = request.POST.get('job_role')
            jobseeker.area = request.POST.get('area')
            
            # Handle availability days
            available_days = request.POST.getlist('available_days')
            jobseeker.availability = ', '.join(available_days)
            
            # Handle times
            jobseeker.start_time = request.POST.get('start_time')
            jobseeker.end_time = request.POST.get('end_time')
            
            # Handle profile picture
            if request.FILES.get('profile'):
                jobseeker.profile = request.FILES['profile']
            
            jobseeker.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
            
        context = {
            'jobseeker': jobseeker,
            'user': request.user,
            'job_roles': [
                ('electrician', 'Electrician'),
                ('acservice', 'AC Service'),
                ('plumber', 'Plumber'),
                ('beautician', 'Beautician'),
                ('dogwalker', 'Dog Walker'),
                ('driver', 'Driver'),
                ('homedeepcleaning', 'Home Deep Cleaning'),
                ('lawncare', 'Lawn Care'),
                ('lumberjack', 'Lumberjack'),
                ('plantkeeper', 'Plant Keeper'),
                ('welder', 'Welder'),
                ('welldigger', 'Well Digger'),
            ],
            'days_of_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'selected_days': [day.strip() for day in jobseeker.availability.split(',')] if jobseeker.availability else []
        }
        return render(request, 'job_app/edit_profile.html', context)
    except JobSeeker.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('home')

@login_required
def schedule_appointment(request, jobseeker_id):
    """Schedule an appointment with a job seeker"""
    if not request.user.is_authenticated or not hasattr(request.user, 'job_provider_profile'):
        messages.error(request, 'Only job providers can schedule appointments.')
        return redirect('home')
    
    job_seeker = get_object_or_404(JobSeeker, id=jobseeker_id)
    
    if request.method == 'POST':
        date_str = request.POST.get('appointment_date')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        notes = request.POST.get('notes', '')
        
        try:
            # Convert strings to datetime objects
            appointment_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
            
            # Check if the time is within job seeker's working hours
            seeker_start = datetime.strptime(job_seeker.start_time.strftime('%H:%M'), '%H:%M').time()
            seeker_end = datetime.strptime(job_seeker.end_time.strftime('%H:%M'), '%H:%M').time()
            
            if start_time < seeker_start or end_time > seeker_end:
                messages.error(request, f'Please schedule within working hours ({seeker_start.strftime("%H:%M")} - {seeker_end.strftime("%H:%M")})')
                return redirect('schedule_appointment', jobseeker_id=jobseeker_id)
            
            # Check for existing appointments
            existing_appointments = Appointment.objects.filter(
                job_seeker=job_seeker,
                appointment_date=appointment_date,
                status__in=['pending', 'confirmed']
            )
            
            for existing_apt in existing_appointments:
                if (start_time >= existing_apt.start_time and start_time < existing_apt.end_time) or \
                   (end_time > existing_apt.start_time and end_time <= existing_apt.end_time):
                    messages.error(request, 'This time slot is already booked.')
                    return redirect('schedule_appointment', jobseeker_id=jobseeker_id)
            
            # Create the appointment
            Appointment.objects.create(
                job_seeker=job_seeker,
                job_provider=request.user.job_provider_profile,
                appointment_date=appointment_date,
                start_time=start_time,
                end_time=end_time,
                notes=notes
            )
            
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('view_appointments')
            
        except ValueError as e:
            messages.error(request, 'Invalid date or time format.')
            return redirect('schedule_appointment', jobseeker_id=jobseeker_id)
    
    context = {
        'job_seeker': job_seeker,
        'min_date': datetime.now().date().strftime('%Y-%m-%d'),
    }
    return render(request, 'job_app/schedule_appointment.html', context)

@login_required
def view_appointments(request):
    """View appointments for the logged-in user"""
    print(f"User is authenticated: {request.user.is_authenticated}")
    print(f"User email: {request.user.email}")
    print(f"Is job seeker: {request.user.is_job_seeker}")
    print(f"Is job provider: {request.user.is_job_provider}")
    print(f"Has job_seeker_profile: {hasattr(request.user, 'job_seeker_profile')}")
    print(f"Has job_provider_profile: {hasattr(request.user, 'job_provider_profile')}")
    
    if hasattr(request.user, 'job_seeker_profile'):
        # Job seeker viewing their appointments
        appointments = Appointment.objects.filter(job_seeker=request.user.job_seeker_profile)
        user_type = 'job_seeker'
    elif hasattr(request.user, 'job_provider_profile'):
        # Job provider viewing their appointments
        appointments = Appointment.objects.filter(job_provider=request.user.job_provider_profile)
        user_type = 'job_provider'
    else:
        messages.error(request, 'Invalid user type.')
        return redirect('home')
    
    context = {
        'appointments': appointments,
        'user_type': user_type
    }
    return render(request, 'job_app/view_appointments.html', context)

@login_required
def update_appointment_status(request, appointment_id):
    """Update the status of an appointment"""
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    # Ensure only the job seeker can update their appointments
    if not hasattr(request.user, 'job_seeker_profile') or request.user.job_seeker_profile != appointment.job_seeker:
        messages.error(request, 'You do not have permission to update this appointment.')
        return redirect('view_appointments')
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['confirmed', 'cancelled', 'completed']:
            appointment.status = new_status
            appointment.save()
            messages.success(request, f'Appointment status updated to {new_status}.')
        else:
            messages.error(request, 'Invalid status.')
    
    return redirect('view_appointments')