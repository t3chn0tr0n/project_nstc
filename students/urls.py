from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'demo/$', views.demo),
    re_path(r'details/$', views.general_details, name='details'),
    re_path(r'univ_details/$', views.univ_details, name='univ_details'),
    re_path(r'sem/([1-8])/$', views.sem_marks, name="sem_marks"),
]
