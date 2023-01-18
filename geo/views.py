from django.shortcuts import render
import folium
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import *
from table.decorators import admin_only, unauthenticated_user, allowed_users
from table.models import Profile



@login_required(login_url='login')
@admin_only
def geo(request):
    from django_pandas.io import read_frame
    #Se crea un dataframe con los datos de la clase Profile excluyendo los valores que no tenga latitud para de esta manera evitar errores
    qs = Profile.objects.exclude(lat__isnull=True)

    df = read_frame(qs)

    #Convierte columnas del df a numéricas  
    df['lat'] = pd.to_numeric(df['lat'])
    df['lng'] = pd.to_numeric(df['lng'])

  
    #Ubicación donde se centra el mapa al iniciar y el zoom de este
    #Para comprender como utilizar libreria de folium 
    #https://towardsdatascience.com/use-html-in-folium-maps-a-comprehensive-guide-for-data-scientists-3af10baf9190
    location = [-29.90453,-71.24894]
    m = folium.Map(location=location,zoom_start=7) 

    #Se crea un ciclo desde el primer valor hasta el total de la longitud del df, y se hacen condicionales para distinguir las situaciones de empleabilidad de los egresados
    for i in range(0,len(df)):
        situacion_laboral = df['situacion_laboral'].iloc[i]
        if situacion_laboral == 'Empleado' or situacion_laboral== 'Empleado buscando otro trabajo':
            color = 'darkblue'
        elif situacion_laboral == 'Desempleado' or situacion_laboral == 'Otro':
            color = 'lightbrown'
        else:
            color = 'gray'


        #Función que muestra el cuadro de información del egresado, cuando se da click en su icono
        def popup_html(row):
            i = row
            nombre=df['nombres'].iloc[i] 
            apellido=df['apellidos'].iloc[i] 
            situacion_laboral=df['situacion_laboral'].iloc[i]
            carrera = df['carrera'].iloc[i] 
            linkedin = df['linkedin'].iloc[i] 
   

            left_col_color = "rgba(30, 66, 150)"
            right_col_color = "#fff"
            
            html = """<!DOCTYPE html>
        <html>
        <head>
        <h4 style="margin-bottom:10"; width="200px"; >{}</h4>""".format(nombre +" " + apellido)+  """
        </head>
            <table style="height: 126px; width: 350px; border:2px solid;">
        <tbody>
        <tr style="border:1px solid;">
        <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Carrera</span></td>
        <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(carrera) + """
        </tr>
        <tr>
        <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">Situación Laboral</span></td>
        <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(situacion_laboral) + """

        <tr style="border:1px solid;">
        </tr>

        <tr>
        <td style="background-color: """+ left_col_color +""";"><span style="color: #ffffff;">LinkedIn</span></td>
        <td style="width: 150px;bckground-color: """+ right_col_color +""";"><a>{}</a></td>""".format(linkedin) + """
        </tr>
       
      
        </tbody>
        </table>
        </html>
        """
            return html

        html = popup_html(i)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)

       #Se crea un markador en cada un de las ubicaciones registradas en el dt, añadiendo el icono previamente definido 
        folium.Marker([df['lat'].iloc[i],df['lng'].iloc[i]],
                  popup=popup,icon=folium.Icon(color=color, icon='graduation-cap', prefix='fa')).add_to(m)



    m = m._repr_html_()

    context = {
        'm':m,
    }

    return render( request, 'geo.html', context)

