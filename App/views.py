from django.shortcuts import render
# Login required to access private pagas
from django.contrib.auth.decorators import login_required
# Prevent back button (destroy the last section)
from django.views.decorators.cache import cache_control

from . forms import ClientForm, LawyerForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Frontend


def frontend(request):
    return render(request, "frontend.html")

# Backend


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "backend.html")


def clients(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "You Have Been Matched Successfully !")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'App/clients.html', context)


def lawyers(request):
    form = LawyerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration successfully")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'App/lawyers.html', context)


def lawyerprofile(request):
    return render(request, "App/lawyerprofile.html")


def clientprofile(request):
    return render(request, "App/clientprofile.html")


def cases(request):
    return render(request, "App/cases.html")


def match(request):
    return render(request, "App/match.html")
