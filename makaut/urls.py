from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('student_mar_report/', student_report, name="student_report"),
    path('makaut_mar/', mentees, name="mentees"),
    path('student_mar_report/update/', update, name="update"),
    path('student_mar_report/gen_certificate/', gen_certificate, name="gen_certificate"),
    re_path('certificate/(NIT\/([2-9][0-9][0-9][0-9])\/([0-9][0-9][0-9][0-9]))',
            certificate, name="certificate"),
]
