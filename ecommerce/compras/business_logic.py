from compras import models
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
        listaProductos.append([producto.idProducto, pCantidad, producto.precio])
        self.carrito.listaProductos = json.dumps(listaProductos)
        self.carrito.total = self.calcularTotal()

    def calcularTotal(self):
        listaProductos = json.loads(self.carrito.listaProductos)
        return sum([cantidad * precio for id, cantidad, precio in listaProductos])


class PurchaseOrder():

    def __init__(self):
        self.ordenCompra = models.OrdenCompra()

    def buyArticles(self, pCarrito):
        self.ordenCompra = models.ordenCompra.objects.create(
            idCliente=1,
            listaProductosOrden=pCarrito.listaProductos,
            status=1,
        )

    def getDetails(self):
        return self.ordenCompra

    @staticmethod
    def find(order_id):
        return models.OrdenCompra.objects.get(id=order_id)


class ProductCatalog():
    def __init__(self):
        pass

    def find(self, pidProduct):
        return models.Producto.objects.get(pk=pidProduct)

    def getAll(self):
        return models.Producto.objects.get()


class PurchaseOrderList():
    def __init__(self):
        pass

    def findById(self, pidPurchaseOrder):
        return models.OrdenCompra.objects.get(pk=pidPurchaseOrder)
    
    def getAll(self):
        return models.OrdenCompra.objects.get()
