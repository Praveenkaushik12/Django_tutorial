from django.shortcuts import render,HttpResponse

# Create your views here.
def set_session(request):
    request.session['name']='PraVeen'
    return render(request,'myapp/setsession.html')

def get_session(request):
    # name=request.session['name']
    if 'name' in request.session:
        name=request.session['name']
        request.session.modified=True
        return render(request,'myapp/getsession.html',{'name':name})
    else:
        return HttpResponse('Session has been Expired!')

def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request,'myapp/delsession.html')