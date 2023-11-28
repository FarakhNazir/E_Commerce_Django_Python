from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import authenticate , login, logout
from accounts.models import Profile
from .models import Profile
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            messages.warning(request, 'User Name not found. Please Sign Up first. ')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].Profile.is_email_verified():
            messages.warning(request, 'account not verified ')
            return HttpResponseRedirect(request.path_info)
        
        user = authenticate(username = email, password = password)
        if user : 
            login(request, user)
            return HttpResponseRedirect('/')
        
        messages.warning(request, 'Invalid Credentials')
        return HttpResponseRedirect(request.path_info)
    
    return  render(request, "accounts/login.html")

def register_page(request):
    if request.method == 'POST':
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        email  = request.POST.get('email')
        password  = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email  )
        
        if user_obj.exists():
            messages.warning(request , 'Email is already taken')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name =  first_name , last_name = last_name , email = email, username = email) 
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request , 'Email has been sent to your email.')
        return HttpResponseRedirect(request.path_info)
    
    
    return render(request , 'accounts/register.html')

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        is_email_verified = True
        user.save()
        return HttpResponseRedirect('/')
    
    except Exception as e:
        return HttpResponse('Invalid Email Token')
    
    