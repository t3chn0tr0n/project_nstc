from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_csv_upload/', upload_student, name="upload_student"),
    path('student_csv_download/', download_student, name="download_student"),
    path('student_csv_upload/upload_student/', upload_student),
    path('search/', student_search, name="search"),
    path('mentees/', mentees_list, name="mentees_list"),
    re_path(r'view_student/(NIT\/([2-9][0-9][0-9][0-9])\/([0-9][0-9][0-9][0-9]))',
            view_student, name="view_student"),
    path('princi_teacher_view/', princi_teacher_view, name="princi_teacher_view"),
    path('princi_teacher_view/assign_hod/', assign_hod, name="assign_hod"),
    path('teacher_profile/', profile, name="teacher_profile"),
    path('int_marks/', int_marks, name="int_marks"),
    path('manage_mentor/', manage_mentor, name="manage_mentor"),
    path('manage_mentor/mentor_student_show/', mentor_student_show, name="mentor_student_show"),
    path('manage_mentor/mentor_change/', mentor_change, name="mentor_change"),
    path('teacher_profile/change_profile/',
         change_profile, name="change_profile"),
    path('teacher_profile/upload_profile_pic/',
         upload_profile_pic, name="upload_profile_pic"),
    path('search/search_filter/', search_filter, name="search_filter"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
