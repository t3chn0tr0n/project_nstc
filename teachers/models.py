from django.db import models


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
    phone_no_1 = models.IntegerField()
    phone_no_2 = models.IntegerField(null=True, blank=True)
    is_hod = models.BooleanField(default=False)
