from django.urls import path
from gamerate import views

app_name = 'gamerate'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('most-popular/', views.most_popular, name='most_popular'),
    path('highest-rated/', views.highest_rated, name='highest_rated'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('login/', views.user_login, name='login'),
    # path needed for my_account
    # path needed for add_game
    path('logout/', views.user_logout, name='logout'),
    # paths needed for category pages

]