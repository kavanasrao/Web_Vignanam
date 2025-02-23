from django import forms 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=40,validators=[RegexValidator(regex=r'^[a-zA-Z]*$', message='Firstname must be alphabetic')])
    last_name = forms.CharField(max_length=40,validators=[RegexValidator(regex=r'^[a-zA-Z]*$',message='lastname must be alphabetic')])
    username = forms.CharField(max_length=100,validators=[RegexValidator(regex=r'^[a-zA-Z0-9_-]*$',message='user name must be alphanumeric and can have "_"&"-"')] )
    email=forms.EmailField(widget=forms.EmailInput(),validators=[RegexValidator(regex=r'^[a-zA-Z0-9]+@gmail\.com$',message='Only @gmail.com can be used')])
    password1=forms.CharField( widget=forms.PasswordInput())
    password2 = forms.CharField( widget=forms.PasswordInput())
    
    def clean_password(self):
        password1=self.cleaned_data.get['password1']
        password2=self.cleaned_data.get['password2']
        if password1!= password2:
            raise ValidationError('Password is not matching')
        
        return password2
    

class SigninForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
    
            