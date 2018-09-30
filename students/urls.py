from django.urls import include, path

from . import views

urlpatterns = [
    path('demo/', views.demo),
    path('form1/', views.general_details, name='details'),
    path('univ_details/', views.univ_details, name='univ_details'),
]
