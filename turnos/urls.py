from django.urls import path
from . import views

urlpatterns = [
    path('', views.generar_turno, name='registro'),
    path('espera/', views.pantalla_espera, name='espera'),
    path('panel/', views.panel_atencion, name='panel'),
]
