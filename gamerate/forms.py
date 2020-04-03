from django import forms
from gamerate.models import UserProfile, Game, Category, Review
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'password',}

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = {'profile_image'}

class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter the game name.")
    category = forms.ModelChoiceField(queryset = Category.objects.all(),help_text="Please enter the category of the game.")
    release_date = forms.DateField(help_text="Please enter the release date of the game.", required=False)
    system = forms.CharField(max_length=64,help_text="Please enter the system which runs the game.", required=False)
    age_rating = forms.CharField(max_length=3,help_text="Please enter the age rating for the game.", required=False)
    developer = forms.CharField(max_length=64,help_text="Please enter the developer name.", required=False)
    publisher = forms.CharField(max_length=64,help_text="Please enter the publisher name.", required=False)
    description = forms.CharField(max_length=256,help_text="Please enter a brief description of the game.", required=False)
    cover_art = forms.ImageField(help_text="Please upload cover art of the game.", required=False)

    likes=forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug=forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Game
        exclude = ( 'slug',)

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter the category name.")
    slug=forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Category
        fields = ('name',)

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(help_text="Please enter a your 5 star rating of the game.", required=True)
    comment = forms.CharField(max_length=256,help_text="Please enter your review of the game.", required=True)
    class Meta:
        model = Review
        exclude = ('user','game',)
