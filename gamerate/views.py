from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# from gamerate.models import ...
from gamerate.forms import UserForm, UserProfileForm

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


def user_registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)  #
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'gamerate/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('gamerate:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("invalid login details supplied.")
    else:
        return render(request, 'gamerate/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('gamerate:home'))


def my_account(request):
    context_dict = {}
    response = render(request, 'gamerate/my_account.html', context=context_dict)
    return response


def add_game(request):
    context_dict = {}
    response = render(request, 'gamerate/add_game.html', context=context_dict)
    return response

# views and templates needed for category pages

# remove before final submission
def testing(request):
    # space to test code
    context_dict = {}
    response = render(request, 'gamerate/testing.html', context=context_dict)
    return response
