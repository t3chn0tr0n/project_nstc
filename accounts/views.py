from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from . import addons
from .models import Temp_user
from csv import excel
from students.models import FormFills, Student
from teachers.models import Teacher


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'].strip(),password=request.POST['password'].strip())
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                error = "username or password invalid! Try signing up if not already!"
                if Temp_user.objects.filter(uname=request.POST['username']).exists():
                    error = "Please Verify your email before logging in!"
                
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

            uid = request.POST['username'].strip()
            email = request.POST['email'].strip()
            password1 = request.POST['password1'].strip()
            password2 = request.POST['password2'].strip()
            
            #-1. form validation
            #-2. check if the given user is a student or a teacher and has the valid email else STOP here.
            #-3. save data in local table (if not already there, in both user tables)
                #i. generate token
                #ii. send email
                #iii. show Email sent page
            #-4. if username exists, show an error page

            # validations:
            # =============

            error = ""
            try:
                that_stud = Student.objects.get(id=uid)
                flag_stud = True
                saved_email = that_stud.email
            except:
                flag_stud = False

            if not flag_stud:
                try:
                    that_teach = Teacher.object.get(id=uid)
                    flag_teach = True
                    saved_email = that_teach.email
                except:
                    flag_teach = False
                    error = "Unknown Id! Who are you exactly?? Go away..."
                    return render(request, 'accounts/signup.html', {'title':'signup error', 'error':error})
            
            # validate their email and if anything falls outs of place, DO NOT PROCEED further!!! 
            if flag_stud or flag_teach:
                if saved_email == email:
                    no_error = True
                else:
                    error = "Please give the Email that we know! This is critical to verify that its you!"
                    return render(request, 'accounts/signup.html', {'title':'signup error', 'error':error})
            # else : Unknown user is already handled above!
                    
            if password1 != password2:
                error = "Passwords must match!"

            elif password1.isalpha():
                error = "mix in some numbers with the password"

            elif Temp_user.objects.filter(email=email).exists():
                msg = ["""
                The account is already registered! Verify your email.
                <br /> Sometimes emails can take some to reach the destination.
                <br /> Please be patient! If this method fails repeatedly contact your mentor!!
                """]
                return message('signup error', msg, request)
            
            # main show starts from here:
            # ===========================
            else:
                token = addons.generate_url()
                tuser = Temp_user.objects.create(uname=uid, password=make_password(password1), email=email, token=token)
                receiver = [request.POST["email"]]
                
                # changing things in student/teacher table
                if Student.objects.filter(id=tuser.uname).exists():
                    user = Student.objects.update(is_registered=True)
                else:
                    user = Teacher.objects.update(is_registered=True)
                
                if addons.verification_mailto(receiver, token):                   
                    img = '<img src="' + addons.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
                    return render(request, 'accounts/resend.html', {'title':'email verification','case':'first_time', 'token':token, 'cute_image': img})
                else:
                    responce = ["ERROR! mail not sent"] 
                return message('signed up', responce, request)
            if error:
                return render(request, 'accounts/signup.html', {'title':'signup error', 'error':error})
        
        else: # request.method is "GET"
            return render(request, 'accounts/signup.html', {'title':'signup'})


def activate(request):
    title = "email_verification" # used to display as page title, nothing special!
    path = str(request.path)
    key = path.split("validate/", 1)[1]
    error = ""

    if Temp_user.objects.filter(token=key).exists():
        tuser = Temp_user.objects.get(token=key)
        
        if tuser.verify_time(timezone.now()): # checking whether the link is valid!
            # check if token is a reset token and do reset if yes
            # reset token starts with "reset"
            login = '"' + reverse('login') + '"'
            if 'reset' not in tuser.token:
                # Adding to user
                # getting the user's name and desig
                try:
                    stud = Student.objects.get(id=tuser.uname)
                    name = stud.name
                    desig = "s" # s for student
                except:
                    teach = Teacher.objects.get(id=tuser.uname)
                    name = teach.name
                    desig = "t" # t for teacher

                user = User.objects.create_user(username=tuser.uname, first_name=name, last_name=desig, password=tuser.password, email=tuser.email)
                user.password = tuser.password # Using this since django will re-hash the hashed password => Thus explicitly, re mentioning it!
                user.is_active = True
                user.save()
                
                # changing things in student/teacher table
                if Student.objects.filter(id=tuser.uname).exists():
                    user = Student.objects.get(id=tuser.uname)
                    user.is_verified=True
                    # creating FormFills
                    forms = FormFills.objects.create(student=tuser.uname)

                else:
                    user = Teacher.objects.get(id=tuser.uname)
                    user.is_verified=True
                user.save()
                
                msg = [
                "Welcome at NiT Student-Teacher Portal", 
                """Thanks for verifying your email! try <a href=""" + login + """>logging in! </a>"""
                ]
            
            else:
                user = User.objects.get(username=tuser.uname)
                user.set_password(tuser.password)
                user.save()
                msg = ["Walla! Your password has been reset!",
                """try <a href=""" + login + """>logging in! </a>"""
                ]
            
            # Deleting from Temp_user
            Temp_user.objects.filter(uname=tuser.uname).delete()

        else:
            img = '<img src="' + addons.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
            return render(request, 'accounts/resend.html', {'title':"email error",'case':'expire', 'token':tuser.token, 'cute_image': img})
    else:
        title = "404"
        msg = "This way does not lead to mars!"
    return message(title, msg, request)


def resend(request):
    if request.method == 'POST' and Temp_user.objects.filter(token=request.POST["token"]).exists():
        token = request.POST['token']
        tuser = Temp_user.objects.get(token=token)
        new_token = addons.generate_url()
        tuser.time = timezone.now()
        tuser.token = new_token
        tuser.save()
        receiver = [tuser.email]
        token = new_token
        if addons.varification_mailto(receiver, token):
            img = '<img src="' + addons.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
            return render(request, 'accounts/resend.html', {'title':'email varifiaction','case':'resend', 'token':new_token, 'cute_image': img})
        else:
            message = "ERROR! mail not sent"
    else:
        message = "Well, you have came a long way, to vain!"
    return message("404", message, request)


def reset(request):
    if request.method == "POST":
        error = ""  
        msg = ""    # error fails loudly
        flag = 0    # flag is used to fail silently
        id = request.POST['id'].strip()
        email = request.POST['email'].strip()
        password1 = request.POST['password1'].strip()
        password2 = request.POST['password2'].strip()

        if id is '' or email is '' or password1 is '' or password2 is '':
            error = "No fields can be kept blank here!"

        if not error and Student.objects.filter(id=id).exists() or Teacher.objects.filter(id=id).exists():
            if Student.objects.filter(id=id).exists():
                obj = Student.objects.get(id=id)
            else:
                obj = Teacher.objects.get(id=id)

            if not obj.is_registered:
                signup_url = reverse_lazy('signup')
                msg = ["Well, register first, even before you forget your account password!!",
                '<h5> <a href="'+str(signup_url)+'">Sign up </h5>']
            elif not obj.is_verified:
                msg = "First verify your account"
            elif password1 != password2:
                error = 'Password must match'
            elif len(password1) < 2:
                error = "Passwords must be atleast 8 characters!"
            elif password1.isalpha():
                error = "mix in some numbers with the password"
            elif not obj.email == email:
                flag = 1  
        else:
            error = "Well, we don't know you!"

        if not flag and not error and not msg:
            reset_token = "reset"+addons.generate_url()
            if Temp_user.objects.filter(uname=obj.id).exists():
                Temp_user.objects.filter(uname=obj.id).update(password=password1, token=reset_token, time=timezone.now())
            else:
                Temp_user.objects.create(uname=obj.id, password=password1, email=obj.email, token=reset_token, time=timezone.now())
            receiver = [obj.email]
            if addons.verification_mailto(receiver, reset_token):
                msg = ["If you entered correct Name, Id and your registered email id", 
                "expect to receive an email to reset password!",
                ]
            else:
                msg = ["Error sending mail... Try again.", "If problem persists, contact your HOD!"]
        else:
            msg = ["If you entered correct Name, Id and your registered email id", 
                "expect to receive an email to reset password!",
                ]

        if msg:
            print(1)
            return message("reset_message", msg, request)
        elif error:
            print(2)
            return render(request, 'accounts/reset.html', {'title':'reset-error', 'error':error})

    else:
        print(3)
        return render(request, 'accounts/reset.html', {"title":"reset password"})


def message(title, mesg, request):
    _ = []
    if type(mesg) != type(_):
        mesg = [mesg]
    img = '<img src="' + addons.get_cute_image() + '" height="200px" width="200px" alt="a cute animal image">'
    return render(request, 'accounts/message.html', {'title':title, 'messages':mesg, 'cute_img':img})

@login_required(login_url=reverse_lazy('login'))
def index(request):
    return render(request, 'accounts/index.html', {'title':'index'})
