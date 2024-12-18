from django.shortcuts import render
from .models import *
def loginPage(request):
    return render(request,'app/login.html')

def UserReg(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['Email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user=User.objects.filter(Email=email,firstname=fname,lastname=lname,contact=contact)

        if user:
            message="User already exist"
            return render(request,'app/login.html',{'msg':message})
        else:
            if password==cpassword:
                new_user=User.objects.create(firstname=fname,lastname=lname,Email=email,contact=contact,password=password)
                message="User register successfully"
                return render(request,'app/register.html',{'msg':message})
            else:
                message="Password and confirm password does not match"
                return render(request,'app/login.html',{'msg':message})
            
def signpage(request):
    return render(request,'app/register.html')

def signup(request):
    if request.method=="POST":
        email=request.POST['Email']
        password=request.POST['password']

        user=User.objects.get(Email=email)
        if user:
            if user.password==password:
                request.session['firstname']=user.firstname
                request.session['lastname']=user.lastname
                request.session['Email']=user.Email
                return render(request,'app/home.html')
            else:
                message="password doesn't match"
                return render(request,'app/register.html',{'msg':message})
            
        else:
            message='user doesnot exist'
            return render(request,'app/login.html',{'msg':message})


