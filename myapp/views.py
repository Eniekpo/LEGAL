from django.shortcuts import render
from . models import Lawyer, Client
from . forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration successfully")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'myapp/index.html', context)


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
