import json
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

    def products(self):
        """ Obtiene una lista de diccionarios (para más facil accesso) donde
        cada uno contiene la información general de un producto para ser
        presentado en el detalle de la orden.

        Cada diccionario en la lista tiene las llaves: 'nombre', 'descripcion',
        'cantidad' y 'precio.
        """
        products = []
        lista_productos = json.loads(self.OrdenCompra.listaProductosOrden)
        for product in lista_productos:
            producto = models.Producto.objects.get(id=product[0])
            cantidad = product[1]
            precio = product[2]

            products.append({
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'cantidad': cantidad,
                'precio': precio
            })

        return products

    @staticmethod
    def find(order_id):
        """ Dado el ID de una orden, la busca en la base de datos y la envuelve
        en una instancia business_logic.OrdenCompra.
        """
        order = OrdenCompra()
        order.OrdenCompra = models.OrdenCompra.objects.get(id=order_id)

        return order
