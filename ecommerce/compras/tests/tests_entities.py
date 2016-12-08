from django.test import TestCase
<<<<<<< HEAD
from compras.models import Carrito, Producto, OrdenCompra
=======
from compras.models import Carrito, Producto
>>>>>>> 05b81a52e926c1d1ebc60b836fa810b374f2fda4
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

<<<<<<< HEAD
    def test_saveProducto(self):
        producto = Producto.objects.create(
            nombre  = "Camisa",
            descripcion = "Camisa blanca tipo polo tamaño regular",
            marca = "Polo",
            precio = 540.50
            
        )

        objProducto = Producto.objects.get(pk=producto.id)

        self.assertEquals(producto, objProducto)

    def test_OrdenCompra(self):
        lstProductos = [[10, 9999.99], [20, 9999.92], [20, 9999.99]]
        ordenCompra = OrdenCompra.objects.create(
            idCliente = 1,
            listaProductosOrden = json.dumps(lstProductos),
            status = 0            
        )

        objOrdenCompras = OrdenCompra.objects.get(pk=ordenCompra.id)
        listaProductosOrden = json.loads(objOrdenCompras.listaProductosOrden)
        
        self.assertEquals(lstProductos, listaProductosOrden)
=======
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
>>>>>>> 05b81a52e926c1d1ebc60b836fa810b374f2fda4
