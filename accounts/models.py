from django.db import models

# Create your models here.

class Parent(models.Model):
    parent_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)  # You should validate this on the form side
    num_of_kids = models.IntegerField(default=0)

    def __str__(self):
        return self.parent_name

class Kid(models.Model):
    parent = models.ForeignKey(Parent, related_name='kids', on_delete=models.CASCADE)
    kid_name = models.CharField(max_length=100)
    kid_age = models.IntegerField()

    def __str__(self):
        return self.kid_name
