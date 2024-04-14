from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name']='PraVeen'
    request.session['lname']='kaushik'
    return render(request,'myapp/setsession.html')

def get_session(request):
    # name=request.session['name']
    name=request.session.get('name',default='Guest')
    lname=request.session.get('lname',default='Guest1')
    keys=request.session.keys()
    items=request.session.items()
    return render(request,'myapp/getsession.html',{'name':name,'lname':lname,'keys':keys,'items':items})

def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render(request,'myapp/delsession.html')