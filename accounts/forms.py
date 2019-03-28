from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class myforms(forms.Form):

#     def set_attr(self, property, value):
#         self.

class login_form(forms.Form):
    email=forms.EmailField(max_length="40")
    password=forms.CharField(widget=forms.PasswordInput)
    

class signup_form(UserCreationForm):
    email=forms.EmailField(max_length="40")
    class Meta:
        model = User    
        fields=('username', 'email', 'password1', 'password2')
