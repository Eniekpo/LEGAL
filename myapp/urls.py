from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('lawyers', views.lawyers, name='lawyers'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
