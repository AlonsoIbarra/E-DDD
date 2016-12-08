from django.test import TestCase
from compras.models import Carrito
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
