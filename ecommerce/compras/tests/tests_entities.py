from django.test import TestCase
from compras.models import Carrito

# Create your tests here.
class TestProduct(TestCase):
    def test_saveListProduct(self):
        lstProductos=[[10,9999.99],[20,9999.92],[20,9999.99]]
        carrito = Carrito.objects.create(
            idCliente=1,
            listaProductos=lstProductos,
            total=99999.99
        )


        objCarrito = Carrito.objects.get(pk = carrito.id)
        self.assertEquals(objCarrito.listaProductos.to_python(),lstProductos);
