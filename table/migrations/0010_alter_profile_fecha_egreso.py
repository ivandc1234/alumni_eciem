# Generated by Django 4.1.3 on 2022-11-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0009_alter_profile_carrera_alter_profile_grado_maximo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fecha_egreso',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]