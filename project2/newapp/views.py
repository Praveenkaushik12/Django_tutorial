from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def show_data(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        messages.add_message(request,messages.SUCCESS,'You have been registered!!')
        messages.info(request,"you can login now!")
        
    else:
        fm=StudentRegistration()
    return render(request,'newapp/form.html',{'form':fm})