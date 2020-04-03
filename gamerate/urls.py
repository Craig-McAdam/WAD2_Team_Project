from django.urls import path
from django.conf.urls import url
from gamerate import views

app_name = 'gamerate'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('most-popular/', views.most_popular, name='most_popular'),
    path('highest-rated/', views.highest_rated, name='highest_rated'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('game/<slug:game_name_slug>/', views.show_game, name='show_game'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_category/', views.add_category, name='add_category'),
    path('game/<slug:game_name_slug>/add_review/', views.add_review, name='add_review'),
]
