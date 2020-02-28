# Generated by Django 3.0.2 on 2020-02-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='"Unknown"')),
                ('src', models.CharField(default='en', max_length=5)),
                ('dest', models.CharField(default='es', max_length=5)),
            ],
        ),
    ]
