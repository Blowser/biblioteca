from django.db import models

# Modelo de Año de Desarrollo
class AñoDesarrollo(models.Model):
    año = models.IntegerField(unique=True)  # El año será único, pero Django generará el campo 'id' automáticamente

    def __str__(self):
        return str(self.año)

# Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Modelo de Restricción
class Restriccion(models.Model):
    tipo = models.CharField(max_length=50)  # Ejemplo: "Edad", "Región", etc.
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo

# Modelo de Desarrollador
class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Modelo de Editor
class Editor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Modelo de Producto (con SKU como clave primaria)
class Producto(models.Model):
    sku = models.CharField(max_length=20, primary_key=True)  # Clave primaria manual
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con Categoría
    añodesarrollo = models.ForeignKey(AñoDesarrollo, on_delete=models.CASCADE)  # Relación con Año de Desarrollo
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)  # Relación con Desarrollador
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)  # Relación con Editor
    restriccion = models.ForeignKey(Restriccion, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con Restricción

    def __str__(self):
        return self.nombre

