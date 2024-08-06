from django.contrib import admin
from .models import Contribuyentes
from .models import Documento

class ContribuyentesAdmin(admin.ModelAdmin):
    list_display = ['id','RazonSocial', 'RFC', 'CodigoPostal', 'TipoPersona', 'RegimenFiscal','ContraseñaFirma','ContraseñaImss','ContraseñaInfonavit','correo_electronico']
    search_fields = ['id']
    
class DocumentoAdmin(admin.ModelAdmin):
    list_display=['id', 'razon_social', 'archivo1', 'archivo2', 'archivo3', 'contraseña', 'fecha_inicio', 'fecha_caducidad']
    search_fields=['id']
 

admin.site.register(Contribuyentes, ContribuyentesAdmin)
admin.site.register(Documento, DocumentoAdmin)
