from django.shortcuts import render
from . forms import ClientForm, LawyerForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'legalapp/index.html')


def clients(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration successfully")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'legalapp/clients.html', context)


def lawyers(request):
    form = LawyerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration successfully")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'legalapp/lawyers.html', context)
