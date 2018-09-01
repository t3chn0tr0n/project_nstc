from django.urls import path, include, re_path
from . import views, pyfunctions

urlpatterns = [
    path('', views.login),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    re_path(r'validate/*', views.activate, name='activate'),
    path('resend/', views.resend, name='resend'),
]
