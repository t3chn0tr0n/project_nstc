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
        if current_month <= 7:
            current_sem = 2
        else:
            current_sem = 3
    elif dif == 2:
        if current_month <= 7:
            current_sem = 4
        else:
            current_sem = 5
    elif dif == 3:
        if current_month <= 7:
            current_sem = 6
        else:
            current_sem = 7
    else:
        current_sem = 8
    return current_sem


def get_sem_details(id, sem):
    no_details = False
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
        sem_details = SemMarks.objects.get(student_id=id, sem_no=sem)
    except:
        no_details = True

    if not no_details and is_sem_filled:
        all_subs = []
        sems_marks = sem_details.sems()
        for x in range(1, 12):
            x = str(x)
            if x > '6':
                all_subs.append(
                    Subject(('L'+ str(int(x)-6)), sem_marks[x][0], sems_marks[x][1], sems_marks[x][2]))
            else:
                all_subs.append(
                    Subject(x, sem_marks[x][0], sems_marks[x][1], sems_marks[x][2]))

        details = {
            'max_score_in_class': sem_details.max_score_in_class,
            'no_of_tutorial_class': sem_details.no_of_tutorial_class,
            'attendance': sem_details.attendance,
            'disciplinary_action': sem_details.disciplinary_action,
            'no_of_fschool_class': sem_details.no_of_fschool_class,
            'scl_activities': sem_details.scl_activities,
            'sgpa': sem_details.sgpa,
        }
    else:
        subs = Subjects.objects.get(sem=sem)
        subs = subs.all_subs()
        all_subs = []
        for x in range(1,len(subs)+1):
            if x > 6:
                all_subs.append(Subject(('L'+ str(x-6)), subs[str(x)]))
            else:
                all_subs.append(Subject(str(x), subs[str(x)]))
        details = {
            'not_found': True
        }
    details['curr_sem'] = sem
    details['all_subs'] = all_subs
    details['available'] = [str(x) for x in range(1, int(sem)+1)]
    details['not_available'] = [str(x) for x in range(int(sem)+1, 9)]   
    return details
    