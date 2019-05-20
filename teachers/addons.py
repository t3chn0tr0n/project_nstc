from .models import Teacher
from students.models import Student

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
        
        for r_no in range(start_stud, end_stud+1):
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
        }
    return d