import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import *
from .addons import get_teach_details
from students.models import Student
from students.addons import get_general_details, extra_curricular, get_univ_details, get_idcard_details

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
    d['available'] = [1, 2, 3, 4]  # call a function here that gives available sems
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
    return render(request, 'teachers/profile.html', d)


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
                    rslt.append(i.name + " " + i.middle_name + " " + i.surname + "$")
                else:
                    rslt.append(i.name + " " + i.surname + "$")

    return HttpResponse(rslt[:10])
