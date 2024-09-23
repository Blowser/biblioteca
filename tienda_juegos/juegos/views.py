# juegos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login



# para el index
def index(request):
    return render(request, 'juegos/index.html')


def ver_catalogo(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'juegos/vercatalogo.html', {'productos': productos})


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
            # Redirigir a listar_productos si es superusuario
            if user.is_superuser:
                return redirect('listar_productos')
            # Si es un usuario normal, redirigir a la página principal
            return redirect('modificar_perfil')
        else:
            # Si las credenciales no son válidas, mostrar error
            return render(request, 'juegos/iniciarsesion.html', {'error': 'Credenciales inválidas'})  
    return render(request, 'juegos/iniciarsesion.html')  




def registrar_cuenta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()  # Guardar los campos adicionales
            messages.success(request, 'Cuenta creada exitosamente. ¡Ahora puedes iniciar sesión!')
            return redirect('iniciar_sesion')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = UserCreationForm()
    return render(request, 'juegos/registrarcuenta.html', {'form': form})




@login_required
def modificar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('modificar_perfil')
    
    return render(request, 'juegos/modificarperfil.html')

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

def es_superuser(user):
    return user.is_superuser

@user_passes_test(es_superuser)
@login_required
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'juegos/listar_productos.html', {'productos': productos})

@user_passes_test(es_superuser)
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'juegos/crear_producto.html', {'form': form})

@user_passes_test(es_superuser)
@login_required
def editar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'juegos/editar_producto.html', {'form': form})

@user_passes_test(es_superuser)
@login_required
def eliminar_producto(request, sku):
    producto = get_object_or_404(Producto, sku=sku)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'juegos/eliminar_producto.html', {'producto': producto})



# VISTAS PARA EL CARRITO

@login_required
def agregar_al_carrito(request, producto_sku):
    producto = get_object_or_404(Producto, sku=producto_sku)  # Cambia de 'id' a 'sku'
    carrito = request.session.get('carrito', {})
    
    # Convertimos el SKU a string para usarlo como clave en el carrito
    producto_sku_str = str(producto.sku)
    
    # Verificamos si el producto ya está en el carrito
    if producto_sku_str in carrito:
        carrito[producto_sku_str]['cantidad'] += 1
    else:
        carrito[producto_sku_str] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1,
        }
    
    # Guardamos el carrito en la sesión
    request.session['carrito'] = carrito
    return redirect('ver_catalogo')

@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'juegos/ver_carrito.html', {'carrito': carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, producto_sku):
    producto_sku_str = str(producto_sku)
    carrito = request.session.get('carrito', {})
    
    if producto_sku_str in carrito:
        del carrito[producto_sku_str]
    
    # Guardamos el carrito actualizado en la sesión
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

@login_required
def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad_carrito(request, producto_sku):
    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        carrito = request.session.get('carrito', {})
        producto_sku_str = str(producto_sku)

        if producto_sku_str in carrito:
            if nueva_cantidad > 0:
                carrito[producto_sku_str]['cantidad'] = nueva_cantidad
            else:
                del carrito[producto_sku_str]  # Elimina el producto si la cantidad es 0

        request.session['carrito'] = carrito
    return redirect('ver_carrito')
# PARA LA API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def productos_api(request, pk=None):
    
    # Manejar solicitud GET para un producto específico o todos los productos
    if request.method == 'GET':
        if pk:
            producto = get_object_or_404(Producto, pk=pk)
            serializer = ProductoSerializer(producto)
        else:
            productos = Producto.objects.all()
            serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    # Manejar solicitud POST para crear un nuevo producto
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Manejar solicitud PUT para actualizar un producto existente
    elif request.method == 'PUT':
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Manejar solicitud DELETE para eliminar un producto
    elif request.method == 'DELETE':
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
import requests
from django.core.cache import cache
def listar_categorias_comida(request):
    # Intentar obtener las categorías desde el caché
    categorias = cache.get('categorias_comida')

    if not categorias:
        # Si las categorías no están en caché, hacer la solicitud a la API
        url = "https://www.themealdb.com/api/json/v1/1/categories.php"
        response = requests.get(url)
        data = response.json()

        # Extraer las categorías de la respuesta
        categorias = data['categories']

        # Guardar las categorías en el caché con un timeout de 1 hora (3600 segundos)
        cache.set('categorias_comida', categorias, timeout=60 * 60)

    # Renderizar la plantilla con las categorías obtenidas
    return render(request, 'juegos/listar_categorias_comida.html', {'categorias': categorias})
from django.core.paginator import Paginator

def detalle_categoria(request, categoria_nombre):
    # URL para obtener las comidas de la categoría
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={categoria_nombre}"
    response = requests.get(url)
    data = response.json()
    
    # Obtener las comidas de la categoría
    comidas = data['meals']
    
    # Configurar el paginador: 6 comidas por página
    paginator = Paginator(comidas, 6) 
    page_number = request.GET.get('page')  # Obtener el número de página desde la URL
    page_obj = paginator.get_page(page_number)  # Obtener la página actual

    # Renderizar la plantilla con el objeto de la página actual
    return render(request, 'juegos/detalle_categoria.html', {'page_obj': page_obj, 'categoria': categoria_nombre})