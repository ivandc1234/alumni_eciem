# Generated by Django 4.1.4 on 2023-01-15 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa_laboral', '0008_rename_post_actividades_actividades'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actividades',
            new_name='Eventos',
        ),
    ]
