from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import models
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
import random

from .utils import get_activation_code

# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        gender = request.POST['gender']
        phonenumber = request.POST['phone']
        activation_code = get_activation_code()
#
        if password == password2:
            from .models import CustomUser
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,"Username is Taken!")
                return render(request,'register.html')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,"Email is Taken!")
                return render(request,'register.html')
            else:
                user = CustomUser.objects.create_user(username=username,first_name=first_name,email=email,password=password,gender=gender,phonenumber=phonenumber,activation_code=activation_code)
                user.save()
                messages.info(request,"New user created!")
                return redirect('login')
        else:
            messages.info(request,"Password not matching!")
            return render(request,'register.html')

    return render(request,'register.html')

# try:
#             send_mail(
#                     subject,
#                     message,
#                     email, #sender
#                     ['inmotion@dtechnologys.com',], #receipient
#                     fail_silently=False,
#                 )

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if not request.user.is_authenticated:
        from .models import CustomUser
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if CustomUser.objects.filter(username=username)[0].account_active ==True:
                User = auth.authenticate(username=username,password=password)

                if User is not None:
                    auth.login(request,User)
                    if request.GET.get('next',None):
                        return HttpResponseRedirect(request.GET['next'])
                    return redirect('/')
                else:
                    messages.info(request,'Invalid credentials')
                    return render(request,'login.html')
            return render(request,'activate.html')
            
        else:
            return render(request,'login.html')
    else:
        return redirect("/")