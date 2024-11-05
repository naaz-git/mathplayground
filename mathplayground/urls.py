"""
URL configuration for mathplayground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # Import the view from your app
from home.views import *  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', home_view, name="home"),  # Add this line for the root path
    path('signup/', signup_view, name="signup"),  # Signup page
    path('login/', login_view, name='login'),  # Login page (add a distinct path for login)
    path('loginsuccess/', loginsuccess_view, name="loginsuccess"),  # loginsuccess
    path('questionchoice/', questionchoice_view, name="questionchoice"),  # loginsuccess

]
