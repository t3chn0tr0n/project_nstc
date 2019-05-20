from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('student_mar_report/', student_report, name="student_report"),
    path('makaut_mar/', mentees, name="mentees"),
    path('student_mar_report/update/', update, name="update"),
]
