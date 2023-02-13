from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('lawyers', views.lawyers, name='lawyers'),
    path('login', views.login, name='login'),
    path('match', views.match, name='match'),
    path('lawyerprofile', views.lawyerprofile, name='lawyerprofile'),
    path('lawyerdashboard', views.lawyerdashboard, name='lawyerdashboard'),
    path('clientprofile', views.clientprofile, name='clientprofile'),
    path('clientdashboard', views.clientdashboard, name='clientdashboard'),
]
