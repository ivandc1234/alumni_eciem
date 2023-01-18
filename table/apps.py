from django.apps import AppConfig


class TableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'table'

    #Nombre que se muestra en el administrador de django
    verbose_name = "Tablas"
