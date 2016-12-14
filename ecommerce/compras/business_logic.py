from compras import models
import json
from django.utils import timezone

class Producto():
    def __init__(self):
        self.Producto = models.Producto.all()


class Carrito():
    def __init__(self, pIdCliente):
        if models.Carrito.objects.filter(idCliente=pIdCliente).exists():
            self.carrito = models.Carrito.objects.get(idCliente=pIdCliente)
        else:
            self.carrito = models.Carrito.objects.create(
                idCliente=pIdCliente,
                listaProductos=json.dumps([]),
                total=0,
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
        listaProductos = [[a, sum(int(y) for x, y in listaProductos if x == a)] for a, b in listaProductos]
        listaProductos = [listaProductos[i] for i in range(len(listaProductos)) if listaProductos[i] not in listaProductos[:i]]
        self.carrito.listaProductos = json.dumps(listaProductos)
        self.carrito.total = self.calcularTotal()
        self.carrito.save()

    def calcularTotal(self):
        listaProductos = json.loads(self.carrito.listaProductos)
        return sum([float(cantidad) * float(models.Producto.objects.get(idProducto=id).precio) for id, cantidad in listaProductos])


class PurchaseOrder():

    def __init__(self, pidCarrito):
        self.carrito = models.Carrito.objects.get(idCarrito=pidCarrito)
        
    def buyArticles(self):
        
        self.oc = models.OrdenCompra.objects.create(
            listaProductosOrden = self.carrito.listaProductos,
            status = 1,
            fechaCompra = timezone.now(),
            idCliente = self.carrito.idCliente
       )


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

