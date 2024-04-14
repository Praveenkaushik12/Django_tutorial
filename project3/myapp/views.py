from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
          fm.save()
        messages.success(request,'Account has created successfully!!')
        
    else:
        fm=SignUpForm()
    return render(request,'myapp/sign_up.html',{'form':fm})
    