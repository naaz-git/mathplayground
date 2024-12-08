# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        # Get form data
        parent_name = request.POST.get('parentName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        kid1_name = request.POST.get('kid1Name')
        kid1_age = request.POST.get('kid1Age')
        kid2_name = request.POST.get('kid2Name')
        kid2_age = request.POST.get('kid2Age')

        # Check password match
        if password != repassword:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Save parent information
        parent = Parent.objects.create(
            parent_name=parent_name,
            email=email,
            password=make_password(password)  # Hash the password
        )

        # Save kids information if provided
        if kid1_name and kid1_age:
            Kid.objects.create(parent=parent, name=kid1_name, age=int(kid1_age))

        if kid2_name and kid2_age:
            Kid.objects.create(parent=parent, name=kid2_name, age=int(kid2_age))

        messages.success(request, "Sign-up successful!")
        return redirect('login')  # Redirect to the login page after successful signup

    return render(request, 'accounts/signupPage.html')

'''def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            messages.success(request, "Signup successful!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form}'''

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    parents = Parent.objects.all()
    for parent in parents:
        print(f"Parent Name: {parent.parent_name}, Email: {parent.email}")


    return render(request, 'accounts/login.html', {'form': form})

