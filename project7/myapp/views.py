from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .forms import SignUpForm,Updated_user_profile,Updated_admin_profile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash


# Create your views here.
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
          fm.save()
          messages.success(request,'Account has created successfully!!')
        #permission nd authorization
        #   user=fm.save()
        #   group=Group.objects.get(name='Editor')
        #   user.groups.add(group)
        
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


#profile views
def profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser == True:
                fm=Updated_admin_profile(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                fm=Updated_user_profile(request.POST,instance=request.user)
                users=None
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile has changed!!')
        else:
            if request.user.is_superuser==True:
                fm=Updated_admin_profile(instance=request.user)
                users=User.objects.all()
            else:
                fm=Updated_user_profile(instance=request.user)
                users=None
        return render(request,'myapp/profile.html',{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_change_pass(request):
   if request.user.is_authenticated: 
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password changed successfully!")
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'myapp/change_pass.html',{'form':fm})
   else:
        return HttpResponseRedirect('/login/')
    

def user_dashboard(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=Updated_admin_profile(instance=pi)
        return render(request,'myapp/dashboard.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')