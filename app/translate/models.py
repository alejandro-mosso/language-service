"""
    Create your models here.
    After adding new model configure app/settings.py to add 'translate' app
    And run in command line:
        $ python3 manage.py makemigrations
        $ python3 manage.py migrate
        $ python3 manage.py runserver 0.0.0.0:9000
"""
from django.db import models


class TranslateModel(models.Model):
    text = models.TextField(default='"Unknown"')
    src = models.CharField(max_length=5, blank=False, default='en')
    dest = models.CharField(max_length=5, blank=False, default='es')
