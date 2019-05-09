from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('student_csv_upload/', upload_student, name="upload_student"),
    path('student_csv_upload/upload_student/', upload_student),
]
