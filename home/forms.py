from django import forms
from .models import Parent, Kid

from django import forms
from django.core.exceptions import ValidationError
from .models import Parent

class ParentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput, label="Re-enter Password")
    num_of_kids = forms.IntegerField(min_value=1, max_value=5, required=True)  # Add this field for form input

    class Meta:
        model = Parent
        fields = ['parent_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')

        if password != repassword:
            raise ValidationError("Passwords do not match.")
        
        return cleaned_data

class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['kid_name', 'kid_age']
