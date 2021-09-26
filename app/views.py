from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


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


def galeria(request):
    return render(request, 'app/galeria.html')


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


def eliminar_producto(req, id):
    producto = get_object_or_404(Producto, id=id)
    if producto:
        producto.delete()
        messages.success(req, "Eliminado correctamente")
    return redirect(to="listar_productos")
