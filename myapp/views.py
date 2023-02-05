from django.shortcuts import render
from . models import Lawyer, Client
from . forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'myapp/index.html')

def lawyer_reg(request):
    return render(request, 'myapp/lawyer_reg.html')


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration successfully")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'myapp/register.html', context)


def login(request):
    return render(request, 'myapp/login.html')


def lawyers(request):
    lawyer = Lawyer.objects.all()
    return render(request, 'myapp/lawyers.html', {'lawyers': lawyer})


def clients(request):
    client = Client.objects.all()
    return render(request, 'myapp/clients.html', {'clients': client})
