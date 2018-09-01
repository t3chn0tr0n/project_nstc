from django.db import models


class Teacher(models.Model):
    id = models.CharField(default=" ", max_length=15, primary_key=True)
    name = models.CharField(default=" ", max_length=50)
    code_name = models.CharField(default=" ", max_length=5)
    stream = models.CharField(default=" ", max_length=20) # stores as cse, ece, etc
    mentees1 = models.CharField(default="0-0", max_length=7)
    mentees2 = models.CharField(default="0-0", max_length=7)
    mentees3 = models.CharField(default="0-0", max_length=7)
    mentees4 = models.CharField(default="0-0", max_length=7)
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
            return mentees[0], mentees[1]
        except:
            return 0

    