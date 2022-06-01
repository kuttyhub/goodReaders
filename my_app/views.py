from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from django.template import Context,Template
from django import template


from my_app.models import User

# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    errors=[]
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        # print(email,password)
        if email and password:
            try:
                User.objects.get(email= email, password=password)
                return redirect("/")
            except:
                errors.append("Invalid email or password")
                
    return render(request,'login.html',{
        "errors":errors,
    })

def signup(request):
    errors=[]

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        if name and email and password:
            ins=User(name= name,email=email,password=password)
            ins.save()
            print("Data saved sucessfully")
            return redirect("/")
        else:
            errors.append("Enter all the fields")
    
    return render(request,'signup.html',{
        'errors':errors,
    })



