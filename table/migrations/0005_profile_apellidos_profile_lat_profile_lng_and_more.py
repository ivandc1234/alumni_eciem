# Generated by Django 4.1.2 on 2022-11-05 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_profile_nombres'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apellidos',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lat',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lng',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='situacion_laboral',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
