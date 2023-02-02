from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('lawyers', views.lawyers, name='lawyers'),
    path('lawyers_reg', views.lawyers_reg, name='lawyers_reg'),
    path('clients_reg', views.clients_reg, name='clients_reg'),
]
