from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput

from .models import Profile
from datetime import datetime



class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='username', 
                    widget=forms.TextInput(attrs={'placeholder': 'Rut'}))
    email = forms.EmailField(label='email', 
                    widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    
    password1 = forms.CharField(label='password1', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su Contraseña'}))

    password2 = forms.CharField(label='password2', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Repita su Contraseña'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']





#Formularios para el perfil

#UserUpdateForm (incluye nombre de usuario y mail)
#ProfileUpdateForm (incluye los campos del template del perfil)

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            #Los campos se ocultan ya que no es necario mostrarlos en la pagina del perfil
            'username': forms.HiddenInput(),
            'email': forms.HiddenInput(),
        }




class ProfileUpdateForm(forms.ModelForm):

    nombres = forms.CharField(label='Nombres', widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'class':'form-control'}))
    linkedin = forms.CharField(label='LinkedIn', widget=forms.TextInput(attrs={'class':'form-control'}))
    


    def possible_years(first_year_in_scroll, last_year_in_scroll):
        p_year = []
        for i in range(first_year_in_scroll, last_year_in_scroll, -1):
            p_year_tuple = str(i), i
            p_year.append(p_year_tuple)
        return p_year



    fecha_egreso = forms.ChoiceField(
    choices=possible_years(((datetime.now()).year), 1900),
    label='Año de egreso',widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:
        model = Profile
        fields = ['carrera','nombres','apellidos','fecha_nacimiento','sexo','direccion','celular','linkedin','titulado','fecha_egreso','lat','lng','grado_maximo','continuidad_estudios','area_interes','programas_interes','oferta_eciem','dominio_ingles','ciudad','situacion_laboral','sector_trabajo','cargo_actual','ingresos','primer_empleo','interes_colaboracion','tipo_colaboracion']
        labels = {
            'titulado':'¿Te encuentras titulado?',
            'fecha_egreso':'Año de egreso',
            'grado_maximo':'Máximo grado académico alcanzado',
            'continuidad_estudios':'¿Te gustaría continuar estudiando?',
            'area_interes':'¿Qué áreas de estudio te interesan más?',
            'programas_interes':'¿Qué tipo de programa te interesaría más?',
            'oferta_eciem':'¿Qué postgrado de la oferta actual de la ECIEM te interesaría cursar?',
            'dominio_ingles':'Grado de dominio del idioma inglés',
            'situacion_laboral':'Situación laboral',
            'sector_trabajo':'Sector donde trabajas',
            'cargo_actual':'Cargo que desempeñas',
            'ingresos': 'Nivel de ingresos líquidos mensuales',
            'primer_empleo':'Tiempo que transcurrió desde el egreso al primer empleo',
            'interes_colaboracion':'¿Te gustaría colaborar con ALUMNI ECIEM?',
            'tipo_colaboracion':'¿De qué forma te gustaría colaborar con ALUMNI ECIEM?',

        }

        widgets = {
        'fecha_egreso': DateInput(attrs={'type': 'date'}),
        'nombres': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
        'carrera': forms.Select(attrs={'class':'form-control'}),
        'sexo': forms.Select(attrs={'class':'form-control'}),
        'celular': forms.TextInput(attrs={'class': 'form-control','placeholder':'Incluir códido de área, ej: +56997031674'}),
        'direccion': forms.TextInput(attrs={'class':'form-control'}),
        'situacion_laboral': forms.Select(attrs={'class':'form-control'}),
        'linkedin': forms.TextInput(attrs={'class':'form-control'}),
        'ingresos': forms.Select(attrs={'class':'form-control'}),
        'titulado': forms.Select(attrs={'class':'form-control'}),
        'programas_interes': forms.Select(attrs={'class':'form-control'}),
        'area_interes': forms.Select(attrs={'class':'form-control'}),
        'oferta_eciem': forms.Select(attrs={'class':'form-control'}),
        'primer_empleo': forms.Select(attrs={'class':'form-control'}),
        'continuidad_estudios': forms.Select(attrs={'class':'form-control'}),
        'grado_maximo': forms.Select(attrs={'class':'form-control'}),
        'sector_trabajo': forms.Select(attrs={'class':'form-control'}),
        'dominio_ingles': forms.Select(attrs={'class':'form-control'}),
        'cargo_actual': forms.Select(attrs={'class':'form-control'}),
        'interes_colaboracion': forms.Select(attrs={'class':'form-control'}),
        'tipo_colaboracion': forms.Select(attrs={'class':'form-control'}),
        'lat': forms.HiddenInput(),
        'lng': forms.HiddenInput(),
        'ciudad': forms.HiddenInput(),
        
    }


