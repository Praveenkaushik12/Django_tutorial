from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


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

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    else:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
                
        
        else:
            fm=AuthenticationForm()
        return render(request,'myapp/login.html',{'form':fm})


def profile(request):
    if request.user.is_authenticated:
        return render(request,'myapp/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')