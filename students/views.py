import json
from builtins import ValueError

from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import success
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.urls import reverse_lazy

from accounts.views import message
from students.addons import (any_sem_yet, comma_separated_add,
                             extra_curricular, form_fill_sem,
                             get_general_details, get_idcard_details,
                             get_page_details, get_sem_details,
                             get_univ_details, is_prev_sems_filled,
                             yes_to_true)
from subject_and_marks.models import SemMarks, Subjects
from teachers.models import Teacher

from .models import (Class10, Class12, Contributions, Counselings, Details,
                     ExtracurricularActivity, FormFills, SeminarsWorkshops,
                     Student)


@login_required(login_url=reverse_lazy('login'))
def general_details(request):
    # if a teacher comes here, well show the way out to them!
    if Teacher.objects.filter(id=request.user.username):
        title = "404"
        error = ['Teachers cannot view this page!']
        return message(title, error, request)

    details = get_idcard_details(request.user.username)
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
            if len(land_phone) != 0:
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
            else:
                land_phone = "N/A"

            if loc_guard in (' ', ''):
                loc_guard = "N/A"
            if loc_add in (' ', ''):
                loc_add = "N/A"

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
                stud = Student.objects.get(id=request.user.username)
                details = Details.objects.create(card_no=request.user.username, dob=dob, blood_grp=blood_type, guardian=guard, perm_add=perm_add,
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
        filled_forms = FormFills.objects.get(student=request.user.username)
        stud = Student.objects.get(id=request.user.username)
        details = {
            **get_idcard_details(request.user.username),
            **get_univ_details(request.user.username),
            **get_general_details(request.user.username),
        }
        details['title'] = 'Student Details'
        details['is_lateral'] = stud.is_lateral
        if filled_forms.is_gen_details_filled:
            details['filled'] = True
        else:
            details['filled'] = False
        return render(request, 'students/details.html/', details)


@login_required(login_url=reverse_lazy('login'))
def univ_details(request):
    # if a teacher comes here, well raise a 404!
    if Teacher.objects.filter(id=request.user.username):
        return render(request, 'message.html', {'title': '404', 'error': True, 'fof': True})

    if request.method == "POST":
        error = ''
        admin_no = request.POST['admin_no'].strip()
        reg_no = request.POST['reg_no'].strip()

        if admin_no is '' or reg_no is '':
            error = ["Who has blank Admission and/or Registration numbers?"]
        try:
            admin_no = int(admin_no)
            reg_no = int(reg_no)
        except ValueError:
            error = ["Enter only Whole Numbers"]

        user = request.user.username
        try:
            stud = Student.objects.get(id=user)
        except:
            error = ["Student not found!"]

        # If already filled, fail loudly!
        if stud.univ_roll_no or stud.registration_no:
            error = ["You have already filled the university details!"]

        if not error:
            stud.univ_roll_no = admin_no
            stud.registration_no = reg_no
            stud.save()
            forms = FormFills.objects.get(student=request.user.username)
            forms.is_univ_details_filled = True
            forms.save()
            return render(request, 'message.html', {'title': 'Saved!', 'success': True})
        return render(request, 'message.html', {'title': 'ERROR', 'error': True,  'messages': error})

    else:  # if GET request
        return render(request, 'message.html', {'title': '404', 'error': True, 'fof': True})


@login_required(login_url=reverse_lazy('login'))
def sem_marks(request, sem):
    if Teacher.objects.filter(id=request.user.username):
        error = ['Teachers cannot view this page!',
                 'Teachers don\'t give sems anymore! :D']
        return render(request, 'message.html', {'title': 'ERROR',  'messages': error})

    forms = FormFills.objects.get(
        student=Student.objects.get(id=request.user.username).id)

    if request.method == "POST":
        user = request.user.username
        error = ''
        filled_sems = forms.sem_fills_easy()
        if not forms.is_gen_details_filled and not forms.is_univ_details_filled:
            error = [
                'Please first fill General Details and University Details (in General Details page)']
        elif not is_prev_sems_filled:
            error = ["Fill previous semester marks first",
                     "Semester {} is not filled".format(is_prev_sems_filled)]
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
        subs = Subjects.objects.get(
            batch=stud.batch, dept=stud.dept, stream=stud.stream, sem=sem)
        subs = subs.get_subjects_as_dict()  # a dictionary of all subjects
        marks = {}
        try:
            if not error:
                for x, y in subs.items():
                    if y in request.POST:
                        marks[x] = y
                        marks[x+'_marks'] = request.POST[y]
                    else:
                        marks[x] = None
                        marks[x+'_internal'] = None
                        marks[x+'_marks'] = None
                # if student data exists due to teacher uploading internal marks -- update
                # TODO: CHECK IF THIS WORKS!
                if SemMarks.objects.filter(student_id=stud.id, sem=sem).exists():
                    stud_marks = SemMarks.objects.get(
                        student_id=stud.id, sem=sem)
                    stud_marks.update(**details, **marks)
                else:  # create new entry
                    SemMarks.objects.create(**details, **marks)
                    form_fill_sem(stud.id, sem)
        except:
            error = ["Something went wrong. Please try again!"]

        if error:
            return render(request, 'message.html', {'title': 'ERROR', 'error': True,  'messages': error})
        else:
            msg = ["SUCCESS", "Your data has been saved!"]
            return render(request, 'message.html', {'title': 'SUCCESS',  'messages': msg})

    else:  # GET request
        student = Student.objects.get(id=request.user.username)
        if student.is_lateral and sem in (1, 2, '1', '2'):
            d = {
                'title': 'ERROR',
                'messages': ['You are a lateral student, remember?']
            }
            return render(request, 'message.html', d)

        details = get_sem_details(request.user.username, sem)
        if details == -1:
            return render(request, 'message.html', {'title': 'ERROR', 'error': True,  'messages': ['Subject list for the semester not found!']})
        if not forms.is_gen_details_filled and not forms.is_univ_details_filled:
            details['messg']: True
        details['title'] = 'Sem {} Marks'.format(sem)
        return render(request, 'students/sem_marks.html', details)


@login_required(login_url=reverse_lazy('login'))
def extracurricular_activities(request):
    if request.method == "GET" and Student.objects.filter(id=request.user.username).exists():
        return render(request, 'students/extracurricular_activity.html', extra_curricular(request.user.username))
    else:
        return render(request, 'message.html', {'title': '404', 'fof': True})


# Form 2
@login_required(login_url=reverse_lazy('login'))
def ea_form1(request):
    if request.method != "POST" and Teacher.objects.filter(id=request.user.username).exists():
        return render(request, 'message.html', {'title': '404',  'fof': True})

    sftskl_condt = request.POST['sftskl_condt'].strip()
    sftskl_attnd = request.POST['sftskl_attnd'].strip()
    apti_condt = request.POST['apti_condt'].strip()
    apti_attnd = request.POST['apti_attnd'].strip()
    mck_intrvw = request.POST['mck_intrvw'].strip()
    iv1_date = request.POST['iv1_date'].strip()
    iv1_place = request.POST['iv1_place'].strip()
    iv2_date = request.POST['iv2_date'].strip()
    iv2_place = request.POST['iv2_place'].strip()
    onln_tst = request.POST['onln_tst'].strip()
    gate = request.POST['gate'].strip()
    cat = request.POST['cat'].strip()

    msg = ""

    if ExtracurricularActivity.objects.filter(student=request.user.username).exists():
        ea = ExtracurricularActivity.objects.get(student=request.user.username)

        if not ea.soft_skill_conduct and not ea.soft_skill_attend and sftskl_condt and sftskl_attnd and sftskl_condt >= sftskl_attnd:
            ea.soft_skill_conduct = sftskl_condt
            ea.soft_skill_attend = sftskl_attnd
            ea.save()
        else:
            msg = True

        if not ea.aptitude_conduct and not ea.aptitude_attend and apti_condt and apti_attnd and apti_condt >= apti_attnd:
            ea.aptitude_conduct = sftskl_condt
            ea.aptitude_attend = sftskl_attnd
            ea.save()
        else:
            msg = True

        if not ea.mock_interview and mck_intrvw == 'yes':
            ea.mock_interview = True
            ea.save()
        else:
            msg = True

        if not ea.industry_visit_1 and not ea.industry_visit_1_date and iv1_date and iv1_place:
            ea.industry_visit_1 = iv1_place
            ea.industry_visit_1_date = iv1_date
            ea.save()
        else:
            msg = True

        if not ea.industry_visit_2 and not ea.industry_visit_2_date and iv2_date and iv2_place:
            ea.industry_visit_2 = iv2_place
            ea.industry_visit_2_date = iv2_date
            ea.save()
        else:
            msg = True

        if not ea.online_test and onln_tst == 'yes':
            ea.online_test = True
            ea.save()
        else:
            msg = True

        if not ea.gate_exam and gate == 'yes':
            ea.gate_exam = True
            ea.save()
        else:
            msg = True

        if not ea.cat_exam and cat == 'yes':
            ea.cat_exam = True
            ea.save()
        else:
            msg = True
    else:
        if not sftskl_condt or not sftskl_attnd:
            sftskl_condt = 0
            sftskl_attnd = 0
        if not apti_condt or not apti_attnd:
            apti_condt = 0
            apti_attnd = 0
        mck_intrvw = yes_to_true(mck_intrvw)
        gate = yes_to_true(gate)
        cat = yes_to_true(cat)
        ExtracurricularActivity.objects.create(student=request.user.username, soft_skill_conduct=sftskl_condt, soft_skill_attend=sftskl_attnd, aptitude_conduct=apti_condt, aptitude_attend=apti_attnd,
                                               mock_interview=mck_intrvw, industry_visit_1=iv1_place, industry_visit_1_date=iv1_date, industry_visit_2=iv2_place, industry_visit_2_date=iv2_date, online_test=onln_tst, gate_exam=gate, cat_exam=cat)
    return_msg = """ <h4 class="text-success"> SUCCESS </h4>
                        You data has been Saved!"""
    if msg:
        return_msg += """<span class="text-muted small" Few entries were omitted! </span>"""
    return HttpResponse(return_msg)


# Form 1
@login_required(login_url=reverse_lazy('login'))
def ea_form2(request):
    if request.method != "POST" and Teacher.objects.filter(id=request.user.username).exists():
        return render(request, 'message.html', {'title': '404',  'fof': True})

    swrswti_puja = request.POST['swrswti_puja'].strip()
    vswkrma_puja = request.POST['vswkrma_puja'].strip()
    contribs_made = request.POST['contribs'].strip()
    ann_mag_pap_pub = request.POST['ann_mag_pap_pub'].strip()
    ann_mag_evnts = request.POST['ann_mag_evnts'].strip()
    wall_mag_evnts = request.POST['wall_mag_evnts'].strip()
    wall_mag_pap_pub = request.POST['wall_mag_pap_pub'].strip()
    papers_pub = request.POST['papers_pub'].strip()
    tech_contst = request.POST['tech_contst'].strip()
    awrds = request.POST['awrds'].strip()

    if ExtracurricularActivity.objects.filter(student=request.user.username).exists():
        ec_obj = ExtracurricularActivity.objects.get(
            student=request.user.username)
        if swrswti_puja == "true":
            ec_obj.saraswati_puja = True
        if vswkrma_puja == "true":
            ec_obj.vishwakarma_puja = True
        ec_obj.save()
    else:
        swrswti_puja = yes_to_true(swrswti_puja)
        vswkrma_puja = yes_to_true(vswkrma_puja)
        ExtracurricularActivity.objects.create(
            student=request.user.username, saraswati_puja=swrswti_puja, vishwakarma_puja=vswkrma_puja)

    if Contributions.objects.filter(student=request.user.username).exists():
        contribs = Contributions.objects.get(student=request.user.username)
    else:
        contribs = Contributions.objects.create(student=request.user.username)

    contribs.contributions = comma_separated_add(
        contribs.contributions, contribs_made)
    contribs.annual_magazine_paper = comma_separated_add(
        contribs.annual_magazine_paper, ann_mag_pap_pub)
    contribs.wall_magazine_event = comma_separated_add(
        contribs.wall_magazine_event, ann_mag_evnts)
    contribs.wall_magazine_paper = comma_separated_add(
        contribs.wall_magazine_paper, wall_mag_pap_pub)
    contribs.wall_magazine_event = comma_separated_add(
        contribs.wall_magazine_event, wall_mag_evnts)
    contribs.paper_publication = comma_separated_add(
        contribs.paper_publication, papers_pub)
    contribs.technical_contests = comma_separated_add(
        contribs.technical_contests, tech_contst)
    contribs.technical_academic_awards = comma_separated_add(
        contribs.technical_academic_awards, awrds)
    contribs.save()

    msg = """ <h4 class="text-success"> SUCCESS </h4>
            You data has been Saved!"""
    return HttpResponse(msg)


# Seminars/Workshops Attended
@login_required(login_url=reverse_lazy('login'))
def ea_form3(request):
    if request.method != "POST" and Teacher.objects.filter(id=request.user.username).exists():
        return render(request, 'message.html', {'title': '404',  'fof': True})

    names = request.POST.getlist('names[]')
    dates = request.POST.getlist('dates[]')
    orgs = request.POST.getlist('orgs[]')

    error = ""
    blank = ""
    duplicate = ""

    if (len(names) != len(dates)) or (len(dates) != len(orgs)) or (len(orgs) != len(names)):
        error = "Internal Server Error!"

    attendee = request.user.username
    for i in range(len(names)):
        # skip if any field is blank
        if (names[i] in [' ', None]) or (dates[i]in [' ', None]) or (orgs[i]in [' ', None]):
            blank = "Blank fields were omitted! "
            continue

        # check if addition willcause redundancy
        elif SeminarsWorkshops.objects.filter(attendee=attendee, name=names[i], date=dates[i], organiser=orgs[i]).exists():
            duplicate = "Duplicate entries were omitted!"
            continue

        else:
            SeminarsWorkshops.objects.create(
                attendee=attendee, name=names[i], date=dates[i], organiser=orgs[i])

    msg = """ <h4 class="text-success"> SUCCESS </h4>
            You data has been Saved! <br /> Refresh page to view changes <span class="text-secondary small">""" + blank + "<br />" + duplicate + "</span>"
    return HttpResponse(msg)


# Counseling With Comments
@login_required(login_url=reverse_lazy('login'))
def ea_form4(request):
    if request.method != "POST" and Teacher.objects.filter(id=request.user.username).exists():
        return render(request, 'message.html', {'title': '404',  'fof': True})

    topics = request.POST.getlist('topics[]')
    dates = request.POST.getlist('dates[]')

    error = ""
    blank = ""
    duplicate = ""

    if (len(topics) != len(dates)):
        error = "Internal Server Error!"

    attendee = request.user.username
    for i in range(len(topics)):
        # skip if any field is blank
        if (topics[i] in [' ', None]) or (dates[i]in [' ', None]):
            blank = "Blank fields were omitted!"
            continue

        # check if addition willcause redundancy
        elif Counselings.objects.filter(student=attendee, topic=topics[i], date=dates[i]).exists():
            duplicate = "Duplicate entries were omitted!"
            continue

        else:
            Counselings.objects.create(
                student=attendee, topic=topics[i], date=dates[i])

    msg = """ <h4 class="text-success"> SUCCESS </h4>
            You data has been Saved! <br /> Refresh page to view changes <span class="text-secondary small">""" + blank + "<br />" + duplicate + "</span>"
    return HttpResponse(msg)


@login_required(login_url=reverse_lazy('login'))
def change_phone(request):
    # if a teacher comes here, well show the way out to them!
    if Teacher.objects.filter(id=request.user.username):
        title = "Error"
        error = ['Teachers have nothing to do with this page!']
        return message(title, error, request)

    if request.method == 'POST' and request.is_ajax():
        mob_no = request.POST['mob_no'].strip()
        mob_len = len(mob_no)
        password = request.POST['password']
        user = auth.authenticate(
            username=request.user.username, password=password)
        try:
            mob_no = int(mob_no)
            if user and mob_len == 10:
                d = Details.objects.filter(
                    card_no=request.user.username).update(mobile_no=mob_no)
            else:
                if(mob_len != 10):
                    return HttpResponse("Mobile no is not valid!!")
                else:
                    return HttpResponse("Password is invalid!!")
        except ValueError:
            return HttpResponse("Mobile no is not valid!!")
    return HttpResponse("1")


@login_required(login_url=reverse_lazy('login'))
def profile(request):
    details = get_page_details(request.user.username)
    details.update(get_idcard_details(request.user.username))
    details.update(get_univ_details(request.user.username))
    details['email'] = Student.objects.get(id=request.user.username).email
    try:
        details['mob_no'] = Details.objects.get(
            card_no=request.user.username).mobile_no
    except:
        details['mob_no'] = " "
    return render(request, 'students/student_profile.html', details)


def change_email(request):
    if Teacher.objects.filter(id=request.user.username):
        title = "Error"
        error = ['Teachers have nothing to do with this page!']
        return message(title, error, request)

    if request.method == 'POST' and request.is_ajax():
        email = request.POST['email'].strip()
        email_len = len(email)
        password = request.POST['password']
        card_no = request.POST['card_no']
        user = auth.authenticate(
            username=request.user.username, password=password)
        try:
            if user:
                if '@' in email and ('.' in email.split('@')[1]):
                    d = Student.objects.filter(id=card_no).update(email=email)
                else:
                    return HttpResponse("Email is invalid!!!Make sure that your Email Id is correct otherwise you will not receive any Email from the collage.")
            else:
                return HttpResponse("Invalid password!!!")
        except ValueError:
            return HttpResponse("Failed to update email!!!Please contact to your mentor as soon as possible.")
    return HttpResponse("1")


def certificate(request):
    pass


def contact_mentor(request):
    if Teacher.objects.filter(id=request.user.username):
        title = "Error"
        error = ['Teachers have nothing to do with this page!']
        return message(title, error, request)
    stud = Student.objects.get(id=request.user.username)
    teach = Teacher.objects.get(id='NIT/01/JYP')
    d = {
        'mname': teach.name,
        'memail': teach.email,
        'mno1': teach.phone_no_1,
        'mno2': teach.phone_no_2,
        'fixed_footer': True,
        'title': 'Contact Mentor'
    }
    return render(request, 'students/contactMentor.html', d)


def upload_documents(request):
    if Teacher.objects.filter(id=request.user.username):
        title = "Error"
        error = ['Teachers have nothing to do with this page!']
        return message(title, error, request)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='/documents')
        print(fs)
        filename = fs.save(myfile.name, myfile)
        print(filename)
        # uploaded_file_url = fs.url(filename)
    return render(request, 'students/upload_documents.html')
