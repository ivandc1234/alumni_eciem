from django.urls import path
from . import views 
from .views import *

urlpatterns = [
    #Bolsa laboral
    path('bolsa_laboral/', HomeView.as_view(), name="home"),
    path('post/int<int:pk>', PostDetail.as_view(), name="post_detail"),

    #Beneficios
    path('beneficios/', HomeView_beneficios.as_view(), name="beneficios"),
    path('post_beneficios/int<int:pk>', PostDetail_beneficios.as_view(), name="post_detail_beneficios"),
    

    #Actividades
    path('actividades/', HomeView_actividades.as_view(), name="actividades"),
    path('post_actividades/int<int:pk>', PostDetail_actividades.as_view(), name="post_detail_actividades"),
]
