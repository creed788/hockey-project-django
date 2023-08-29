from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Contact

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control my-3'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class' : 'form-control my-3'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class' : 'form-control my-3'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        lables = {'email' : 'Email'}
        widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control'})}
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )

class ContactForm(forms.ModelForm):
     name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
     email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control' }))
     subject = forms.CharField(max_length=100, label='Subject', widget=forms.TextInput(attrs={'class': 'form-control'}))
     message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}), label='Message')
    
     class Meta:
        model = Contact
        fields = ['name', 'email','subject', 'message']
