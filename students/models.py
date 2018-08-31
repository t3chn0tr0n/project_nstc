from django.db import models
from teachers import Teacher

class Student(model.Model):
    id = models.CharField(default=" ", max_length=15, primary_key=True)
    name = models.CharField(default=" ", max_length=50)
    mentor = models.ForeignKeyField(Teacher, on_delete=models.CASCADE)
    registration_no = models.IntegerField(default=0000, max_length=50)
    admision_no = models.IntegerField(default=0000, max_length=50)
    stream = models.CharField(default=" ", max_length=20) # stores as cse_btech, cse_mtech
    batch = models.IntegerField(default=0000, max_length=4) # stores the year the course started
    lateral = models.BooleanField(default=False)
    registered = models.BooleanField(default=False) 
    varified = models.BooleanField(default=False)
    email = models.EmailField(max_length=70)
