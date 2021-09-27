from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializers, MarcaSerializers

# Create your views here.

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializers

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')
        
        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        
        return productos
        # return super().get_queryset()

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

# @login_required
def galeria(request):
    return render(request, 'app/galeria.html')

@permission_required('app.add_producto')
def agregar_producto(req):
    data = {
        'form': ProductoForm()
    }
    if req.method == 'POST':
        formulario = ProductoForm(data=req.POST, files=req.FILES)
        if formulario.is_valid():
            formulario.save()
            # data["mensaje"] = "Guardado correctamente"
            messages.success(req, "Creado correctamente")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(req, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(req):
    productos = Producto.objects.all()
    page = req.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(req, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def editar_producto(req, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if req.method == 'POST':
        formulario = ProductoForm(
            data=req.POST, instance=producto, files=req.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(req, "Modificado correctamente")
            # data["mensaje"] = "Editado correctamente"
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(req, 'app/producto/editar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(req, id):
    producto = get_object_or_404(Producto, id=id)
    if producto:
        producto.delete()
        messages.success(req, "Eliminado correctamente")
    return redirect(to="listar_productos")

def registro(req):
    data = {
        'form': CustomUserCreationForm
    }
    if req.method == 'POST':
        formulario = CustomUserCreationForm(data=req.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(req, user)
            messages.success(req, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(req, 'registration/registro.html', data)
