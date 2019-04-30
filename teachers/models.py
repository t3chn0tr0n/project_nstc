from django.db import models


class Teacher(models.Model):
    id = models.CharField(default=" ", max_length=15, primary_key=True)
    name = models.CharField(default=" ", max_length=50)
    code_name = models.CharField(default=" ", max_length=5)
    dept = models.CharField(default=" ", max_length=20) # stores as cse, ece, etc
    mentees1 = models.CharField(default="0-0", max_length=27, null=True)
    mentees2 = models.CharField(default="0-0", max_length=27, null=True)
    mentees3 = models.CharField(default="0-0", max_length=27, null=True)
    mentees4 = models.CharField(default="0-0", max_length=27, null=True)
    is_registered = models.BooleanField(default=False) 
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(max_length=70)
    phone_no_1 = models.CharField(default=0, max_length=12)
    phone_no_2 = models.CharField(null=True, blank=True, max_length=12)
    is_hod = models.BooleanField(default=False)
