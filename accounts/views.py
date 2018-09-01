from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from . import pyfunctions
from .models import Temp_user
from django.urls import reverse


def login(request):
    if request.user.is_authenticated:
        return redirect(request.GET['next'] or 'index')
    else:
        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                error = "username or password invalid! Try signing up if not already!"
                if Temp_user.objects.filter(uname=request.POST['username']).exists():
                    error = "Please Varify your email before logging in!"
                
                return render(request, 'accounts/login.html',{"title":"login_error", 'error':error})
        else:
            return render(request, 'accounts/login.html', {"title":"log in"})


def  logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            
            #-1. form validation
            #-2. save data in local table (if not already there, in both user tables)
                #i. generate token
                #ii. send email
                #iii. show Email sent page
            #-3. if username exists, show an error page

            # validations:
            # =============
            # if not form.is_valid():
            #     error = "Invalid Form details!"
            error = ""
            
            if request.POST["password1"] != request.POST["password2"]:
                error = "Passwords must match!"
            elif Temp_user.objects.filter(uname = request.POST["username"]).exists() or User.objects.filter(username = request.POST["username"]).exists():
                error = "Username already taken. Try Loging in!"
            elif Temp_user.objects.filter(email=request.POST["email"]).exists() or User.objects.filter(email=request.POST["email"]).exists():
                error = "An account already exists with that email!"
            
            # main show starts from here:
            # ===========================
            else:
                token = pyfunctions.generate_url()
                Temp_user.objects.create(uname=request.POST['username'], password=make_password(request.POST['password1']), email=request.POST['email'], token=token)
                reciever = [request.POST["email"]]
                if pyfunctions.varification_mailto(reciever, token):
                    img = '<img src="' + pyfunctions.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
                    return render(request, 'accounts/resend.html', {'title':'email varifiaction','case':'first_time', 'token':token, 'cute_image': img})
                else:
                    responce = ["ERROR! mail not sent"] 
                img = pyfunctions.get_cute_image()
                responce.append('<img src="' + img + '" height="200px" width="200px" alt="a cute animal image">')
                return render(request, 'accounts/message.html', {'title': 'signed up', 'messages':responce})
            if error:
                return render(request, 'accounts/signup.html', {'title':'signup error', 'error':error})
        
        else: # request.method is "GET"
            return render(request, 'accounts/signup.html', {'title':'signup'})


def activate(request):
    title = "email_varifiaction" # used to display as page title, nothing special!
    path = str(request.path)
    key = path.split("validate/", 1)[1]
    error = ""

    if Temp_user.objects.filter(token=key).exists():
        tuser = Temp_user.objects.get(token=key)
        
        if tuser.varify_time(timezone.now()): # checking whether the link is valid!
            # Adding to user
            user = User.objects.create_user(username=tuser.uname, password=tuser.password, email=tuser.email)
            user.password = tuser.password # Using this since django will re-hash the hashed password => Thus explicitely, re mentioning it!
            user.is_active = True
            user.save()

            # Deleting from Temp_user
            Temp_user.objects.filter(uname=tuser.uname).delete()
            login = '"' + reverse('login') + '"'
            message = [
                "Welcome to snapshare!", 
                """Thanks for varifying your email! try <a href=""" + login + """>logging in! </a>"""
            ]
        
        else:
            img = '<img src="' + pyfunctions.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
            return render(request, 'accounts/resend.html', {'title':"email error",'case':'expire', 'token':tuser.token, 'cute_image': img})
    
    else:
        title = "404"
        message = ["This way does not leads to mars!"]

    img = pyfunctions.get_cute_image()
    message.append('<img src="' + img + '" height="200px" width="200px" alt="a cute animal image">')
    return render(request, 'accounts/message.html', {'title':title, 'messages':message})


def resend(request):
    if request.method == 'POST' and Temp_user.objects.filter(token=request.POST["token"]).exists():
        token = request.POST['token']
        tuser = Temp_user.objects.get(token=token)
        new_token = pyfunctions.generate_url()
        tuser.token = new_token
        tuser.save()
        reciver = [tuser.email]
        token = new_token
        if pyfunctions.varification_mailto(reciver, token):
            img = '<img src="' + pyfunctions.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
            return render(request, 'accounts/resend.html', {'title':'email varifiaction','case':'resend', 'token':new_token, 'cute_image': img})
        else:
            message = ["ERROR! mail not sent"] 
    else:
        title = "404"
        message = ["Well, you have came a long way, to vain!"]
    message.append('<img src="' + pyfunctions.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">')
    return render(request, 'accounts/message.html', {'title':"404", 'messages':message})


