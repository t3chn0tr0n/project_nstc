from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import *
from students.models import Student


# TODO: Handle errors gracefully!
@login_required(login_url=reverse_lazy('login'))
def upload_student(request):
    if Student.objects.filter(id=request.user.username):
        title = "404"
        error = ['Students cannot view this page!']
        return message(title, error, request)
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
            title = "Access Denied"
            error = ['</h3> <h2 class="text-danger">ACCESS DENIED!</h2>',
                     'ONLY HODS CAN UPLOAD STUDENT LIST!'
                     ]
            return message(title, error, request)

    # GET Request
    hod = Teacher.objects.get(id=request.user.username)
    if hod.is_hod == "true":
        title = "Access Denied"
        error = ['</h2> <h3 class="text-danger">ACCESS DENIED!</h3><h2>',
                 'ONLY HODS CAN ACCESS THIS PAGE!'
                 ]
        return message(title, error, request)
    mentor_id = request.user.username
    ment = Teacher.objects.get(id=mentor_id)
    if ment.is_hod:
        rank = "HOD"
        is_hod = True
    else:
        rank = "Mentor"
        is_hod = False
    return render(request, 'teachers/student_csv_upload.html', {'dept': hod.dept, 'title': "Upload Student", "rank": rank, 'is_hod': is_hod})
