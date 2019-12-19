from students.addons import current_sem, get_sem_details
from students.models import Student

from .models import Teacher


def mentees_of(teacher, year):
    try:
        if year == 1:
            mentees = teacher.mentees1
        elif year == 2:
            mentees = teacher.mentees2
        elif year == 3:
            mentees = teacher.mentees3
        elif year == 4:
            mentees = teacher.mentees4

        mentees = mentees.split('-')
        mentees[0] = int(mentees[0])
        mentees[1] = int(mentees[1])
        start_stud = Student.objects.get(id=mentees[0])
        end_stud = Student.objects.get(id=mentees[1])
        start_stud = start_stud.roll_no
        end_stud = end_stud.roll_no
        list_of_mentees = []
        for r_no in range(start_stud, end_stud + 1):
            list_of_mentees.append(Student.objects.get(roll_no=r_no))
        return list_of_mentees
    except:
        return False


def get_teach_details(request):
    teach = Teacher.objects.get(id=request.user.username)
    rank = teach.desig
    if teach.is_principal:
        rank = "Principal"
    elif teach.is_hod:
        rank = "HOD"
    d = {
        'id': teach.id,
        'dept': teach.dept,
        'rank': rank,
        'is_hod': teach.is_hod,
        'is_princi': teach.is_principal,
    }
    return d


def get_sem_results_for(id):
    d1 = {}
    stud = Student.objects.get(id=id)
    cur_sem = current_sem(id)
    if stud.is_lateral:
        d1['lat_sems'] = (1, 2)
        d1['lat'] = True

    if stud.stream == "B":
        max_sem = 8
    elif stud.stream == "D":
        max_sem = 6
    elif stud.stream == "M":
        max_sem = 4

    d['available'] = range(1, cur_sem + 1)
    d['not_available'] = range(cur_sem + 1, max_sem + 1)
    d['invalid'] = range(max_sem + 1, 9)

    for sem in range(cur_sem + 1):
        d = get_sem_details(id, sem)
        if d.get('not_found'):
            pass
    pass
