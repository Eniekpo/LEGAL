from django.shortcuts import render
from . models import Lawyer, Client

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')


def lawyers_reg(request):
    return render(request, 'myapp/lawyers_reg.html')


def clients_reg(request):
    return render(request, 'myapp/clients_reg.html')


def lawyers(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'myapp/lawyers.html', {'lawyers': lawyers})


def clients(request):
    clients = Client.objects.all()
    return render(request, 'myapp/clients.html', {'clients': clients})
