# Generated by Django 4.1.2 on 2022-11-09 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_profile_cargo_actual_profile_celular_profile_ciudad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nivel_ingles',
        ),
    ]
