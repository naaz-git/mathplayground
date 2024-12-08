# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .forms import ParentSignUpForm, KidForm
from .models import Parent, Kid
from django.contrib.auth.hashers import check_password

def home_view(request):
    return render(request, 'home/indexpage.html')

def loginsuccess_view(request):
    if request.user.is_authenticated:
        # Get the Parent object linked to the current logged-in user
        try:
            parent = Parent.objects.get(user=request.user)
            # Get the kids related to this parent
            kids = Kid.objects.filter(parent=parent)
        except Parent.DoesNotExist:
            # If the parent does not exist for the logged-in user, handle the error
            return redirect('login')  # Redirect to login if no parent is found
        
        # Pass the kids data to the template
        return render(request, 'home/profileselectionpage.html', {'kids': kids})
    else:
        return redirect('login')  # Redirect to login if user is not authenticated

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Retrieve user by email
            user = User.objects.get(email=email)

            # Check if password is correct
            if check_password(password, user.password):
                login(request, user)
                # Clear previous messages to avoid showing old error messages
                storage = get_messages(request)
                for _ in storage:
                    pass  # Iterate to clear existing messages
                print('SHASHANK Login was successful')
                return redirect('loginsuccess')  # Redirect to homepage or dashboard
            else:
                print('Invalid email or password')
                messages.error(request, 'Invalid email or password.')
        except User.DoesNotExist:
            print('User does not exist')
            messages.error(request, 'Invalid email or password.')

    return render(request, 'home/loginpage.html')  # Return the login template

def signup_view(request):
    if request.method == 'POST':
        parent_form = ParentSignUpForm(request.POST)
        print('ParentSignUpForm')
        
        if parent_form.is_valid():
            print('if parent_form.is_valid() check')

            parent = parent_form.save()

            # If the parent form is valid, we can save the kids as well
            # Get the number of kids from the form data
            num_of_kids = parent_form.cleaned_data['num_of_kids']  # Retrieve the number of kids from the form
            for i in range(1, num_of_kids + 1):
                print('num_of_kids', num_of_kids)
                kid_name = request.POST.get(f'kid{i}Name')
                kid_age = request.POST.get(f'kid{i}Age')
                if kid_name and kid_age:
                    kid = Kid(parent=parent, kid_name=kid_name, kid_age=kid_age)
                    kid.save()
                    print(kid_name)

            # Redirect to a success page or profile page after saving
            messages.success(request, "Registration successful! You can log in now.")

            # Create user based on the parent email and password
            email = parent_form.cleaned_data['email']  # Retrieve email from the form
            password = parent_form.cleaned_data['password']  # Retrieve password from the form

            # Create user and save
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()

            # Optionally link the user to the parent model if you have a relationship
            parent.user = user  # If you have a user field in the Parent model
            parent.save()

            return redirect('login')  # Redirect to the login page after successful registration
        else:
            print(parent_form.errors)  # Print the errors to the console
            # Optionally, add this to the context to display the errors on the template
            messages.error(request, "There was an error with your form submission.")
    else:
        parent_form = ParentSignUpForm()

    return render(request, 'home/signuppage.html', {'parent_form': parent_form})

def profile_view(request, parent_id):
    parent = Parent.objects.get(id=parent_id)
    kids = Kid.objects.filter(parent=parent)
    return render(request, 'home/profile.html', {'parent': parent, 'kids': kids})

def questionchoice_view(request):
    return render(request, 'home/questionchoice.html')

def answer_sheet_view(request):
    return render(request, 'home/indexpage.html')

