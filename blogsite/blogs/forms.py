from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    # class Meta:
        # model = User
        # fields = ["username", "email", "password1", "password2"]

        # widgets = {
        #     'username' : forms.CharField(widget=forms.TextInput(attrs={
        #         'class': 'form-control', 
        #         'placeholder':"Enter username: ",
        #     })),
        #     'email' : forms.CharField(widget=forms.EmailInput(attrs={'class':  
        #         'form-control', 'placeholder': 'Enter email'}))  ,

        #     'password1' : forms.PasswordInput(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})),
        #     'password2' : forms.PasswordInput(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))             
        # }
            class Meta:
                print("this clled")
                model = User  
                fields = ['username', 'email', 'password1', 'password2']   
                widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
                    'email': forms.EmailInput(attrs={'class': 
                    'form-control', 'placeholder': 'Enter email'}),
                    'password1':  
                    forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
                    'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),

                }
class CustomRegForm(UserCreationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder':"Enter username: ",
        }))
        email = forms.CharField(widget=forms.EmailInput(attrs={'class':  
            'form-control', 'placeholder': 'Enter email'}))  

        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})) 
