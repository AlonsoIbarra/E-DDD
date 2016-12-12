import json
from django.test import TestCase
from django.utils import timezone
from compras.models import OrdenCompra, Producto

# Create your tests here.


class OrdenCompraTest(TestCase):

    def setUp(self):
        products = json.dumps([[1, 10.45], [2, 10.35], [3, 13.17]])

        self.pending_order = OrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=1)

        self.canceled_order = OrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=2)

        self.paid_order = OrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=0)

    def test_view_order(self):
        response = self.client.get('/orders/1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')

        # Orden pagada no tiene boton pagar
        # Orden cancelada no tiene boton pagar
        # Orden pendiente tiene boton pagar
        # El total mostrado coincide con la suma del total de los productos


class ProductoTest(TestCase):
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

class TestCarrito(TestCase):
    def TestCarritoTemplate(self):
        request = self.client.get('/orders/agregarProductoCarrito/1/6')
        self.assertTemplateUsed(response, 'detalles_producto.html')
