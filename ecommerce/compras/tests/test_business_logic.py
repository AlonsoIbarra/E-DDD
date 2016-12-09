import json
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from compras.models import OrdenCompra as OrdenCompraModel
from compras.business_logic import OrdenCompra


class OrdenCompraTest(TestCase):

    def setUp(self):
        products = json.dumps([
            [1, 1, 10.45],
            [2, 4, 10.35],
            [3, 10, 13.17]])

        # TODO: Cuando sea posible utilizar la capa logica para
        # crear una orden sin acceder al modelo, cambiar esto.
        self.pending_order = OrdenCompraModel.objects.create(
            fechaCompra=timezone.now(),
            idCliente=1,
            listaProductosOrden=products,
            status=1)

    def test_find_exising_order(self):
        """ Prueba que OrdenCompra.find funcione correctamente al pasarle el Id
        de una orden existente.
        """
        order = OrdenCompra.find(self.pending_order.id)

        self.assertIsInstance(order, OrdenCompra)
        self.assertEquals(order.OrdenCompra, self.pending_order)

    def test_find_non_existent_order(self):
        """ Prueba que OrdenCompra.find arroje la excepcion cuando
        se le da el ID de una orden que no existe.
        """
        with self.assertRaises(ObjectDoesNotExist):
            OrdenCompra.find(32)
