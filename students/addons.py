from builtins import object

from .models import Class10, Class12, Contributions, Details, \
    ExtracurricularActivity, FormFills, SeminarWorkshop, Student

import datetime
from subject_and_marks.models import SemMarks, Subjects
from teachers.models import Teacher


def get_idcard_details(id):
    try:
        stud = Student.objects.get(id=id)
        details = {
            'name': stud.name,
            'id': stud.id,
            'card_no': stud.id,
            'roll_no': stud.roll_no,
            'email': stud.email,
            'dept': stud.stream,
            'mentor': stud.mentor.name
        }
        if stud.is_lateral:
            details['is_diploma'] = True
        return details
    except:
        return False


def get_univ_details(id):
    stud = Student.objects.get(id=id)
    filled_forms = FormFills.objects.get(student=id)
    if filled_forms.is_univ_details_filled:
        details = {
            'admin_no':  stud.admission_no,
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
                        Subject(('L'+ str(int(x)-6)), sems_marks[x][0], sems_marks[x][1], sems_marks[x][2]))
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
            subs = Subjects.objects.get(batch=stud.batch, dept=stud.dept, stream=stud.stream, sem=sem)
            subs = subs.all_subs()
            all_subs = []
            for x in range(1,len(subs)+1):
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