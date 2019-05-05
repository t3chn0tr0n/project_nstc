from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('student_report/', student_report, name="student_report"),
    path('mentees/', mentees, name="mentees"),
    path('student_report/update/', update, name="update"),
    path('makaut_csv_upload/', upload_student, name="upload_student"),
    path('makaut_csv_upload/upload_student/', upload_student),
]
