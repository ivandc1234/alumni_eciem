# Generated by Django 4.1.2 on 2022-11-08 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa_laboral', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
