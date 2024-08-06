from django.urls import path
from . import views
from .views import LoginView
from .views import *
from .views import Logout  # Asegúrate de importar la vista Logout



urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('principal/', Principal.as_view(), name='principal'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registro/', RegistroClientes.as_view(), name='registro'),
    path('gestion/', GestionClientes.as_view(), name='gestion'),
    path('archivos/', GestionArchivos.as_view(), name='archivo'),
    path('editar/<int:id>/', EditarRegistro.as_view(), name='editar'),
    path('revision/', RevisionArchivos.as_view(), name='revision'),  # Nueva ruta
    path('descargar_archivos/<int:documento_id>/', DescargarArchivos.as_view(), name='descargar_archivos'),
    path('editararchivo/<int:id>/', EditarArchivo.as_view(), name='editararchivo'),
]

