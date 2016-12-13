import json
from django.db.models import Q
from django.test import TestCase
from django.conf import settings
from django.utils import timezone, dateformat, html

from compras.business_logic import OrdenCompra
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

        # los productios a los que hace referencia la orden deben estar creados

        formated_date = dateformat.format(
            self.pending_order.fechaCompra,
            settings.DATE_FORMAT)

        self.assertTrue('order' in response.context)
        self.assertContains(response, 'Estado: Pendiente')
        self.assertContains(
            response,
            html.escape(self.pending_order.idOrdenCompra))
        self.assertContains(
            response,
            html.escape('Fecha compra: {}'.format(formated_date)))

        # Revisar que los productos vengan listados
        order = OrdenCompra.find(self.pending_order.id)

        for product in order.products():
            self.assertContains(response, product['nombre'])
            self.assertContains(response, product['descripcion'])
            self.assertContains(response, product['cantidad'])
            self.assertContains(response, product['precio'])

        # Orden pagada no tiene boton pagar
        # Orden cancelada no tiene boton pagar
        # Orden pendiente tiene boton pagar
        # El total mostrado coincide con la suma del total de los productos


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
