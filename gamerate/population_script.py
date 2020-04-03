import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2_Team_Project.settings')

import django
django.setup()
from gamerate.models import Category, Game

def populate():
    categories_list = []

    with open('/home/2350871G/WAD2_Team_Project/population_data/categories.csv') as categories:
        categoriesReader = csv.reader(categories)
        for cat in categoriesReader:
            categories_list+=cat

    categories_dict = {}

    for cat in categories_list:
        categories_dict[cat] = {'games': []}

    with open('/home/2350871G/WAD2_Team_Project/population_data/games.csv') as games:
        gamesReader = csv.reader(games)
        for game in gamesReader:
            for category in categories_dict.keys():
                if game[1] == category:
                    categories_dict[category]['games'].append({'title': game[0], 'category': game[1], 'system': game[2], 'developer': game[3], 'publisher': game[4], 'description': game[5], 'rating': game[6], 'cover': game[7], 'releaseDate': game[8]})

    for cat, cat_data in categories_dict.items():
        c = add_cat(cat)
        for g in cat_data['games']:
            add_game(c, g['title'], g['system'], g['developer'], g['publisher'], g['description'], g['rating'], g['cover'])

    for c in Category.objects.all():
        for g in Game.objects.filter(category=c):
            print(f'- {c}: {g}')

def add_game(category, title, system, developer, publisher, description, rating, cover):
    g = Game.objects.get_or_create(name=title, category=category, system=system, developer=developer, publisher=publisher, description=description, age_rating=rating, cover_art=cover)[0]
    g.save()
    return g

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == '__main__':
    print('Starting gamerate population script...')
    populate()