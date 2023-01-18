from django.shortcuts import render, redirect, HttpResponse
from .models import Profile
from .forms import ProfileUpdateForm, UserUpdateForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .filters import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import datetime
import csv

from .decorators import admin_only, unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

def index(request):
    return render(request,'index.html')

def area_alumni(request):
    return render(request,'area_alumni.html')


@login_required(login_url='login')
@admin_only  #Decorator que restringe el uso de este modulo a solo el usuario admin
def area_admin(request):
    return render(request,'area_admin.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            #Se crea este grupo para que al registrarse los egresados, queden inmediantemente registrados en el grupo estudiante.
            group = Group.objects.get(name='estudiante')
            user.groups.add(group)



            messages.success(request,"Usuario registrado correctamente")
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request,"register.html",{'form':form})



def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        #Condicional para redirigir al usuario una vez se haya logeado, dependiando del tipo de usuario
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('area_admin')
            return redirect('area_alumni')
        else:
             messages.info(request, "username or password incorrect")

    context = {}
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")




@login_required()
def profile(request):
    if request.method == "POST":

        form_u = UserUpdateForm(request.POST,instance=request.user)
        form_p = ProfileUpdateForm(request.POST,instance=request.user.profile)
        
        if form_u.is_valid() and form_p.is_valid():
            form_u.save()
            form_p.save()
            messages.success(request,"Perfil Actualizado!")
            return redirect('profile')
    else:
        form_u = UserUpdateForm(instance=request.user)
        form_p = ProfileUpdateForm(instance=request.user.profile)

    context = {

            'form_u':form_u,
            'form_p':form_p,
            }
    return render(request,"profile.html", context)

@login_required(login_url='login')
@admin_only
def directorio_admin(request):
    personas = Profile.objects.exclude(nombres = 'Admin')
    #Filtro
    myfilter = EstudianteFilter(request.GET, queryset=personas)
    personas = myfilter.qs

    return render(request, 'directorio_admin3.html', {'personas': personas,'myfilter':myfilter})



def directorio_alumnos(request):
    personas = Profile.objects.exclude(nombres='Admin')
    #Filtro
    myfilter = EstudianteFilter_alumnos(request.GET, queryset=personas)
    personas = myfilter.qs

    return render(request, 'directorio_alumnos3.html', {'personas': personas, 'myfilter': myfilter})



def export_csv(request):
    response = HttpResponse(content_type='text_csv')
    response['Content-Disposition'] = 'attachment; filename=Directorio' +\
        str(datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['direccion','carrera'])

    expenses = Profile.objects.all()
 
    for expense in expenses:
        writer.writerow([expense.direccion,expense.carrera])

    return response



def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message= request.POST['message'] + " Enviado por: " + request.POST['message_email']

        #Enviar correo
        send_mail(
            message_name, #asunto, en este caso el nombre de la persona
            message, #mensaje 
            settings.EMAIL_HOST_USER, #from email
            ['ivandiazc.22@gmail.com'] #to email
        )

        return render(request,'index.html',{'message_name':message_name})
    else:
        return render(request,'index.html',{})


def contact_alumni(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message= request.POST['message'] + " Enviado por: " + request.POST['message_email']

        #Enviar correo
        send_mail(
            message_name, #asunto, en este caso el nombre de la persona
            message, #mensaje 
            settings.EMAIL_HOST_USER, #from email
            ['ivandiazc.22@gmail.com'] #to email
        )

        return render(request,'contacto_alumni.html',{'message_name':message_name})
    else:
        return render(request,'contacto_alumni.html',{})




# Manejadores de códigos de error
def handler400(request, exception):
    return render(request, "error/400.html", status=400)


def handler403(request, exception):
    return render(request, "error/403.html", status=403)


def handler404(request, exception):
    return render(request, "error/404.html", status=404)


def handler500(request):
    return render(request, "error/500.html", status=500)


def handler500(request):
    return render(request, "error/500.html", status=500)
