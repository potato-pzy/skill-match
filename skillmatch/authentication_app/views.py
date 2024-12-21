from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
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
   
def home(request):
    
    return render(request,'authentication_app/index.html')

def logout_view(request):
    logout(request)
    return redirect(home)

def who_are_you(request):
    return render(request,'authentication_app/who_are_you.html')

def about(request):
    return render(request,'authentication_app/about.html')