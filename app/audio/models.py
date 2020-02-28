"""
    Create your models here.
    After adding new model configure app/settings.py to add 'audio' app
    And run in command line:
        $ python3 manage.py makemigrations
        $ python3 manage.py migrate
        $ python3 manage.py runserver 0.0.0.0:9000
"""
from django.db import models


class AudioModel(models.Model):
    word = models.TextField(default='"Unknown"')
    language = models.TextField(default='"english"')
