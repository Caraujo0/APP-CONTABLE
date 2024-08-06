from django.db import models

TIPOPERSONA_CHOICES=(
    (1, 'PERSONA FÍSICA'),
    (2, 'PERSONA MORAL')
)

REGIMEN_CHOICES=(
    (1, 'SUELDOS Y SALARIOS E INGRESOS ASIMILADOS A SALARIOS'),
    (2, 'ARRENDAMIENTO'),
    (3, 'RÉGIMEN DE ENAJENACIÓN O ADQUISICIÓN DE BIENES'),
    (4, 'DEMAS INGRESOS'),
    (5, 'RESIDENTES EN EL EXTRANJERO SIN ESTABLECIMIENTO PERMANENTE EN MÉXICO'),
    (6, 'INGRESOS POR DIVIDIENDOS (SOCIOS Y ACCIONISTAS)'),
    (7, 'PERSONAS FÍSICAS CON ACTIVIDADES EMPRESARIALES Y PROFESIONALES'),
    (8, 'INGRESOS POR INTERESES'),
    (9, 'RÉGIMEN DE LOS INGRESOS POR OBTENCIÓN DE PREMIOS'),
    (10, 'SIN OBLIGACIONES FISCALES'),
    (11, 'INCORPORACIÓN FISCAL'),
    (12, 'REGIMEN DE LAS ACTIVIDADES EMPRESARIALES CON INGRESOS A TRAVES DE PLATAFORMAS TECNOLÓGICAS'),
    (13, 'RÉGIMEN SIMPLIFICADO DE CONFIANZA'),
    (14, 'GENERAL DE LEY DE PERSONAS MORALES'),
    (15, 'RÉGIMEN DE PERSONAS MORALES CON FINES NO LUCRATIVOS'),
    (16, 'CONSOLIDACIÓN'),
    (17, 'SOCIEDADES COOPERATIVAS DE PRODUCCIÓN QUE OPTAN POR DIFERIR SUS INGRESOS'),
    (18, 'ACTIVIDADES AGRÍCOLAS, GANADERAS, SILVÍCOLAS Y PESQUERAS'),
    (19, 'COORDINADOS')
)


# Create your models here.
class Contribuyentes(models.Model):
    RazonSocial=models.CharField(max_length=100)
    RFC=models.CharField(max_length=13)
    CodigoPostal=models.CharField(max_length=5)
    TipoPersona=models.PositiveSmallIntegerField(choices=TIPOPERSONA_CHOICES,default=1)
    RegimenFiscal=models.PositiveSmallIntegerField(choices=REGIMEN_CHOICES,default=1)
    ContraseñaFirma=models.CharField(max_length=100)
    ContraseñaImss=models.CharField(max_length=100)
    ContraseñaInfonavit=models.CharField(max_length=100)
    correo_electronico = models.EmailField(default='default@example.com')  # Agrega esto con un valor por defecto



class Documento(models.Model):
    razon_social = models.CharField(max_length=255)
    archivo1 = models.FileField(upload_to='archivos/')
    archivo2 = models.FileField(upload_to='archivos/')
    archivo3 = models.FileField(upload_to='archivos/')
    contraseña = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_caducidad = models.DateField()

   
