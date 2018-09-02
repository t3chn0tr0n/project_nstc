from django.db import models
from students.models import Student


class Teacher(models.Model):
    id = models.CharField(default=" ", max_length=15, primary_key=True)
    name = models.CharField(default=" ", max_length=50)
    code_name = models.CharField(default=" ", max_length=5)
    stream = models.CharField(default=" ", max_length=20) # stores as cse, ece, etc
    mentees1 = models.CharField(default="0-0", max_length=27)
    mentees2 = models.CharField(default="0-0", max_length=27)
    mentees3 = models.CharField(default="0-0", max_length=27)
    mentees4 = models.CharField(default="0-0", max_length=27)
    is_registered = models.BooleanField(default=False) 
    is_varified = models.BooleanField(default=False)
    email = models.EmailField(max_length=70)
    is_hod = models.BooleanField(default=False)

    def mentees_of(self, yr):
        if yr == 1:
            mentees = self.mentees1

        elif yr == 2:
            mentees = self.mentees2
        
        elif yr == 3:
            mentees = self.mentees3

        elif yr == 4:
            mentees = self.mentees4
        
        try:
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
