import csv
import json
import os

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from students.addons import (extra_curricular, get_general_details,
                             get_idcard_details, get_univ_details)
from students.models import Batch, Student

from .addons import get_teach_details
from .models import *


# TODO: Handle errors gracefully!
@login_required(login_url=reverse_lazy('login'))
def upload_student(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

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
            batch = request.POST['Batch']
            bat = Batch.objects.filter(id=batch)
            if bat is None:
                Batch.objects.create(
                    id=batch, batch=batch[3:7] + '-' + batch[7:])

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
                Student.objects.create(id=id, admission_no=ad, name=n, middle_name=m, surname=s,
                                       mentor=ment, email=e, dept=dept, is_lateral=Is_lat, batch=Batch, stream=Stream)
            return HttpResponse("Update Successful!!")
        else:
            d['title'] = "Access Denied"
            error = ['</h3> <h2 class="text-danger">ACCESS DENIED!</h2>',
                     'ONLY HODS CAN UPLOAD STUDENT LIST!'
                     ]
            return render(request, 'message.html', d)

    # GET Request
    hod = Teacher.objects.get(id=request.user.username)
    d = get_teach_details(request)
    if not hod.is_hod:
        d['title'] = "Access Denied"
        error = ['</h2> <h3 class="text-danger">ACCESS DENIED!</h3><h2>',
                 'ONLY HODS CAN ACCESS THIS PAGE!'
                 ]
        d['msg'] = error
        return render(request, 'teachers/message.html', d)
    else:
        d['title'] = "Upload Student"
        return render(request, 'teachers/student_csv_upload.html', d)


@login_required(login_url=reverse_lazy('login'))
def student_search(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    if request.method == "POST":
        pass
    else:
        ment = Teacher.objects.get(id=request.user.username)
        if ment.is_hod:
            rank = "HOD"
            is_hod = True
        else:
            rank = "Mentor"
            is_hod = False
        return render(request, 'teachers/search.html', {'dept': ment.dept, 'title': "Upload Student", "rank": rank, 'is_hod': is_hod})


@login_required(login_url=reverse_lazy('login'))
def princi_teacher_view(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    d = get_teach_details(request)

    teacher = Teacher.objects.all()
    d = get_teach_details(request)
    d['teacher'] = teacher
    d['title'] = "Manage HODs"
    return render(request, 'teachers/princi_teacher_view.html', d)


# TODO: only can be done by principal
@login_required(login_url=reverse_lazy('login'))
def assign_hod(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    if request.method == "POST" and request.is_ajax():
        mentor_id = request.POST.get('mentor_id')
        new_obj = Teacher.objects.get(id=mentor_id)
        old_hod = Teacher.objects.get(is_hod=True)
        new_obj.is_hod = True
        old_hod.is_hod = False
        new_obj.save()
        old_hod.save()
        return HttpResponse("CHANGES SAVED SUCCESSFULLY!")
    else:
        d = {'fof': True}
        return render(request, 'message.html', d)


@login_required(login_url=reverse_lazy('login'))
def mentees_list(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

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


@login_required(login_url=reverse_lazy('login'))
def view_student(request, x, y, z):
    if not Student.objects.filter(id=x):
        d = {'fof': True}
        return render(request, 'message.html', d)

    d = get_teach_details(request)
    student_id = x
    id_card = get_idcard_details(student_id)
    if id_card:
        d.update(id_card)
    univ_details = get_univ_details(student_id)
    gen_details = get_general_details(student_id)
    if gen_details and univ_details:
        d['gen_details'] = True
        d.update(gen_details)
        d.update(univ_details)
        d['dob'] = str(d['dob'])
    extra_curr_details = extra_curricular(student_id)
    if extra_curr_details:
        d['ext_acts'] = True
        d.update(extra_curr_details)

    d['gen_edit'] = True

    d['no_sem'] = False
    d['lat_sems'] = (1, 2)  # constant
    # call a function here that gives available sems
    d['available'] = [1, 2, 3, 4]
    d['not_available'] = [5, 6]
    d['invalid_sems'] = [7, 8]

    return render(request, 'teachers/student_view.html', d)


@login_required(login_url=reverse_lazy('login'))
def manage_teacher(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

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


# to view profile of hod, teacher, principal
@login_required(login_url=reverse_lazy('login'))
def profile(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    d = get_teach_details(request)

    teach = Teacher.objects.get(id=request.user.username)
    d['mob_no1'] = teach.phone_no_1
    d['mob_no2'] = teach.phone_no_2
    d['email'] = teach.email
    # print(len(teach.image)){% static 'teachers/img/profile.jpg'%}
    if teach.image is None:
        d['profile_pic'] = "blank"
    else:
        d['profile_pic'] = teach.image
    return render(request, 'teachers/profile.html', d)


@login_required(login_url=reverse_lazy('login'))
def upload_profile_pic(request):
    upload_file = request.FILES['profile_pic']
    teach = Teacher.objects.get(id=request.user.username)
    d = get_teach_details(request)
    # if teach.image != None:
    #     print(type(teach.image))
    #     #print(os.path.exists(teach.image[1:]))
    #     print(os.path.exists("media/"+upload_file.name))
    fs = FileSystemStorage()
    name = fs.save(upload_file.name, upload_file)
    url = fs.url(name)
    teach.image = url
    teach.save()
    return redirect(profile)


@login_required(login_url=reverse_lazy('login'))
def int_marks(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    d = get_teach_details(request)
    return render(request, 'teachers/int_marks.html', d)


@login_required(login_url=reverse_lazy('login'))
def change_profile(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    if request.method == 'POST' and request.is_ajax():
        email = request.POST['email']
        mob1 = request.POST['mob1']
        mob2 = request.POST['mob2']
        teach_id = request.POST['id']
        if (email != "" and mob1 != "" or mob2 != ""):
            if '@' not in email:
                return HttpResponse("Invalid Email!!")
            d1 = Teacher.objects.filter(id=teach_id).update(email=email)
            d2 = Teacher.objects.filter(id=teach_id).update(phone_no_1=mob1)
            d3 = Teacher.objects.filter(id=teach_id).update(phone_no_2=mob2)
            return HttpResponse("Update Successful!!")
    return HttpResponse("Something went worng!!!Please contact to your mentor as soon as possible.")


@login_required(login_url=reverse_lazy('login'))
def search_filter(request):
    if Student.objects.filter(id=request.user.username):
        d = {'fof': True}
        return render(request, 'message.html', d)

    if request.method == "POST":
        rslt = []
        srch = request.POST['srch'].upper()
        ment = Teacher.objects.get(id=request.user.username)

        if srch[0:4] == "NIT/":
            if ment.is_principal:
                student = Student.objects.all().filter(id__startswith=srch)
            elif ment.is_hod:
                student = Student.objects.filter(
                    dept=ment.dept).filter(id__startswith=srch)
            else:
                student = Student.objects.filter(
                    mentor=request.user.username).filter(id__startswith=srch)
            for i in student:
                # if(i.middle_name != "NULL"):
                #     l.append(i.name+" "+i.middle_name+" "+i.surname+"$")
                # else:
                #     l.append(i.name+" "+i.surname+"$")
                rslt.append(i.id + "$")
        else:
            if ment.is_principal:
                student = Student.objects.all().filter(name__startswith=srch)
            elif ment.is_hod:
                student = Student.objects.filter(
                    dept=ment.dept).filter(name__startswith=srch)
            else:
                student = Student.objects.filter(
                    mentor=request.user.username).filter(name__startswith=srch)
            for i in student:
                if(i.middle_name != "NULL"):
                    rslt.append(i.name + " " + i.middle_name +
                                " " + i.surname + "$")
                else:
                    rslt.append(i.name + " " + i.surname + "$")

    return HttpResponse(rslt[:10])
# download student and teacher


@login_required(login_url=reverse_lazy('login'))
def download_student(request):
    d = get_teach_details(request)
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        if request.POST.get('catagory') == 'Teacher':
            response['Content-Disposition'] = 'attachment; filename="teachers.csv"'
            writer = csv.writer(response)
            writer.writerow(['ID', 'FIRST NAME', 'MIDDLE NAME', 'LAST NAME',
                             'DEPARTMENT', 'EMAIL', 'PHONE NO 1', 'PHONE NO 2'])
            teach_obj = Teacher.objects.filter(dept=d['dept'])
            for i in teach_obj:
                nm = i.name.split(' ')
                if len(nm) == 2:
                    writer.writerow(
                        [i.id, nm[0], '', nm[1], i.dept, i.email, i.phone_no_1, i.phone_no_2, ])
                else:
                    writer.writerow(
                        [i.id, nm[0], nm[1], nm[2], i.dept, i.email, i.phone_no_1, i.phone_no_2, ])
        else:
            response['Content-Disposition'] = 'attachment; filename="students.csv"'
            writer = csv.writer(response)
            writer.writerow(['ID', 'FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'DEPARTMENT',
                             'UNIV_ROLL_NO', 'REGISTRATION_NO', 'ADMISSION_NO', 'BATCH', 'EMAIL'])
            student_obj = Student.objects.filter(dept=d['dept'])
            for i in student_obj:
                writer.writerow([i.id, i.name, i.middle_name, i.surname, i.dept,
                                 i.univ_roll_no, i.registration_no, i.admission_no, i.batch, i.email])

        return response
    return render(request, 'teachers/download_student.html', d)


@login_required(login_url=reverse_lazy('login'))
def manage_mentor(request):
    d = get_teach_details(request)
    batch = Batch.objects.all()
    mentor = Teacher.objects.filter(dept=d['dept'])
    d['batch'] = batch
    d['mentor'] = mentor
    return render(request, 'teachers/manage_mentor.html', d)


@login_required(login_url=reverse_lazy('login'))
def mentor_student_show(request):
    if request.method == 'POST' and request.is_ajax():
        std_id_str = ''
        # student_ids = [i for i in json.loads(request.POST['info'])]
        batch_id = request.POST['batch_id']
        mentor_id = request.POST['mentor_id']
        student = Student.objects.filter(
            mentor=mentor_id).filter(batch=batch_id)
        # print(student)
        for i in student:
            std_id_str = std_id_str + i.id + ','
        l = len(std_id_str)
        return HttpResponse(std_id_str[:l-1])
    return render(request, 'teachers/manage_mentor.html')


@login_required(login_url=reverse_lazy('login'))
def mentor_change(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            batch_id = request.POST['batch_id']
            mentor_id = request.POST['mentor_id']
            student_ids = [i for i in json.loads(request.POST['info'])]
            for i in student_ids:
                Student.objects.filter(id=i).update(mentor=mentor_id)
            return HttpResponse("Changes has been successfully saved!!")
        except:
            return HttpResponse("Error! Something is wrong. Please upload data carefully!!")
