from django.db import models


class SemMarks(models.Model):
    student_id = models.CharField(default=" ", max_length=15, primary_key=True)
    sem_no = models.IntegerField(default=0)
    max_score_in_class = models.FloatField(default=0.0, max_length=5)
    no_of_tutorial_class = models.IntegerField(default=0)		
    attendance = models.IntegerField(default=0) 	
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

    def sems(self):
        return {
            "1": [self.sub1, self.sub1_internal, self.sub1_marks],
            "2": [self.sub2, self.sub2_internal, self.sub2_marks],
            "3": [self.sub3, self.sub3_internal, self.sub3_marks],
            "4": [self.sub4, self.sub4_internal, self.sub4_marks],
            "5": [self.sub5, self.sub5_internal, self.sub5_marks],
            "6": [self.sub6, self.sub6_internal, self.sub6_marks],
            "7": [self.lab1, self.lab1_internal, self.lab1_marks],
            "8": [self.lab2, self.lab2_internal, self.lab2_marks],
            "9": [self.lab3, self.lab3_internal, self.lab3_marks],
            "10": [self.lab4, self.lab4_internal, self.lab4_marks],
            "11": [self.lab5, self.lab5_internal, self.lab5_marks]
        }


class Subjects(models.Model):
    sem = models.IntegerField(default=0)
    sub1 = models.CharField(default="", max_length=8)
    sub2 = models.CharField(default="", max_length=8)
    sub3 = models.CharField(default="", max_length=8)
    sub4 = models.CharField(default="", max_length=8)
    sub5 = models.CharField(default="", max_length=8)
    sub6 = models.CharField(default="", max_length=8, null=True, blank=True)
    lab1 = models.CharField(default="", max_length=8)
    lab2 = models.CharField(default="", max_length=8)
    lab3 = models.CharField(default="", max_length=8)
    lab4 = models.CharField(default="", max_length=8)
    lab5 = models.CharField(default="", max_length=8, null=True, blank=True)

    def all_subs(self):
        return {
            "1": self.sub1, 
            "2": self.sub2, 
            "3": self.sub3, 
            "4": self.sub4, 
            "5": self.sub5, 
            "6": self.sub6, 
            "7": self.lab1, 
            "8": self.lab2, 
            "9": self.lab3, 
            "10": self.lab4,
            "11": self.lab5
        }