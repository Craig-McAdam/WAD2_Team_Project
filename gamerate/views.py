from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# from gamerate.models import ...
# from gamerate.forms import ...

def home(request):
    context_dict = {}
    response = render(request, 'gamerate/home.html', context=context_dict)
    return response


def most_popular(request):
    context_dict = {}
    response = render(request, 'gamerate/most_popular.html', context=context_dict)
    return response


def highest_rated(request):
    context_dict = {}
    response = render(request, 'gamerate/highest_rated.html', context=context_dict)
    return response


def contact_us(request):
    context_dict = {}
    response = render(request, 'gamerate/contact_us.html', context=context_dict)
    return response


def user_login(request):
    context_dict = {}
    response = render(request, 'gamerate/login.html', context=context_dict)
    return response


def my_account(request):
    context_dict = {}
    response = render(request, 'gamerate/my_account.html', context=context_dict)
    return response


def add_game(request):
    context_dict = {}
    response = render(request, 'gamerate/add_game.html', context=context_dict)
    return response

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('gamerate:home'))

# views and templates needed for category pages
