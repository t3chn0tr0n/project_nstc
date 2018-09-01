from django.db import models


class SemMarks(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    sem_no = models.IntegerField(default=0)
    max_score_in_class = models.FloatField(default=0.0, max_length=5)
    no_of_tutorial_class = models.IntegerField(default=0)		
    attentence = models.IntegerField(default=0) 	
    disciplinary_action = models.CharField(default="", max_length=50) 
    no_of_fschool_class  = 	models.IntegerField(default=0)
    scl_activities = models.CharField(default="", max_length=50) 	

    sub1 = models.CharField(default="", max_length=50)
    sub1_internal = models.FloatField(default=0.0, max_length=5)	
    sub1_marks = models.FloatField(default=0.0, max_length=5) 		

    sub2 = models.CharField(default="", max_length=50)	 	
    sub2_internal = models.FloatField(default=0.0, max_length=5) 		
    sub2_marks = models.FloatField(default=0.0, max_length=5) 		

    sub3 = models.CharField(default="", max_length=50)	 	
    sub3_internal = models.FloatField(default=0.0, max_length=5) 		
    sub3_marks = models.FloatField(default=0.0, max_length=5) 		

    sub4 = models.CharField(default="", max_length=50)	 	
    sub4_internal = models.FloatField(default=0.0, max_length=5) 		
    sub4_marks = models.FloatField(default=0.0, max_length=5) 		

    sub5 = models.CharField(default="", max_length=50)	 	
    sub5_internal = models.FloatField(default=0.0, max_length=5) 		
    sub5_marks = models.FloatField(default=0.0, max_length=5) 		

    sub6 = models.CharField(default="", max_length=50)
    sub6_internal = models.FloatField(default=0.0, max_length=5)		
    sub6_marks = models.FloatField(default=0.0, max_length=5) 		

    lab1 = models.CharField(default="", max_length=50) 	 	
    lab1_internal = models.FloatField(default=0.0, max_length=5) 		
    lab1_marks = models.FloatField(default=0.0, max_length=5) 		

    lab2 = models.CharField(default="", max_length=50) 	 	
    lab2_internal = models.FloatField(default=0.0, max_length=5) 	 	
    lab2_marks = models.FloatField(default=0.0, max_length=5) 	 	

    lab3 = models.CharField(default="", max_length=50) 	 	
    lab3_internal = models.FloatField(default=0.0, max_length=5) 	 	
    lab3_marks = models.FloatField(default=0.0, max_length=5) 	 	

    lab4 = models.CharField(default="", max_length=50) 	 	
    lab4_internal = models.FloatField(default=0.0, max_length=5) 	 	
    lab4_marks = models.FloatField(default=0.0, max_length=5) 	 	

    lab5 = models.CharField(default="", max_length=50) 	 	
    lab5_internal = models.FloatField(default=0.0, max_length=5) 	 	
    lab5_marks = models.FloatField(default=0.0, max_length=5) 	 	

    sgpa = models.FloatField(default=0.0, max_length=4)

