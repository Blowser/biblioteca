# juegos/urls.py
from django.urls import path
from . import views

urlpatterns = [#html, luego nombre funcion, finalmente name, el name para llamar en los htmls
               
    path('', views.index, name='index'),
    path('vercatalogo/', views.ver_catalogo, name='ver_catalogo'),
    path('iniciarsesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('accion/', views.categoria_accion, name='categoria_accion'),
    path('mundoabierto/', views.categoria_mundo_abierto, name='categoria_mundo_abierto'),
    path('freetoplay/', views.categoria_free_to_play, name='categoria_free_to_play'),
    path('supervivencia/', views.categoria_supervivencia, name='categoria_supervivencia'),
    path('carrerasydeportes/', views.categoria_carreras_deportes, name='categoria_carreras_y_deportes'),
    
    #paths para el catálogo
    path('detalles/elderscroll/', views.detalles_elderscroll, name='detalles_elderscroll'),
    path('detalles/fc24/', views.detalles_fc24, name='detalles_fc24'),
    path('detalles/ark/', views.detalles_ark, name='detalles_ark'),
    path('detalles/gtav/', views.detalles_gtav, name='detalles_gtav'),
    path('detalles/cs2/', views.detalles_cs2, name='detalles_cs2'),
    path('detalles/lostark/', views.detalles_lostark, name='detalles_lostark'),
    path('detalles/dota2/', views.detalles_dota2, name='detalles_dota2'),
    path('detalles/palworld/', views.detalles_palworld, name='detalles_palworld'),
    path('detalles/eldenring/', views.detalles_eldenring, name='detalles_eldenring'),
    path('detalles/rocketleague/', views.detalles_rocketleague, name='detalles_rocketleague'),
    
    
    #paths para los formularios:
    path('registrarcuenta/', views.registrar_cuenta, name='registrar_cuenta'),
    path('modificarperfil/', views.modificar_perfil, name='modificar_perfil'),
    path('recuperarcontrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
]




