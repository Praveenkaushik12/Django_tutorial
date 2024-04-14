from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','password']