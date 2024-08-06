from django.http import HttpResponse
from .models import Contribuyentes, Documento
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import reverse
from urllib.parse import quote
from io import BytesIO
import zipfile



# Create your views here.
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('principal'))  
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos'
            return render(request, self.template_name, {'error_message': error_message})

class Principal(View):
    def get(self, request):
        contribuyentes = Contribuyentes.objects.all()  # Obtener todos los contribuyentes
        return render(request, 'principal.html', {'contribuyentes': contribuyentes})
    
class RegistroClientes(View):
    def get(self, request):
        return render(request, 'registro.html')

    def post(self, request):
        try:
            # Obtener datos del formulario
            razonsocial = request.POST.get('razon_social')
            rfc = request.POST.get('rfc')
            codigopostal = request.POST.get('codigo_postal')
            tipopersona = request.POST.get('tipo_persona')
            regimenfiscal = request.POST.get('regimen_fiscal')
            contraseñafirma = request.POST.get('contraseña_firma')
            contraseñaimss = request.POST.get('contraseña_imss')
            contraseñainfonavit = request.POST.get('contraseña_infonavit')
            correoelectronico=request.POST.get('correo_electronico')

            # Crear una instancia del modelo y guardarla en la base de datos
            nuevo_contribuyente = Contribuyentes(
                RazonSocial=razonsocial,
                RFC=rfc,
                CodigoPostal=codigopostal,
                TipoPersona=tipopersona,
                RegimenFiscal=regimenfiscal,
                ContraseñaFirma=contraseñafirma,
                ContraseñaImss=contraseñaimss,
                ContraseñaInfonavit=contraseñainfonavit,
                correo_electronico=correoelectronico
            )
            nuevo_contribuyente.save()

            return redirect('principal')
        except Exception as e:
            return render(request, 'registro.html', {
                'error': 'Ups, hubo un error... ' + str(e)
            })

class GestionClientes(View):
    def get(self, request):
        contribuyentes = Contribuyentes.objects.all()
        return render(request, 'gestion.html', {'Contribuyentes': contribuyentes})

class EditarRegistro(View):
    def get(self, request, id):
        contribuyente = get_object_or_404(Contribuyentes, pk=id)
        return render(request, 'editar.html', {'contribuyente': contribuyente})

    def post(self, request, id):
        contribuyente = get_object_or_404(Contribuyentes, pk=id)
        contribuyente.RazonSocial = request.POST.get('razon_social')
        contribuyente.RFC = request.POST.get('rfc')
        contribuyente.CodigoPostal = request.POST.get('codigo_postal')
        contribuyente.TipoPersona = request.POST.get('tipo_persona')
        contribuyente.RegimenFiscal = request.POST.get('regimen_fiscal')
        contribuyente.ContraseñaFirma = request.POST.get('contraseña_firma')
        contribuyente.ContraseñaImss = request.POST.get('contraseña_imss')
        contribuyente.ContraseñaInfonavit = request.POST.get('contraseña_infonavit')
        contribuyente.correo_electronico=request.POST.get('correo_electronico')
        contribuyente.save()
        return redirect('gestion')
    
    
class GestionArchivos(View):
    def get(self, request):
        return render(request, 'archivos.html')

    def post(self, request):
        razon_social = request.POST['razon_social']
        contraseña = request.POST['contraseña']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_caducidad = request.POST['fecha_caducidad']

        documentos = Documento(
            razon_social=razon_social,
            contraseña=contraseña,
            fecha_inicio=fecha_inicio,
            fecha_caducidad=fecha_caducidad
        )

        for i in range(1, 6):
            archivo = request.FILES.get(f'archivo{i}')
            if archivo:
                setattr(documentos, f'archivo{i}', archivo)

        documentos.save()

        return redirect('principal')
    
    
class RevisionArchivos(View):
    def get(self, request):
        documentos = Documento.objects.all()  # Obtén todos los registros del modelo Documento
        return render(request, 'revision.html', {'documentos': documentos})


class DescargarArchivos(View):
    def get(self, request, documento_id):
        documento = get_object_or_404(Documento, id=documento_id)

        # Crea un archivo en memoria
        buffer = BytesIO()
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if documento.archivo1:
                zipf.writestr(f'Archivo1_{documento_id}.pdf', documento.archivo1.read())
            if documento.archivo2:
                zipf.writestr(f'Archivo2_{documento_id}.pdf', documento.archivo2.read())
            if documento.archivo3:
                zipf.writestr(f'Archivo3_{documento_id}.pdf', documento.archivo3.read())

        # Prepara la respuesta HTTP
        response = HttpResponse(buffer.getvalue(), content_type='application/zip')
        filename = f'Documentos_{documento_id}.zip'
        response['Content-Disposition'] = f'attachment; filename="{quote(filename)}"'
        return response
    
    
class EditarArchivo(View):
    def get(self, request, id):
        documento = get_object_or_404(Documento, pk=id)
        return render(request, 'editararchivo.html', {'documento': documento})
    
    def post(self, request, id):
        documento = get_object_or_404(Documento, pk=id)
        
        documento.razon_social = request.POST.get('razon_social', documento.razon_social)
        
        if 'archivo1' in request.FILES:
            documento.archivo1 = request.FILES['archivo1']
        if 'archivo2' in request.FILES:
            documento.archivo2 = request.FILES['archivo2']
        if 'archivo3' in request.FILES:
            documento.archivo3 = request.FILES['archivo3']
        
        documento.contraseña = request.POST.get('contraseña', documento.contraseña)
        documento.fecha_inicio = request.POST.get('fecha_inicio', documento.fecha_inicio)
        documento.fecha_caducidad = request.POST.get('fecha_caducidad', documento.fecha_caducidad)
        
        documento.save()
        return redirect('revision')
    


        
    
class Logout(View):
    def get(self, request):
        return redirect('/')