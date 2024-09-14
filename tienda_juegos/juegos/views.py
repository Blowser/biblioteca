# juegos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
# para el index
def index(request):
    return render(request, 'juegos/index.html')

def ver_catalogo(request):
    return render(request, 'juegos/vercatalogo.html')

def iniciar_sesion(request):
    return render(request, 'juegos/iniciarsesion.html')

def categoria_accion(request):
    return render(request, 'juegos/accion.html')

def categoria_mundo_abierto(request):
    return render(request, 'juegos/mundoabierto.html')

def categoria_free_to_play(request):
    return render(request, 'juegos/freetoplay.html')

def categoria_supervivencia(request):
    return render(request, 'juegos/supervivencia.html')

def categoria_carreras_deportes(request):
    return render(request, 'juegos/carrerasydeportes.html')


# para el catalogo
def detalles_elderscroll(request):
    return render(request, 'juegos/detalleselderscroll.html')

def detalles_fc24(request):
    return render(request, 'juegos/detallesfc24.html')

def detalles_ark(request):
    return render(request, 'juegos/detallesark.html')

def detalles_gtav(request):
    return render(request, 'juegos/detallesgtav.html')

def detalles_cs2(request):
    return render(request, 'juegos/detallescs2.html')

def detalles_lostark(request):
    return render(request, 'juegos/detalleslostark.html')

def detalles_dota2(request):
    return render(request, 'juegos/detallesdota2.html')

def detalles_palworld(request):
    return render(request, 'juegos/detallespalworld.html')

def detalles_eldenring(request):
    return render(request, 'juegos/detalleseldenring.html')

def detalles_rocketleague(request):
    return render(request, 'juegos/detallesrocketleague.html')

# para los formularios
def registrar_cuenta(request):
    return render(request, 'juegos/registrarcuenta.html')

def modificar_perfil(request):
    return render(request, 'juegos/modificarperfil.html')

def recuperar_contrasena(request):
    return render(request, 'juegos/recuperarcontrasena.html')


# para el CRUD
# Vista para listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'juegos/listar_productos.html', {'productos': productos})

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'juegos/crear_producto.html', {'form': form})

# Vista para editar un producto
def editar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'juegos/editar_producto.html', {'form': form, 'producto': producto})

# Vista para eliminar un producto
def eliminar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'juegos/eliminar_producto.html', {'producto': producto})



