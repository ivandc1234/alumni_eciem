from django.urls import path
from . import views 


urlpatterns = [
    path('geo', views.geo, name="geo"),

        ]
