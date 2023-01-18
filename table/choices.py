
#Opciones multiples utilizadas en el modelo


SEXO_CHOICES = [
        ('M','Masculino'),
        ('F','Femenino')
    ]

CARRERA_CHOICES = [
        ('IICG','Ingeniería en Información y Control de Gestión'),
        ('INGECO','Ingeniería Comercial'),
    ]

NIVEL_INGLES_CHOICES = [
        ('Ninguno','Ninguno'),
        ('Básico','Básico'),
        ('Intermedio','Intermedio'),
        ('Avanzado','Avanzado'),
    ]

SITUACION_LABORAL_CHOICES = [
        ('Empleado','Empleado'),
        ('Desempleado','Desempleado'),
        ('Empleado buscando otro trabajo','Empleado buscando otro trabajo'),
        ('No deseo ejercer','No deseo ejercer'),
    
    ]

GRADO_MAXIMO_CHOICES = [
        ('Licenciatura','Licenciatura'),
        ('Diplomado','Diplomado'),
        ('Magíster','Magíster'),
        ('Doctorado','Doctorado'),
        ('Podtdoctorado','Postdoctorado'),
    ]

SECTOR_TRABAJO_CHOICES = [
        ('Público','Público'),
        ('Privado','Privado'),
        ('Social','Social'),
        ('No me encuentro trabajando','No me encuentro trabajando'),
    ]

CARGO_ACTUAL_CHOICES = [
        ('Emprendedor o socio de mi empresa','Emprendedor o socio de mi empresa'),
        ('Cargo directivo o gerencial','Cargo directivo o gerencial'),
        ('Cargo subgerente o jefe de departamento','Cargo subgerente o jefe de departamento'),
        ('Profesional con trabajadores a cargo','Profesional con trabajadores a cargo'),
        ('Profesional sin trabajadores a cargo','Profesional sin trabajadores a cargo'),
        ('Independiente (freelance)','Independiente (freelance)'),
        ('No me encuentro trabajando','No me encuentro trabajando'),
    ]
TITULADO_CHOICES = [
    ('Sí','Sí'),
    ('No','No'),
]

PROGRAMAS_INTERES_CHOICES = [

    ('Talleres','Talleres'),
    ('Cursos','Cursos'),
    ('Magísteres','Magísteres'),
    ('Doctorados','Doctorados'),
    ('Ninguno','Ninguno'),
]

INGRESOS_CHOICES = [
    ('$0 a $500.000','$0 a $500.000'),
    ('$500.001 a $1.000.000','$500.001 a $1.000.000'),
    ('$1.000.001 a $1.500.000 ','$1.000.001 a $1.500.000'),
    ('$1.500.001 a $2.000.000','$1.500.001 a $2.000.000'),
    ('$2.000.001 a $2.500.000','$2.000.001 a $2.500.000'),
    ('$2.500.001 a $3.000.000','$2.500.001 a $3.000.000'),
    ('Más de $3.000.000','mas de $3.000.000'),
]
PRIMER_EMPLEO_CHOICES = [
    ('Entre 0 y 3 meses','Entre 0 y 3 meses'),
    ('Entre 3 y 6 meses','Entre 3 y 6 meses'),
    ('Entre 6 meses y 1 año','Entre 6 meses y 1 año'),
    ('Más de 1 año','Mas de 1 año'),
    ('Aún no encuentro mi primer empleo','Aún no encuentro mi primer empleo'),
]

CONTINUIDAD_ESTUDIOS_CHOICES = [
    ('Si','Sí'),
    ('No','No'),
    ('Actualmente me encuentro estudiando','Actualmente me encuentro estudiando'),
]

MOVILIDAD_UCN_CHOICES = [
    ('Sí','Sí'),
    ('No','No'),

]

OFERTA_ECIEM_CHOICES = [
    ('Magíster en Administración','Magíster en Administración'),
    ('Magíster en Ciencias Empresariales con Mención Emprendimiento','Magíster en Ciencias Empresariales con Mención Emprendimiento'),

]

INTERES_COLABORACION_CHOICES = [
    ('Sí','Sí'),
    ('No','No'),

]

TIPO_COLABORACION_CHOICES = [
    ('Ofrecer puestos de trabajo a egresados','Ofrecer puestos de trabajo a egresados'),
    ('Ofrecer beneficios/descuentos a egresados','Ofrecer beneficios/descuentos a egresados'),
    ('Impartir cursos o talleres sobre inserción laboral','Impartir cursos o talleres sobre inserción laboral'),
    ('Impartir cursos o talleres sobre alguna especialidad','Impartir cursos o talleres sobre alguna especialidad'),
    ('Organizar eventos para egresados','Organizar eventos para egresados'),
    ('Ninguna','Ninguna'),

]

AREAS_INTERES_CHOICES = [
    ('Administración','Administración'),
    ('Recursos humanos','Recursos humanos'),
    ('Marketing','Marketing'),
    ('Contabilidad','Contabilidad'),
    ('Finanzas','Finanzas'),
    ('Control de Gestión','Control de Gestión'),
    ('Análisis de datos','Análisis de datos'),
    ('TI (python, excel, R, Stata, Bizagi, entre otros)','TI (python, excel, R, Stata, Bizagi, entre otros)'),
]