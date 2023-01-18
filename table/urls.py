from django.urls import path 
from . import views
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
        


        path('', views.index, name="index"),
        path('area_alumni', views.area_alumni, name="area_alumni"),
        path('area_admin', views.area_admin, name="area_admin"),
        path('perfil', views.profile, name="profile"),
        path('contact', views.contact, name="contact"),
        path('contact_alumni/', views.contact_alumni, name="contact_alumni"),
        #register
        path('register/', views.register, name="register"),
        path('login/', views.login_page, name="login"),
        path('logout/', views.logoutUser, name="logout"),
        path('directorio_admin', views.directorio_admin, name='directorio2'),
        path('directorio_alumni', views.directorio_alumnos, name='directorio_alumnos'),
        #exportar csv
        path('export_csv', views.export_csv, name='export_csv'),

        #Recuperación de contraseña
        path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
        path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
        path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
        path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),



]
