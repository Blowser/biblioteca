# juegos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# para el index
def index(request):
    return render(request, 'juegos/index.html')

def ver_catalogo(request):
    return render(request, 'juegos/vercatalogo.html')

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

# para los formularios

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página principal 
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'juegos/iniciarsesion.html')



def registrar_cuenta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. ¡Ahora puedes iniciar sesión!')
            return redirect('login')  # Redirigir al login después de registrar
    else:
        form = UserCreationForm()
    return render(request, 'juegos/registrarcuenta.html', {'form': form})


@login_required
def modificar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        # Puedes agregar más campos personalizados como teléfono o dirección si tienes los modelos correctos
        # user.telefono = request.POST.get('telefono', '')
        # user.direccion = request.POST.get('direccion', '')
        user.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('modificar_perfil')
    return render(request, 'juegos/modificarperfil.html', {'user': request.user})

def recuperar_contrasena(request):
    return render(request, 'juegos/recuperarcontrasena.html')


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



