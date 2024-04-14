from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
# Create your views here.
def showformdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form Validated!")
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=Student(name=nm,email=em,password=pwd)
            reg.save()     
    else:   
        fm=StudentRegistration()
    return render(request,'form.html',{'form':fm} )

