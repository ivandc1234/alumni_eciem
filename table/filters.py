from .models import *
import django_filters
from django import forms
import django_filters as filters
from django_filters import CharFilter

#Filtros que se utilizan en el directorio admin

class EstudianteFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['nombres','apellidos','carrera','situacion_laboral','area_interes','programas_interes']


        widgets = {
            'carrera': forms.Select(attrs={'class': 'form-control'}),

    
     }
#Filtros que se utilizan en el directorio alumni
class EstudianteFilter_alumnos(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['nombres','apellidos','carrera']


        widgets = {
        'carrera': forms.Select(attrs={'class': 'form-control'}),
        
    }
