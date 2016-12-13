import json
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from compras.models import OrdenCompra as EntityOrdenCompra, \
    Producto as EntityProducto
from compras.business_logic import PurchaseOrder, Carrito


class OrdenCompraTest(TestCase):

    def setUp(self):
        Carrito(1)  # Crea un carrito para que no falle al crear un PurchaseOrder
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

        # TODO: Cuando sea posible utilizar la capa logica para
        # crear una orden sin acceder al modelo, cambiar esto.
        self.pending_order = EntityOrdenCompra.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=1)

    def test_find_exising_order(self):
        """ Prueba que OrdenCompra.find funcione correctamente al pasarle el Id
        de una orden existente.
        """
        order = PurchaseOrder.find(self.pending_order.id)
        self.assertIsInstance(order, PurchaseOrder)
        self.assertEqual(order.OrdenCompra, self.pending_order)

    def test_find_non_existent_order(self):
        """ Prueba que OrdenCompra.find arroje la excepcion cuando
        se le da el ID de una orden que no existe.
        """
        with self.assertRaises(ObjectDoesNotExist):
            PurchaseOrder.find(32)

    def test_products(self):
        """ Prueba que dada una OrdenCompra pueda obtener la información de sus
        productos en un dict (a menos hasta que exista capa lógica de Producto)
        """
        order = PurchaseOrder.find(self.pending_order.id)

        products = order.products()
        self.assertEqual(2, len(products))
        self.assertEqual(products[0]['nombre'], self.p1.nombre)
        self.assertEqual(products[0]['descripcion'], self.p1.descripcion)
        self.assertEqual(products[0]['cantidad'], 1)
        self.assertEqual(products[0]['precio'], 10.45)
