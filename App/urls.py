from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients, name="clients"),
    path('lawyers/', views.lawyers, name="lawyers"),
    path('lawyerdashboard/', views.lawyerdashboard, name="lawyerdashboard"),
    path('clientdashboard/', views.clientdashboard, name="clientdashboard"),
    path('lawyerprofile/', views.lawyerprofile, name="lawyerprofile"),
    path('clientprofile/', views.clientprofile, name="clientprofile"),
    path('cases/', views.cases, name="cases"),
    path('match/', views.match, name="match"),
]
