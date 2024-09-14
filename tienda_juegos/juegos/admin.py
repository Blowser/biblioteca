from django.contrib import admin
from .models import Producto, Categoria, AñoDesarrollo, Desarrollador, Editor, Restriccion

# Registrar cada modelo en el panel de administración
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(AñoDesarrollo)
admin.site.register(Desarrollador)
admin.site.register(Editor)
admin.site.register(Restriccion)
