from django.contrib import admin

# Register your models here.
from .models import Parent, Kid  # Import your models

# Register models to be visible in the admin panel
admin.site.register(Parent)
admin.site.register(Kid)
