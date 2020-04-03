from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from gamerate.models import Category, Game, Favourite, Review
from gamerate.forms import UserForm, UserProfileForm, GameForm, CategoryForm, ReviewForm

def home(request):
    game_list = Game.objects.order_by('name')[:10]
    category_list = Category.objects.order_by('name')[:10]
    context_dict = {}
    context_dict['games'] = game_list
    context_dict['categories'] = category_list
    response = render(request, 'gamerate/home.html', context=context_dict)
    return response


def most_popular(request):
    context_dict = {}
    game_list = Game.objects.order_by('-likes')[:10]
    context_dict['games'] = game_list
    category_list = Category.objects.order_by('name')[:10]
    context_dict['categories'] = category_list
    response = render(request, 'gamerate/most_popular.html', context=context_dict)
    return response


def highest_rated(request):
    context_dict = {}
    game_list = Game.objects.order_by('-likes')[:10]
    context_dict['games'] = game_list
    category_list = Category.objects.order_by('name')[:10]
    context_dict['categories'] = category_list
    response = render(request, 'gamerate/highest_rated.html', context=context_dict)
    return response


def contact_us(request):
    context_dict = {}
    category_list = Category.objects.order_by('name')[:10]
    context_dict['categories'] = category_list
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
    category_list = Category.objects.order_by('name')[:10]
    context_dict['categories'] = category_list
    response = render(request, 'gamerate/my_account.html', context=context_dict)
    return response


def add_game(request):
    form = GameForm()
    if request.method =='POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/gamerate/home/')
        else:
            print(form.errors)
    return render(request, 'gamerate/add_game.html',{'form':form})

def add_category(request):
    form = CategoryForm()
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/gamerate/home/')
        else:
            print(form.errors)
    return render(request, 'gamerate/add_category.html',{'form':form})

def add_review(request, game_name_slug):
    try:
        game = Game.objects.get(slug=game_name_slug)
    except Game.DoesNotExist:
        game  = None
    if game is None:
        return redirect('/gamerate/home/')
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user;
            if game:
                review.game = game
                review.save()
                return redirect(reverse('gamerate:show_game',kwargs={'game_name_slug':game_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'game': game}
    return render(request, 'gamerate/add_review.html', context=context_dict)

def show_game(request, game_name_slug):
    context_dict ={}
    category_list = Category.objects.order_by('name')[:10]
    context_dict['categories'] = category_list
    try:
        game = Game.objects.get(slug=game_name_slug)
        context_dict['game'] = game
    except Game.DoesNotExist:
        context_dict['game'] = None
    return render(request,'gamerate/game.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict ={}
    category_list = Category.objects.order_by('name')[:10]
    context_dict['categories'] = category_list
    try:
        category = Category.objects.get(slug=category_name_slug)
        games = Game.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['games'] = games
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['games'] = None
    return render(request,'gamerate/category.html', context=context_dict)
