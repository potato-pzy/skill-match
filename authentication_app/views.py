from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser,JobSeeker,JobProvider
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def signUp(request):
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        context = {
            'first_name':firstName,
            'email':email,
        }
        if password != confirm_password:
            messages.error(request,"Password doesn't match")
            return render(request,'authentication_app/sign_up.html',context)
        else:
            CustomUser.objects.create_user(first_name=firstName,email=email,password=password,username=email)
            return redirect(signIn)
    return render(request,'authentication_app/sign_up.html')

def signUpJobSeeker(request):
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        is_job_seeker = request.POST.get('is_job_seeker')
        
        context = {
            'first_name': firstName,
            'email': email,
        }
        
        if is_job_seeker:
            phone = request.POST.get('phone')
            available_days = request.POST.getlist('available_days')  # This returns a list of selected days
            availability = ', '.join(available_days)
            area = request.POST.get('area')
            profile = request.FILES.get('profile')
            job_role = request.POST.get('job_role')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            context['phone'] = phone
            context['availability'] = availability
            context['area'] = area
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'authentication_app/sign_up_job_seeker.html', context)
        
        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'authentication_app/sign_up_job_seeker.html', context)
        
        # Create the user and job seeker
        try:
            user = CustomUser.objects.create_user(
                first_name=firstName,
                email=email,
                password=password,
                username=email,
                is_job_seeker=is_job_seeker
            )
            
            if is_job_seeker:
                profile = request.FILES.get('profile')
                JobSeeker.objects.create(
                    user=user,
                    phone=phone,
                    availability=availability,
                    area=area,
                    profile=profile if profile else None,  # Handle missing profile
                    job_role = job_role,
                    start_time = start_time,
                    end_time = end_time,
                )

            
            return redirect(signIn)
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'authentication_app/sign_up_job_seeker.html', context)

    return render(request, 'authentication_app/sign_up_job_seeker.html')

def signIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if the user exists
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # If the email does not match any user
            messages.error(request, "The email you entered does not exist!")
            return render(request, 'authentication_app/login.html', {'email': email})

        # Authenticate the user using email/password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect(home)
            # Redirect based on user role
        else:
            # If authentication fails
            messages.error(request, "Email or Password is incorrect!")
            return render(request, 'authentication_app/login.html', {'email': email})
    else:
        return render(request, 'authentication_app/login.html')
    
def signIn2(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if the user exists
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # If the email does not match any user
            messages.error(request, "The email you entered does not exist!")
            return render(request, 'authentication_app/login_jobseaker.html', {'email': email})

        # Authenticate the user using email/password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect(home)
            # Redirect based on user role
        else:
            # If authentication fails
            messages.error(request, "Email or Password is incorrect!")
            return render(request, 'authentication_app/login_jobseaker.html', {'email': email})
    else:
        return render(request, 'authentication_app/login_jobseaker.html')
def home(request):
    
    return render(request,'authentication_app/index.html')

def logout_view(request):
    logout(request)
    return redirect(home)

def who_are_you(request):
    return render(request,'authentication_app/who_are_you.html')

def contact(request):
    return render(request,'authentication_app/contact.html')

def about(request):
    return render(request,'authentication_app/about.html')

def signUpProvider(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        company_name = request.POST.get('company_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        context = {
            'username': username,
            'email': email,
            'company_name': company_name,
            'phone': phone,
            'address': address,
        }
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'authentication_app/sign_up.html', context)
        
        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'authentication_app/sign_up.html', context)
        
        # Create the user and job provider
        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_job_provider=True
            )
            
            JobProvider.objects.create(
                user=user,
                company_name=company_name,
                phone=phone,
                address=address
            )
            
            return redirect('login_provider')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'authentication_app/sign_up.html', context)

    return render(request, 'authentication_app/sign_up.html')

def signInProvider(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if the user exists and is a job provider
            user = CustomUser.objects.get(email=email, is_job_provider=True)
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid email or you are not registered as a job provider!")
            return render(request, 'authentication_app/login.html', {'email': email})

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_job_provider:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "Email or Password is incorrect!")
            return render(request, 'authentication_app/login.html', {'email': email})
    
    return render(request, 'authentication_app/login.html')

def service_providers(request, service_type):
    """View to display service providers of a specific type"""
    providers = JobSeeker.objects.filter(job_role__iexact=service_type)
    
    context = {
        'service_type': service_type.title(),  # Capitalize the service type
        'providers': providers
    }
    
    return render(request, 'services/service_providers.html', context)