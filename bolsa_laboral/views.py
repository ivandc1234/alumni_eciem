from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bolsa_laboral, Beneficios, Eventos


#Bolsa laboral
class HomeView(ListView):
    model = Bolsa_laboral
    template_name = 'bolsa_laboral/home.html'

class PostDetail(DetailView):
    model = Bolsa_laboral
    template_name = 'bolsa_laboral/post_detail.html'



#Beneficios
class HomeView_beneficios(ListView):
    model = Beneficios
    template_name = 'beneficios/home2.html'

class PostDetail_beneficios(DetailView):
    model = Beneficios
    template_name = 'beneficios/post_detail_beneficios.html'



#Actividades
class HomeView_actividades(ListView):
    model = Eventos
    template_name = 'actividades/home.html'

class PostDetail_actividades(DetailView):
    model = Eventos
    template_name = 'actividades/post_detail_actividades.html'

