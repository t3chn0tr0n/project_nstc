from .models import Class10, Class12, Contributions, Details, \
    ExtracurricularActivity, SeminarWorkshop, Student, FormFills


from subject_and_marks.models import SemMarks
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
            'department': stud.stream,
            'mentor': stud.mentor.name
        }
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
