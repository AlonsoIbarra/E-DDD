from django.test import TestCase
from compras.models import Carrito, Producto
import json

# Create your tests here.


class TestProduct(TestCase):

    def test_saveListProduct(self):
        lstProductos = [[10, 9999.99], [20, 9999.92], [20, 9999.99]]
        carrito = Carrito.objects.create(
            idCliente=1,
            listaProductos=json.dumps(lstProductos),
            total=99999.99
        )

        objCarrito = Carrito.objects.get(pk=carrito.id)
        listaProducto = json.loads(objCarrito.listaProductos)
        self.assertEquals(listaProducto, lstProductos)

class TestListarProductos(TestCase):
    def test_mostrarListaProductos(self):
        producto1 = Producto.objects.create(
            nombre = 'Computadora',
            descripcion = 'Escritorio 13 plugadas, memoria RAM',
            marca = 'HP',
            precio = 9999.99,
        )
        producto2 = Producto.objects.create(
            nombre = 'Teclado',
            descripcion = 'Inalambrico',
            marca = 'ACER',
            precio = 400
        )
        producto3 = Producto.objects.create(
            nombre = 'Memoria USB',
            descripcion = 'Capacidad 16G',
            marca = 'Kin',
            precio = 400
        )
        self.assertEquals(
            list(Producto.objects.all()),
            [producto1,producto2,producto3]
        )
