from compras import models
from decimal import Decimal
import json

class Carrito():
    def __init__(self, pIdCliente):
        if models.Carrito.objects.filter(idCliente = pIdCliente).exists():
            self.carrito = models.Carrito.objects.get(idCliente = pIdCliente)
        else:
            self.carrito = models.Carrito.objects.create(
                idCliente = pIdCliente,
                listaProductos = json.dumps([]),
                total = 0,
            )

    def get(self):
        return self.carrito.idCarrito

    @staticmethod
    def find(idCarrito):
        return models.Carrito.objects.get(idCarrito=idCarrito)

    def agregarProducto(self, pProducto, pCantidad):
        producto = models.Producto.objects.get(idProducto=pProducto)
        listaProductos = json.loads(self.carrito.listaProductos)
        listaProductos.append([producto.idProducto, pCantidad])
        self.carrito.listaProductos = json.dumps(listaProductos)
        self.carrito.total = self.calcularTotal()

    def calcularTotal(self):
        listaProductos = json.loads(self.carrito.listaProductos)
        return sum([float(cantidad) * float(models.Producto.objects.get(idProducto=id).precio)  for id, cantidad in listaProductos])


class OrdenCompra():
    def __init__(self, pCarrito):
        self.OrdenCompra = entities.OrdenCompra(idCliente = pCarrito.idCliente, status = 1, listaProductosOrden = pCarrito.listaProductos)

    def mostrarDetalle(self):
        return self.OrdenCompra

    @staticmethod
    def find(order_id):
        return models.OrdenCompra.objects.get(id=order_id)
