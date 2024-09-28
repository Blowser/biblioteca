# juegos/views.py
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login
import requests
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.http import HttpResponse



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
# PARA LAS APIS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
#API PROPIA
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@user_passes_test(es_superuser)
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

#PARA LA API CONSUMIDA DEL EJEMPLO COMIDAS   
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

#PARA LA API CONSUMIDA DE LA PÁGINA WEB RAWGIO
import requests
from django.shortcuts import render
#https://rawgthedocs.orels.sh/api/
#https://api.rawg.io/docs/

def proximos_lanzamientos(request):
    url = 'https://api.rawg.io/api/games'
    params = {
        'key': '9fe0cbc8cbbe416ca00a5a0f7356d8fe',  # Aquí mi API key de RAWG, Free 2000 request por período
        'platforms': 4,  # PC (el ID de la plataforma PC es 4: #https://api.rawg.io/api/platforms?key=9fe0cbc8cbbe416ca00a5a0f7356d8fe
        'dates': '2024-09-26,2024-12-31',  # Fechas para los próximos lanzamientos #https://api.rawg.io/docs/#operation/games_list
        'ordering': 'released' #https://api.rawg.io/docs/#operation/games_list
    }

    response = requests.get(url, params=params)

    # Verificar si la respuesta es exitosa
    if response.status_code == 200:
        data = response.json()
        juegos = data['results']  # Aquí están los juegos obtenidos
    else:
        juegos = []

    # Renderizar el template con la lista de juegos
    return render(request, 'juegos/proximos_lanzamientos.html', {'juegos': juegos})

def detalle_juego(request, juego_id):
    url = f'https://api.rawg.io/api/games/{juego_id}'
    params = {
        'key': '9fe0cbc8cbbe416ca00a5a0f7356d8fe'  
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        juego = response.json()  # Datos del juego
    else:
        juego = None  # En caso de error

    return render(request, 'juegos/detalle_juego.html', {'juego': juego})


from rest_framework import viewsets
from .serializers import PedidoSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pedido, Producto
from .forms import PedidoForm
# ViewSet para el modelo Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Recuperar todos los productos de la base de datos
    serializer_class = ProductoSerializer  # Usar el serializador definido para Producto
    permission_classes = [IsAuthenticated]  # Requiere que el usuario esté autenticado para acceder

# ViewSet para el modelo Pedido
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()  # Recuperar todos los pedidos
    serializer_class = PedidoSerializer  # Usar el serializador definido para Pedido
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder a este ViewSet

    # Sobrescribimos el método "perform_create" para asignar el usuario logueado
    def perform_create(self, serializer):
        # Asignamos el usuario autenticado al pedido
        serializer.save(usuario=self.request.user)
        
# Vista para listar los pedidos

class ListaPedidosView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'juegos/lista_pedidos.html'
    context_object_name = 'pedidos'
    login_url = 'iniciar_sesion'  # Redirecciona a la página de login si no está autenticado

# Vista para crear un nuevo pedido
class CrearPedidoView(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'juegos/crear_pedido.html'
    success_url = reverse_lazy('lista_pedidos')

    def form_valid(self, form):
        # Asignar el usuario autenticado al pedido
        form.instance.usuario = self.request.user

        # Buscar el producto seleccionado por su ID desde el formulario
        producto_id = self.request.POST.get('producto')
        if producto_id:
            form.instance.producto = Producto.objects.get(id=producto_id)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()  # Pasar productos al contexto
        return context

    def form_valid(self, form):
        print(form.cleaned_data)  # Verificar los datos que se están enviando
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Esto mostrará los errores del formulario si los hay
        return super().form_invalid(form)


# Vista para editar un pedido existente
class EditarPedidoView(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'juegos/editar_pedido.html'
    success_url = reverse_lazy('lista_pedidos')
    login_url = 'iniciar_sesion'

# Vista para eliminar un pedido existente
class EliminarPedidoView(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = 'juegos/eliminar_pedido.html'
    success_url = reverse_lazy('lista_pedidos')
    login_url = 'iniciar_sesion'
    
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer