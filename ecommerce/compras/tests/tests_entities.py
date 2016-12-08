from django.test import TestCase
from compras.models import Carrito, Producto, OrdenCompra
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
