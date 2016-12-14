import json
from django.db.models import Q
from django.test import TestCase
from django.conf import settings
from django.utils import timezone, dateformat, html

from compras.business_logic import PurchaseOrder
from compras.models import Producto
from compras.models import \
    OrdenCompra as EntityOrdenCompra, \
    Producto as EntityProducto

# Create your tests here.


class OrdenCompraTest(TestCase):

    def setUp(self):
        self.p1 = EntityProducto.objects.create(
            nombre='Tesla Model X',
            descripcion='Auto que se conduce solo',
            marca='Tesla Motors',
            precio=34.50)

        self.p2 = EntityProducto.objects.create(
            nombre='iPhone',
            descripcion='iPhone nuevo plus',
            marca='Apple',
            precio=14.30)

        products = json.dumps([
            [self.p1.id, 1, 10.45],
            [self.p2.id, 4, 10.35]])

        self.pending_order = EntityOrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=1)

        self.canceled_order = EntityOrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=2)

        self.paid_order = EntityOrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=0)

    def test_view_order(self):
        """
        Prueba que el usuario vea los detalles de la orden
        de compra correctamente.
        """
        response = self.client.get('/orders/{}'.format(self.pending_order.id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')

        formated_date = dateformat.format(
            self.pending_order.fechaCompra,
            settings.DATE_FORMAT)

        # Probamos que la página muestre el status, la fecha e Id de la orden
        self.assertTrue('order' in response.context)
        self.assertContains(response, 'Pendiente')
        self.assertContains(
            response,
            html.escape(self.pending_order.idOrdenCompra))
        self.assertContains(
            response,
            html.escape(formated_date))

        # Probamos que los productos vengan listados en la página
        order = PurchaseOrder.find(self.pending_order.id)

        for product in order.products():
            self.assertContains(response, product['nombre'])
            self.assertContains(response, product['descripcion'])
            self.assertContains(response, product['cantidad'])
            self.assertContains(response, product['precio'])

        # Probamos que el botón de "Pagar Orden" se despliegue
        self.assertContains(response, 'Pagar Orden')

    def test_view_canceled_order(self):
        """ Prueba que al ver el detalle de la orden que ya esta cancelada, no
        aparezca ningún botón para pagarla.
        """
        response = self.client.get('/orders/{}'.format(self.canceled_order.id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')

        self.assertNotContains(response, 'Pagar Orden')

    def test_view_paid_order(self):
        """ Prueba que al ver el detalle de la orden que ya esta pagada, no
        aparezca ningún botón para pagarla.
        """
        response = self.client.get('/orders/{}'.format(self.paid_order.id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')

        self.assertNotContains(response, 'Pagar Orden')


class ProductoTest(TestCase):
    def test_mostrarListaProductos(self):
        producto1 = Producto.objects.create(
            nombre='Computadora 1',
            descripcion='Escritorio 13 plugadas, memoria RAM',
            marca='HP',
            precio=9999.99,
        )
        producto2 = Producto.objects.create(
            nombre='Teclado',
            descripcion='Inalambrico 1',
            marca='ACER',
            precio=400
        )
        producto3 = Producto.objects.create(
            nombre='Memoria USB',
            descripcion='Capacidad 16G RAM',
            marca='Kin',
            precio=400
        )

        self.assertEquals(
            list(Producto.objects.all()),
            [producto1, producto2, producto3]
        )

        consulta='RAM'
        resultado=Producto.objects.filter(Q(descripcion__icontains=consulta) | Q(descripcion__icontains=consulta))

        self.assertEquals(
             resultado[0].nombre,
            'Computadora 1'
        )
        self.assertEquals(
            resultado[1].nombre,
            'Memoria USB'
        )


class TestCarrito(TestCase):
    def TestCarritoTemplate(self):
        request = self.client.get('/orders/agregarProductoCarrito/1/6')
        self.assertTemplateUsed(request, 'product_list.html')
