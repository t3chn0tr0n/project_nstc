from builtins import object

from .models import Class10, Class12, Contributions, Details, \
    ExtracurricularActivity, SeminarWorkshop, Student
from subject_and_marks.models import SemMarks
from teachers.models import Teacher


def get_idcard_details(id):
    """
    return name, card number, roll number, email, department, mentor
    """
    try:
        stud = Student.objects.get(id=id)
        details = {
            'name' : stud.name, 
            'id' : stud.id, 
            'roll' : stud.id,
            'email' : stud.email, 
            'department' : stud.stream, 
            'mentor' : stud.mentor.name
        }
        return details
    except:
        return False