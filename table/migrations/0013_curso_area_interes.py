# Generated by Django 4.1.3 on 2022-11-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0012_remove_profile_image_alter_profile_tipo_colaboracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Area_interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ManyToManyField(to='table.curso')),
            ],
        ),
    ]
