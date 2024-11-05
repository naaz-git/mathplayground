# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def home_view(request):
    return render(request, 'home/indexpage.html')

def loginsuccess_view(request):
    return render(request, 'home/profileselectionpage.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Use the correct field
        if user is not None:
            login(request, user)
            return redirect('loginsuccess')  # Redirect to home after login
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'home/loginpage.html')  # Return the login template


def signup_view(request):
    if request.method == 'POST':
        parent_name = request.POST['parentName']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['repassword']
        
        # Check if passwords match
        if password != re_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')  # Redirect back to the signup page
        
        # Ensure the username is unique
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        # Create user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! You can log in now.")
        return redirect('login')  # Redirect to the login page after successful registration
    
    return render(request, 'home/signuppage.html')  # Render the signup template

def questionchoice_view(request):
    return render(request, 'home/questionchoice.html')
