from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    parent_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Use a valid User ID

    def __str__(self):
        return self.parent_name

class Kid(models.Model):
    parent = models.ForeignKey(Parent, related_name='kids', on_delete=models.CASCADE)
    kid_name = models.CharField(max_length=100)
    kid_age = models.IntegerField()

    def __str__(self):
        return self.kid_name
    
