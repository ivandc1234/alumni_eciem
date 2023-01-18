from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()


#Estas funciones se utilizan para modificar el comportamiento de otras funciones, en este caso para crear diferenciar los permisos a los que tienen acceso los distintos tipos de usuarios a modulos especificos.


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = get_user_model()
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("No estas autorizado")
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "estudiante":
            return redirect("index")
        if group == "admin":
            return view_func(request, *args, **kwargs)

    return wrapper_func
