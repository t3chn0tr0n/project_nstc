from django.urls import include, path, re_path

from . import views

urlpatterns = [
    re_path(r'^demo/$', views.demo),
    path('details/', views.general_details, name='details'),
    path('univ_details/', views.univ_details, name='univ_details'),
    path('extracurricular_activity/', views.extracurricular_activities, name='extracurricular'),
    path('ea_form1/', views.ea_form1, name='ea_form1'),
    path('ea_form2/', views.ea_form2, name='ea_form2'),
    path('ea_form3/', views.ea_form3, name='ea_form3'),
    path('ea_form4/', views.ea_form4, name='ea_form4'),
    path('profile/', views.profile, name='profile'),
    re_path(r'^sem/([1-8])/$', views.sem_marks, name="sem_marks"),
    path('update_phone/', views.change_phone, name="change_phone"),
]
