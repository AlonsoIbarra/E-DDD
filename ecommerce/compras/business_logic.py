from compras import models

class Carrito():


    def __init__(self, pIdCliente):
        self.idCliente = pidCliente
        self.listaProductos = []

    def agregarProducto(self, pProducto, pCantidad, pPrecio):
        self.listaProductos.append([pProducto.id, pCantidad, pPrecio])

    def calcularTotal(self):
        sCantidad = 0
        sprecio = 0
        for id, cantidad, precio in self.listaProductos:
            sCantidad += cantidad
            sprecio += precio


class OrdenCompra():
    def __init__(self, pCarrito=None):
        self.OrdenCompra = None

        if pCarrito:
            self.OrdenCompra = models.OrdenCompra(
                idCliente=pCarrito.idCliente,
                status=1,
                listaProductosOrden=pCarrito.listaProductos)

    def mostrarDetalle(self):
        return self.OrdenCompra

    @staticmethod
    def find(order_id):
        """ Dado el ID de una orden, la busca en la base de datos y la envuelve
        en una instancia business_logic.OrdenCompra.
        """
        order = OrdenCompra()
        order.OrdenCompra = models.OrdenCompra.objects.get(id=order_id)

        return order
