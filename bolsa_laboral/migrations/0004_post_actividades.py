# Generated by Django 4.1.3 on 2022-11-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsa_laboral', '0003_post_beneficios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='actividades/images/')),
            ],
        ),
    ]
