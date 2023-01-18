from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Bolsa_laboral(models.Model):
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='bolsa_laboral/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bolsa Laboral"
        verbose_name_plural= "Bolsa Laboral" 


    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))


class Beneficios(models.Model):

    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='beneficios/images/')

    def __str__(self):
        return self.titulo 

    class Meta:
        verbose_name = "Beneficios"
        verbose_name_plural= "Beneficios" 

    def get_absolute_url(self):
        return reverse('post_detail_beneficios', args=(str(self.id)))



class Eventos(models.Model):

    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='actividades/images/')

    def __str__(self):
        return self.titulo 


    class Meta:
        verbose_name = "Eventos"
        verbose_name_plural= "Eventos" 


    def get_absolute_url(self):
        return reverse('post_detail_actividades', args=(str(self.id)))