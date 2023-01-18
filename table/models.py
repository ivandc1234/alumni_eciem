from django.db import models
from django.contrib.auth.models import User
from .choices import *
from phonenumber_field.modelfields import PhoneNumberField




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateField(null=True)
    
   #
    carrera = models.CharField(max_length=200, choices=CARRERA_CHOICES, null=True, blank= True)
    lat = models.CharField(max_length=300, null=True, blank= True)
    lng = models.CharField(max_length=300, null=True, blank= True)
    ciudad = models.CharField(max_length=300, null=True, blank= True)
    situacion_laboral = models.CharField(max_length=200,verbose_name="Situación Laboral",choices=SITUACION_LABORAL_CHOICES, null=True, blank= True)
    direccion = models.CharField(max_length=300, null=True, blank= True)
    linkedin = models.CharField(max_length=200, null=True, blank= True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    celular = PhoneNumberField(null=True,blank=True)
    cargo_actual = models.CharField(max_length=200,choices=CARGO_ACTUAL_CHOICES,null=True)
    dominio_ingles = models.CharField(max_length=200, choices=NIVEL_INGLES_CHOICES,null=True) 
    titulado = models.CharField(max_length=200,null=True,choices=TITULADO_CHOICES)
    grado_maximo = models.CharField(max_length=200,null=True,choices=GRADO_MAXIMO_CHOICES)
    sector_trabajo = models.CharField(max_length=200,null=True,choices=SECTOR_TRABAJO_CHOICES)
    fecha_egreso = models.IntegerField(null=True, blank=True)
    programas_interes = models.CharField(max_length=200,verbose_name="Programas Interés",null=True, blank=True, choices= PROGRAMAS_INTERES_CHOICES)
    ingresos = models.CharField(max_length=200, null=True, blank=True, choices=INGRESOS_CHOICES)
    primer_empleo = models.CharField(max_length=200, null=True, blank=True, choices=PRIMER_EMPLEO_CHOICES)
    continuidad_estudios = models.CharField(max_length=200, null=True, blank=True, choices=CONTINUIDAD_ESTUDIOS_CHOICES)
    oferta_eciem = models.CharField(max_length=200, null=True, blank=True, choices=OFERTA_ECIEM_CHOICES)
    interes_colaboracion = models.CharField(max_length=200, null=True, blank=True, choices=INTERES_COLABORACION_CHOICES)
    tipo_colaboracion = models.CharField(max_length=200, null=True, blank=True, choices=TIPO_COLABORACION_CHOICES)
    area_interes = models.CharField(max_length=200, null=True,verbose_name="Área Interés", choices=AREAS_INTERES_CHOICES)



    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
