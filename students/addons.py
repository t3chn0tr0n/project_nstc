from subject_and_marks.models import SemMarks
from teachers.models import Teacher

from .models import (Class10, Class12, Contributions, Details,
                     ExtracurricularActivity, SeminarWorkshop, Student)

def get_idcard_details(id):
    """
    return name, card number, roll number, email, department, mentor
    """
    pass