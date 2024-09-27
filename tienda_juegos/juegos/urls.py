# juegos/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import productos_api
from .views import detalle_categoria
urlpatterns = [#html, luego nombre funcion, finalmente name, el name para llamar en los htmls
               
    path('', views.index, name='index'),
    path('vercatalogo/', views.ver_catalogo, name='ver_catalogo'),
    path('accion/', views.categoria_accion, name='categoria_accion'),
    path('mundoabierto/', views.categoria_mundo_abierto, name='categoria_mundo_abierto'),
    path('freetoplay/', views.categoria_free_to_play, name='categoria_free_to_play'),
    path('supervivencia/', views.categoria_supervivencia, name='categoria_supervivencia'),
    path('carrerasydeportes/', views.categoria_carreras_deportes, name='categoria_carreras_y_deportes'),
    
    #paths de login y formularios
    # Login y autenticación
    path('iniciarsesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarcuenta/', views.registrar_cuenta, name='registrar_cuenta'),
    path('modificarperfil/', views.modificar_perfil, name='modificar_perfil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    #paths de recuperación de contraseña:
    path('recuperarcontrasena/', auth_views.PasswordResetView.as_view(template_name='juegos/recuperarcontrasena.html'), name='password_reset'),
    path('recuperarcontrasena/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='juegos/recuperarcontrasenadone.html'), name='password_reset_done'),
    path('recuperarcontrasena/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperarcontrasenaconfirm.html'), name='password_reset_confirm'),
    path('recuperarcontrasena/completo/', auth_views.PasswordResetCompleteView.as_view(template_name='juegos/recuperarcontrasenacomplete.html'), name='password_reset_complete'),

 


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
    
    #paths CRUD
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<str:sku>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<str:sku>/', views.eliminar_producto, name='eliminar_producto'),
    
    
    #para el carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<str:producto_sku>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<str:producto_sku>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('carrito/actualizar/<str:producto_sku>/', views.actualizar_cantidad_carrito, name='actualizar_cantidad_carrito'),
    
    #PARA LA API CONSUMIDA DE EJEMPLO  DE COMIDAS 
    path('categorias-comida/', views.listar_categorias_comida, name='listar_categorias_comida'),
    path('categoria/<str:categoria_nombre>/', detalle_categoria, name='detalle_categoria'),
    #PARA LA APIREST PROPIA 
    path('api/productos/', views.productos_api, name='productos_api'),
    path('api/productos/<int:pk>/', productos_api, name='producto_detalle'),
    
    #PARA LA API CONSUMIDA PROPIA DE LA PÁGINA RAWGIO
    path('proximos-lanzamientos/', views.proximos_lanzamientos, name='proximos_lanzamientos'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),


]
