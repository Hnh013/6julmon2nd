from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
   
   
    class Meta:
    	model = User
    	fields = ('first_name','last_name','email', 'username', 'password1', 'password2')

    


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user_role','profile_pic')


class AstroProfileForm(forms.ModelForm):
	class Meta:
		model = Astro_Profile
		fields = ('skill','language','experience','location','about',)

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email', 'username')
		exclude = ()

class WalletForm(forms.ModelForm):
	class Meta:
		model = Wallet
		exclude = ('balance', 'user' )