from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        
class Updated_user_profile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'email':'Email'}
    
class Updated_admin_profile(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'
        label={'email':'Email'}
    