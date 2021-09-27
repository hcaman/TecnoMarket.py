from django.urls import path, include
from .views import home, contacto, galeria, agregar_producto, listar_productos, editar_producto, eliminar_producto, registro, ProductoViewSet, MarcaViewSet, error_facebook
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('marca', MarcaViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('editar-producto/<id>/', editar_producto, name="editar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('error-facebook/', error_facebook, name="error_facebook"),
    path('api/', include(router.urls)),
]
