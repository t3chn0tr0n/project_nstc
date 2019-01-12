from builtins import ValueError

from . import addons
from .models import FormFills, Student
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import success
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from accounts.views import message
from students.addons import (
                                get_univ_details, 
                                form_fill_sem, 
                                is_prev_sems_filled, 
                                any_sem_yet
                            )
from students.models import Class10, Class12, FormFills
from subject_and_marks.models import SemMarks, Subjects
from teachers.models import Teacher

# Test Ground for new templates - Contains unchecked code - comment it out if it causes error
@login_required(login_url=reverse_lazy('login'))
def demo(request):
    return render(request, 'students/sem_marks.html', {'messg':True})


@login_required(login_url=reverse_lazy('login'))
def general_details(request):
    details = addons.get_idcard_details(request.user)
    if not details:
        error = ["Error getting student details"]

    if request.method == "POST":
        error = ""
        filled_forms = FormFills.objects.get(student=request.user.username)
        if filled_forms.is_gen_details_filled:
            error = ["Can't Overwrite existing data!"]
        else:
            stud = Student.objects.get(id=request.user.username)
            dob = request.POST['dob'].strip()
            blood_type = request.POST['blood_type'].strip()
            # HOUSE DETAILS
            guard = request.POST['guard'].strip()
            perm_add = request.POST['perm_add'].strip()
            loc_guard = request.POST['loc_guard'].strip()
            loc_add = request.POST['loc_add'].strip()
            # CONTACT NOs
            land_phone = request.POST['land_phone'].strip()
            g_mob_no = request.POST['g_mob_no'].strip()
            mob_no = request.POST['mob_no'].strip()
            # SCHOOL DETAILS
            # Class 10
            sc10_name = request.POST['sc10_name'].strip()
            sc10_med = request.POST['sc10_med'].strip()
            sc10_marks = request.POST['sc10_score'].strip()
            sc10_year = request.POST['sc10_year'].strip()
            sc10_add = request.POST['sc10_add'].strip()
            # Class 12
            sc12_name = request.POST['sc12_name'].strip()
            sc12_med = request.POST['sc12_med'].strip()
            sc12_marks = request.POST['sc12_score'].strip()
            sc12_year = request.POST['sc12_year'].strip()
            sc12_add = request.POST['sc12_add'].strip()
            # DIPLOMA SCORE
            if stud.is_lateral:
                dip_score = request.POST['dip_score'].strip()
            else:
                dip_score = -1

            if '' in [dob, blood_type, guard, perm_add, g_mob_no, mob_no, sc10_name, sc10_med, sc10_marks, sc10_year, sc10_add, sc12_name, sc12_med, sc12_marks, sc12_year, sc12_add, dip_score]:
                error = ["All Compulsory Fields must be filled!"]

            # land phone no verification
            try:
                land_phone = int(land_phone)
                if len(str(land_phone)) > 11:
                    error = ["Land phone number too long!"]
                elif len(str(land_phone)) == 8:
                    error = ["Please provide STD code for Land phone.",
                            "example: 03322222222"]
                elif len(str(land_phone)) < 8:
                    error = ["Land phone number too short!"]
            except ValueError:
                error = ["land phone number can't contain characters!"]

            # mobile no verification
            try:
                g_mob_no = int(g_mob_no)
                mob_no = int(mob_no)

                if len(str(mob_no)) != 10 or len(str(g_mob_no)) != 10:
                    error = ["Mobile Number must be equal to 10 digits!"]
            except ValueError:
                error = ["Mobile phone number can't contain characters!",
                        "Tip: No need for country code: (eg. +91 in India)"]
            try:
                if int(sc12_year) - int(sc10_year) < 2:
                    error = [
                        "How did you pass class 10 and 12 in less then 2 years? Magic??"]

                elif int(sc10_year) - int(dob.split('-')[0]) < 15:
                    error = [
                        "Your dob and class 10 passout year doesn't add up!",
                        'Got multiple promotions in middle school? Contact your Mentor!']

                elif float(sc10_marks) > 100 or float(sc12_marks) > 100:
                    error = [
                        "How did you get more than 100 in boards? Good handwriting?"]

                elif float(sc10_marks) < 30 or float(sc12_marks) < 30:
                    error = [
                        "Well, your board marks are fishy! contact Mentor or reCheck!"]
            except:
                error = ["Well year, marks, etc cannot be alphabets"]

            if not error:
                stud = Student.object.get(id=request.user.username)
                details = Details.object.create(card_no=request.user.username, dob=dob, blood_grp=blood_type, guardian=guard, perm_add=perm_add,
                                                loc_guardian=loc_guard, loc_add=loc_add, land_phone=land_phone, guardian_mobile_no=g_mob_no, mobile_no=mob_no)
                if stud.is_lateral:
                    details.diploma_score = dip_score
                    details.save()
                sc10 = Class10.objects.create(student=request.user.username, medium=sc10_med,
                                            school_name=sc10_name, passing_year=sc10_year, school_address=sc10_add, score=sc10_marks)
                sc12 = Class12.objects.create(student=request.user.username, medium=sc12_med,
                                            school_name=sc12_name, passing_year=sc12_year, school_address=sc12_add, score=sc12_marks)
                forms = FormFills.objects.get(student=request.user.username)
                forms.is_gen_details_filled = True
                forms.save()
                sc10.save()
                sc12.save()
                d = {
                    'title': "Form saved!",
                    'success': True,
                }
            else:
                d = {
                    'title': "ERROR",
                    'messages': error,
                    'error': True
                }
            return render(request, 'message.html', d)

    # for GET request
    else:
        # if a teacher comes here, well show the way out to them!
        if Teacher.objects.filter(id=request.user.username):
            title = "404"
            msg = "This way leads nowhere for you!"
            return message(title, msg, request)

        filled_forms = FormFills.objects.get(student=request.user.username)
        stud = Student.objects.get(id=request.user.username)
        details = {**addons.get_idcard_details(
            request.user.username), **addons.get_univ_details(request.user.username)}
        details['title'] = 'Student Details'
        details['is_lateral'] = stud.is_lateral
        if filled_forms.is_gen_details_filled:
            details['filled'] = True
        else:
            details['filled'] = False
        return render(request, 'students/details.html/', details)


@login_required(login_url=reverse_lazy('login'))
def univ_details(request):
    if request.method == "POST":
        error = ""
        admin_no = request.POST['admin_no'].strip()
        reg_no = request.POST['reg_no'].strip()

        if admin_no is '' or reg_no is '':
            error = [
                "Who has blank Admission and/or Registration numbers?"]
        try:
            admin_no = int(admin_no)
            reg_no = int(reg_no)
        except ValueError:
            error = ["Enter only Whole Numbers"]

        user = request.user.username
        try:
            stud = Student.objects.get(id=user)
        except:
            error = ["ERROR finding the student"]

        # If already filled, fail loudly!
        if stud.admission_no or stud.registration_no:
            error = ["Can't Overwrite existing data!"]

        if not error:
            stud.admission_no = admin_no
            stud.registration_no = reg_no
            stud.save()
            forms = FormFills.objects.get(student=request.user.username)
            forms.is_univ_details_filled = True
            forms.save()
            return render(request, 'message.html', {'title': 'Saved!', 'success': True})
        return render(request, 'message.html', {'title': 'ERROR', 'error': True,  'messages': error})

    else:
        # if a teacher comes here, well show the way out to them!
        if Teacher.objects.filter(id=request.user.username):
            title = "404"
            msg = "This way leads nowhere for you!"
            return message(title, msg, request)
        d = {
            'title': '404 Error',
            'fof': True
        }
        return render(request, 'message.html', d)


@login_required(login_url=reverse_lazy('login'))
def sem_marks(request, sem):
    if Teacher.objects.filter(id=request.user.username).exists():
        error = ['Teachers cannot view this page!', 'Teachers don\'t give sems anymore! :D']
        return render(request, 'message.html', {'title': 'ERROR',  'messages': error})   
    
    forms = FormFills.objects.get(student=Student.objects.get(id=request.user.username).id)

    if request.method == "POST":
        user = request.user.username
        error = ''
        filled_sems = forms.sem_fills_easy() 
        if not forms.is_gen_details_filled and not forms.is_univ_details_filled:
            error = ['Please first fill General Details and University Details (in General Details page)']
        elif not is_prev_sems_filled:
            error = ["Fill previous semester marks first", "Semester {} is not filled".format(is_prev_sems_filled)]
        elif filled_sems[sem]:
            error = ['Your data is already saved! Cannot re submit!']
        elif not any_sem_yet:
            error = ['No semester has been taken yet!']
        
        try:
            sem = int(sem)
        except:
            error = ["Internal Server Error!"]
        try:
            stud = Student.objects.get(id=user)
        except:
            error = ["Problem in finding the student"]
        # part - 1: Details
        try:
            details = {
                        'student_id': stud.id,
                        'sem_no': int(sem),
                        'max_score_in_class': float(request.POST['highest_score'].strip()),
                        'attendance': int(request.POST['attendance'].strip()),
                        'no_of_tutorial_class': int(request.POST['tut_class'].strip()),
                        'no_of_fschool_class': int(request.POST['f_school'].strip()),
                        'scl_activities': request.POST['slc'].strip(),
                        'disciplinary_action': request.POST['disc_action'].strip(),
                        'sgpa': float(request.POST['sgpa'].strip()),
                    }
        except:
            error = ["Invalid Input. Try again!"]

        # part - 2: Marks
        subs = Subjects.objects.get(batch=stud.batch, dept=stud.dept, stream=stud.stream, sem=sem)
        subs = subs.get_subjects_as_dict() # a dictionary of all subjects
        marks = {}
        try:
            if not error:
                for x,y in subs.items():
                    if y in request.POST:
                        marks[x]= y
                        marks[x+'_marks'] = request.POST[y]
                    else:
                        marks[x] = None
                        marks[x+'_internal'] = None
                        marks[x+'_marks'] = None                
                # if student data exists due to teacher uploading internal marks -- update
                # TODO: CHECK IF THIS WORKS!
                if SemMarks.objects.filter(student_id=stud.id, sem=sem).exists():
                    stud_marks = SemMarks.objects.get(student_id=stud.id, sem=sem)
                    stud_marks.update(**details, **marks)                
                else: # create new entry
                    SemMarks.objects.create(**details, **marks)
                    form_fill_sem(stud.id, sem)                    
        except:
            error = ["Internal Server Error!", 
                            "Cause: Student not found or database integrity errors"] 

        if error:
            return render(request, 'message.html', {'title': 'ERROR', 'error': True,  'messages': error})
        else:
            msg = ["SUCCESS", "Your data has been saved!"]
            return render(request, 'message.html', {'title': 'SUCCESS',  'messages': msg})

    else:  # GET request
        details = addons.get_sem_details(request.user.username, sem)
        if details == -1:
            return render(request, 'message.html', {'title': 'ERROR', 'error': True,  'messages': ['Subject list for the semester not found!']})
        if not forms.is_gen_details_filled and not forms.is_univ_details_filled:
            details['messg']: True
        return render(request, 'students/sem_marks.html', details)


@login_required(login_url=reverse_lazy('login'))
def extracurricular_activities(request):
    pass