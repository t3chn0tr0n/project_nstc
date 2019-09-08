import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import *
from .addons import (get_teach_details)
from students.models import Student


# TODO: Handle errors gracefully!
@login_required(login_url=reverse_lazy('login'))
def upload_student(request):
    if Student.objects.filter(id=request.user.username):
        title = "ERROR"
        error = ['Students cannot view this page!']
        return message(title, error, request)
    d = get_teach_details(request)
    
    if request.method == 'POST' and request.is_ajax():
        hod = Teacher.objects.get(id=request.user.username)
        if hod.is_hod:
            Is_lat = request.POST['Is_lat']
            if(Is_lat == 1):
                Is_lat = True
            else:
                Is_lat = False
            Stream = request.POST['Stream']
            if(Stream == "B-TECH"):
                Stream = 'B'
            elif(Stream == "M-TECH"):
                Stream = "M"
            else:
                Stream = "D"
            Batch = request.POST['Batch']
            arr = [str(i) for i in json.loads(request.POST['arr'])]
            dept = Teacher.objects.get(id=request.user.username).dept
            for i in arr:
                l = i.split(" ")
                ment = Teacher.objects.get(id=l[6])
                id = l[0].strip()
                ad = l[1].strip()
                n = l[2].strip().upper()
                m = l[3].strip().upper()
                s = l[4].strip().upper()
                e = l[5].strip().lower()
                # Possibility of errors: [return the id of error data] [Untracked Exception at CSV File]
                # 1. *** id exists (duplicate data) ***
                # 2. blank fields
                # 3. unique email
                # 4. Mentor does not exist
                # 5. Dept does not exist
                # 6. Stream does not exist
                if not id or not ad or not n or not m or not s or not e:
                    raise "Error: Blank Field"
                student.objects.create(id=id, admission_no=ad, name=n, middle_name=m, surname=s,
                                       mentor=ment, email=e, dept=dept, is_lateral=Is_lat, batch=Batch, stream=Stream)
        else:
            d['title'] = "Access Denied"
            error = ['</h3> <h2 class="text-danger">ACCESS DENIED!</h2>',
                     'ONLY HODS CAN UPLOAD STUDENT LIST!'
                     ]
            return render(request, 'message.html', d)

    # GET Request
    hod = Teacher.objects.get(id=request.user.username)
    if not hod.is_hod:
        d['title'] = "Access Denied"
        error = ['</h2> <h3 class="text-danger">ACCESS DENIED!</h3><h2>',
                 'ONLY HODS CAN ACCESS THIS PAGE!'
                 ]
        d['msg'] = error
        return render(request, 'teachers/message.html', d)
    else:
        d['title']= "Upload Student"
        return render(request, 'teachers/student_csv_upload.html', d)


@login_required(login_url=reverse_lazy('login'))
def student_search(request):
    if Student.objects.filter(id=request.user.username):
        title = "ERROR"
        error = ['Students cannot view this page!']
        return message(title, error, request)
    else:
        if request.method == "POST":
            pass
        d = get_teach_details(request)
        d['title'] = "Upload Student"
        return render(request, 'teachers/student_view.html', d)
        return render(request, 'teachers/search.html', d)


def princi_teacher_view(request):
    teacher = Teacher.objects.all()
    d = get_teach_details(request)
    d['teacher'] = teacher
    d['title'] =  "Manage HODs"
    return render(request, 'teachers/princi_teacher_view.html', d)


#TODO: only can be done by principal
def assign_hod(request):
    if request.method == "POST" and request.is_ajax():
        mentor_id=request.POST.get('mentor_id')
        new_obj = Teacher.objects.get(id=mentor_id)
        old_hod =  Teacher.objects.get(is_hod=True)
        new_obj.is_hod=True
        old_hod.is_hod=False
        new_obj.save()
        old_hod.save()
        return HttpResponse("CHANGES SAVED SUCCESSFULLY!")
    else:
        princi_teacher_view(request)


def mentees_list(request):
    teach = Teacher.objects.get(id=request.user.username)
    students = Student.objects.filter(mentor=teach)
    d = get_teach_details(request)
    if len(students) == 0:
        d['title'] = "Students List"
        d['msg'] = ["You have no student as mentees yet!"]
        return render(request, 'teachers/message.html', d)
    batches = []
    for x in students:
        if x.batch not in batches:
            batches.append(x.batch)
    d['mentees'] = students
    d['batches'] = batches
    return render(request, 'teachers/mentees.html', d)


def view_student(request, x, y, z):
    d = get_teach_details(request)
    id = x
    return render(request, 'teachers/mentees.html', d)


def manage_teacher(request):
    if Student.objects.filter(id=request.user.username):
        title = "ERROR"
        error = ['Students cannot view this page!']
        return message(title, error, request)
    d = get_teach_details(request)

    hod = Teacher.objects.get(id=request.user.username)
    if not hod.is_hod:
        title = "ERROR"
        error = ['Only HODs can access this page']
        return message(title, error, request)

    teachers = Teacher.objects.filter(dept=hod.dept)
    d['title'] = 'Manage Teachers'
    d['teacher'] = teachers
    return render(request, 'teachers/hod_teacher_view.html', d)