from django.shortcuts import render,redirect
from .models import *
import core.pw as pw
# Create your views here.
def home_view(request):
    return render(request,'guest/index.html')

def user_home_view(request):
    return render(request,'user/index.html')

def login(request):
    try:
        if request.session['email']:
            return redirect('/u/home/')
    except:
        pass
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        us = User.objects.get(email=email)
        if not pw.ComparePassword(password,us.password):
            render(request,'guest/login.html')

        request.session['email'] = us.email
        return redirect('/u/home/')
    
    return render(request,'guest/login.html')

def logout(request):
    del request.session['email']
    return redirect('/')

def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        try:
            us = User.objects.get(username=username)
            if us is not None:
                return render(request,'guest/register.html')
            us = User.objects.get(email=email)
            if us is not None:
                return render(request,'guest/register.html')
        except:
            pass

        
        password = request.POST['password']
        passwordHash = pw.GeneratePassword(password)
        us = User.objects.create_user(username,email,passwordHash)
        us.save()

        request.session['email'] = us.email

        return redirect('/u/home/')
    
    return render(request,'guest/register.html')

def profile_view(request):
    email = request.session.get('email')
    user = User.objects.get(email=email)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    return render(request,'user/profile.html',{'user':user})