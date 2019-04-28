from builtins import object

from .models import (Class10, Class12, Contributions, Details, Counselings,
                     ExtracurricularActivity, FormFills, SeminarsWorkshops, Student)

import datetime
from subject_and_marks.models import SemMarks, Subjects
from teachers.models import Teacher


def get_idcard_details(id):
    try:
        stud = Student.objects.get(id=id)
        details = {
            'name': stud.name + stud.middle_name + stud.surname,
            'id': stud.id,
            'card_no': stud.id,
            'roll_no': stud.univ_roll_no,
            'email': stud.email,
            'dept': stud.dept,
            'mentor': stud.mentor.name,
            'nav_sems': sem_for_nav_bar(id)
        }
        if stud.stream == 'B':
            details['stream'] = "B.Tech"
        elif stud.stream == 'M':
            details['stream'] = "M.Tech"
        else:
            details['stream'] = "Diploma"
        if stud.is_lateral:
            details['is_diploma'] = True
        return details
    except:
        return False


def get_general_details(id):
    stud = Student.objects.get(id=id)
    filled_forms = FormFills.objects.get(student=id)
    if filled_forms.is_gen_details_filled:
        data = Details.objects.get(card_no=id)
        class10 = Class10.objects.get(student=id)
        class12 = Class12.objects.get(student=id)
        details = {
            'dob': data.dob,
            'blood_type': data.blood_grp,
            'guard': data.guardian,
            'perm_add': data.perm_add,
            'loc_guard': data.loc_guardian,
            'loc_add': data.loc_add,
            'land_phone': data.land_phone,
            'g_mob_no': data.guardian_mobile_no,
            'mob_no': data.mobile_no,
            'sc10_med': class10.medium,
            'sc10_name': class10.school_name,
            'sc10_year': class10.passing_year,
            'sc10_add': class10.school_address,
            'sc10_score': class10.score,
            'sc12_med': class12.medium,
            'sc12_name': class12.school_name,
            'sc12_year': class12.passing_year,
            'sc12_add': class12.school_address,
            'sc12_score': class12.score,
            'nav_sems': sem_for_nav_bar(id)
        }
        if stud.is_lateral:
            details['dip_score'] = data.diploma_score
    return details


def get_univ_details(id):
    stud = Student.objects.get(id=id)
    filled_forms = FormFills.objects.get(student=id)
    if filled_forms.is_univ_details_filled:
        details = {
            'admin_no': stud.univ_roll_no,
            'reg_no': stud.registration_no
        }
        return details
    else:
        return {}


def current_sem(id):
    stud = Student.objects.get(id=id)
    batch = stud.batch
    year = int(batch[3:7])
    date = datetime.datetime.now()
    current_year = int(date.year)
    current_month = int(date.month)
    dif = current_year - year
    if dif == 0:
        current_sem = 1
    elif dif == 1:
        if current_month >= 7:
            current_sem = 1
        else:
            current_sem = 2
    elif dif == 2:
        if current_month >= 7:
            current_sem = 4
        else:
            current_sem = 3
    elif dif == 3:
        if current_month >= 7:
            current_sem = 6
        else:
            current_sem = 5
    else:
        if current_month >= 7:
            current_sem = 8
        else:
            current_sem = 7
    return current_sem


def get_sem_details(id, sem):
    class Subject():
        def __init__(self, n, sub, int_marks='', marks='', lab=''):
            self.name = sub
            self.internal = int_marks
            self.marks = marks
            self.lab = lab
            self.slno = n

    try:
        stud = Student.objects.get(id=id)
        filled_forms = FormFills.objects.get(student=id)
        is_sem_filled = filled_forms.sem_fills_easy()
        sem_details = SemMarks.objects.get(student_id=id, sem_no=int(sem))
        no_details = False
    except:
        no_details = True
    error = False
    if not no_details and is_sem_filled[sem]:
        all_subs = []
        sems_marks = sem_details.sems()
        for x in range(1, 12):
            if sems_marks[str(x)][0] == None:
                pass
            else:
                x = str(x)
                if int(x) > 6:
                    all_subs.append(
                        Subject(('L' + str(int(x)-6)), sems_marks[x][0], sems_marks[x][1], sems_marks[x][2]))
                else:
                    all_subs.append(
                        Subject('T' + str(x), sems_marks[x][0], sems_marks[x][1], sems_marks[x][2]))

        details = {
            'is_filled': True,
            'highest_score': sem_details.max_score_in_class,
            'tut_class': sem_details.no_of_tutorial_class,
            'attendance': sem_details.attendance,
            'disc_action': sem_details.disciplinary_action,
            'f_school': sem_details.no_of_fschool_class,
            'slc': sem_details.scl_activities,
            'sgpa': sem_details.sgpa,
        }
    else:
        try:
            subs = Subjects.objects.get(
                batch=stud.batch, dept=stud.dept, stream=stud.stream, sem=sem)
            subs = subs.all_subs()
            all_subs = []
            for x in range(1, len(subs)+1):
                if x > 6:
                    all_subs.append(Subject(('L' + str(x-6)), subs[str(x)]))
                else:
                    all_subs.append(Subject(('T' + str(x)), subs[str(x)]))
            details = {
                'not_found': True
            }
        except:
            error = True
    if not error:
        details['all_subs'] = all_subs
        if stud.is_lateral:
            details['lat'] = True
        else:
            details['lat'] = False
        # Sem management
        details['curr_sem'] = sem
        sem = current_sem(id)
        details['available'] = [str(x) for x in range(1, int(sem)+1)]
        if stud.stream == "B":
            details['not_available'] = [str(x) for x in range(int(sem)+1, 9)]
        elif stud.stream == "D":
            details['not_available'] = [str(x) for x in range(int(sem)+1, 7)]
        elif stud.stream == "M":
            details['not_available'] = [str(x) for x in range(int(sem)+1, 5)]
        details['nav_sems'] = sem_for_nav_bar(id)
        return details
    else:
        return -1


def form_fill_sem(id, sem):
    forms = FormFills.objects.get(student=Student.objects.get(id=id))
    if sem == '1':
        forms.is_sem1_filled = True
    elif sem == '2':
        forms.is_sem2_filled = True
    elif sem == '3':
        forms.is_sem3_filled = True
    elif sem == '4':
        forms.is_sem4_filled = True
    elif sem == '5':
        forms.is_sem5_filled = True
    elif sem == '6':
        forms.is_sem6_filled = True
    elif sem == '7':
        forms.is_sem7_filled = True
    elif sem == '8':
        forms.is_sem8_filled = True
    forms.save()


def is_prev_sems_filled(id, curr_sem):
    forms = FormFills.objects.get(student=Student.objects.get(id=id))
    filled_sem = forms.sem_fills_easy()
    sem = int(sem)
    for x in range[1, sem]:
        if not filled_sem[str(x)]:
            return x
    return 0


def any_sem_yet(id):
    stud = Student.objects.get(id=id)
    batch = stud.batch
    year = int(batch[3:7])
    date = datetime.datetime.now()
    current_year = int(date.year)
    current_month = int(date.month)
    diff = current_year - year
    if diff == 0 or (diff == 1 and current_month == 2):
        return False
    return True


def get_page_details(id):
    forms = FormFills.objects.get(student=id)
    sems = forms.sem_fills_easy()
    stud = Student.objects.get(id=id)
    class page:
        def __init__(self, name, link, filled, sem=None, sem_no=None):
            self.name = name
            self.link = link
            self.filled = filled
            self.sem = sem
            self.sem_no = sem_no
    def true2yes(var):
        if var:
            return 'yes'
        else:
            return 'no'
    pages_details = [
        page('General Details', 'details', true2yes(forms.is_gen_details_filled)),
        page('University Details', None, true2yes(forms.is_univ_details_filled)),
        page('Extracurricular Details', 'extracurricular', 'na'),
        # Add Choose Elective page
    ]
    # Add sem fields and if a sem does not exist (eg. sem8 for Mtech), skip that entry!
    for x in range(1, 9):
        if (stud.is_lateral and x in (1, 2)) or (stud.stream == 'D' and x in (7, 8)) or (stud.stream == 'M' and x in range(5, 9)):
            continue
        if str(x) in sems:
            pages_details.append(page(name=('Sem ' + str(x)), link='sem_marks', filled=sems[str(x)], sem=True, sem_no=x))
    details = {'pages': pages_details, 'nav_sems': sem_for_nav_bar(id)}

    return details


def extra_curricular(id):
    d = {
        'title': "Extracurricular activity",
        'nav_sems': sem_for_nav_bar(id)
    }
    if ExtracurricularActivity.objects.filter(student=id).exists():
        ea = ExtracurricularActivity.objects.get(student=id)
        d['sftskl_condt'] = ea.soft_skill_conduct
        d['sftskl_attnd'] = ea.soft_skill_attend
        d['apti_condt'] = ea.aptitude_conduct
        d['apti_attnd'] = ea.aptitude_attend
        d['mck_intrvw'] = ea.mock_interview
        d['iv1_date'] = ea.industry_visit_1_date
        d['iv1_place'] = ea.industry_visit_1
        d['iv2_date'] = ea.industry_visit_2_date
        d['iv2_place'] = ea.industry_visit_2
        d['onln_tst'] = ea.online_test
        d['gate'] = ea.gate_exam
        d['cat'] = ea.cat_exam
        d['swrswti_puja'] = ea.saraswati_puja
        d['vswkrma_puja'] = ea.vishwakarma_puja
    if SeminarsWorkshops.objects.filter(attendee=id).exists():
        sw = SeminarsWorkshops.objects.filter(attendee=id)
        l = []

        class Seminar:
            def __init__(self, n, d, o):
                self.name = n
                self.date = d
                self.org = o
        for x in sw:
            l.append(Seminar(x.name, x.date, x.organiser))
        l = sorted(l, key=lambda x: x.date)
        d['wrk_shp_list'] = l
        d['wrk_shp'] = len(l)
    else:
        d['wrk_shp'] = 0

    if Counselings.objects.filter(student=id).exists():
        cs = Counselings.objects.filter(student=id)
        l = []

        class Counciling:
            def __init__(self, d, t):
                self.date = d
                self.topic = t
        for x in cs:
            l.append(Counciling(x.date, x.topic))
        d['counslng_count'] = len(l)
        l = sorted(l, key=lambda x: x.date)
        d['counslng_list'] = l
    else:
        d['counslng_count'] = 0

    if Contributions.objects.filter(student=id).exists():
        cbs = Contributions.objects.get(student=id)
        d['contribs'] = cbs.contributions
        d['ann_mag_pap_pub'] = cbs.annual_magazine_paper
        d['ann_mag_evnts'] = cbs.annual_magazine_event
        d['wall_mag_evnts'] = cbs.wall_magazine_event
        d['wall_mag_pap_pub'] = cbs.wall_magazine_paper
        d['tech_contst'] = cbs.technical_contests
        d['awrds'] = cbs.technical_academic_awards
    return d


def sem_for_nav_bar(id):
    stud = Student.objects.get(id=id)

    class Semester:
        def __init__(self, num, state):
            self.num = num
            self.state = state

    cur_sem = current_sem(id)
    l = []
    for x in range(1, cur_sem+1):
        if stud.is_lateral and x in (1, 2):
            l.append(Semester(x, 'true'))
        else:
            l.append(Semester(x, 'false'))

    if stud.stream == "B":
        max_sem = 8
    elif stud.stream == "D":
        max_sem = 6
    elif stud.stream == "M":
        max_sem = 4
    for x in range(int(current_sem(id))+1, max_sem+1):
        l.append(Semester(x, 'true'))
    return l


def comma_separated_add(model_obj, input_obj):
    '''
    ... This function helps to add comma seperated fields, doing various integrity checks.
    ... Param 1: The object of the model
    ... Param 2: The variable storing the input
    ... Returns: A sting with all modifications(if at all!)
    '''
    if input_obj:
        if input_obj[-1] in (',', '\n',):
            input_obj = input_obj[:-1]
        model_obj = model_obj.split(', ')
        input_obj = input_obj.split(',')
        if model_obj[0] in (' ', ''):
            model_obj.pop(0)
        for x in input_obj:
            x = x.strip()
            if x not in model_obj:
                model_obj.append(x)
        model_obj = ', '.join(model_obj)
    return model_obj


def yes_to_true(var):
    if var == "yes":
        return True
    else:
        return False
