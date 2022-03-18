import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'djangoProject.settings')

django.setup()
from forum.models import *
import _sqlite3

def populate():

    conn = _sqlite3.connect("db.sqlites3")
    cursor = conn.cursor()
    print(conn)
    user1 = User.objects.create(username="admin",password="admin",is_staff=1,is_superuser=1)
    UserProfile.objects.create(user=user1,name="admin1")

    for user in UserProfile.objects.all():
        print(user)
    # for cat, cat_data in cats.items():
    #     c = add_cat(cat, cat_data['views'],cat_data['likes'])
    #     for p in cat_data['pages']:
    #         add_page(c, p['title'], p['url'],p['views'])
    #
    # # Print out the categories we have added.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print(f'- {c}: {p}')


def add_user(name, title, url, views):
    # p = UserProfile.objects.get_or_create(category=cat, title=title)[0]
    # p.url = url
    # p.views = views
    # p.save()
    # return p
    return None


def add_manager():
    return None


def add_module(name, views, likes):
    c = Module.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c


def add_post():
    return None


def add_start_content():
    return None


def add_comment():
    return None


if __name__ == '__main__':
    print('Starting population script...')
    populate()
