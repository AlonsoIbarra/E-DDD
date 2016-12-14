import json
from compras import models
from django.utils import timezone
from django.db.models import Q


class ListProduct():
    def __init__(self):
        self.Producto = models.Producto.all()

    def findAll():
        """ Obtener el listado de producto que se encuentre en la
        entidad de productos
        """
        product_list = models.Producto.objects.order_by('nombre')
        return product_list

    def findByConsulta(consulta):
        """ Obtener el listado de producto que se encuentre en la
        entidad de productos de acuerdo a la consulta
        """
        products = models.Producto.objects.filter(
            Q(descripcion__icontains=consulta) |
            Q(nombre__icontains=consulta)
        )
        return products


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

    def __init__(self, pidCarrito=None):
        if pidCarrito:
            self.carrito = models.Carrito.objects.get(idCarrito=pidCarrito)

    def buyArticles(self):
        self.oc = models.OrdenCompra.objects.create(
            listaProductosOrden=self.carrito.listaProductos,
            status=1,
            fechaCompra=timezone.now(),
            idCliente=self.carrito.idCliente
        )

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
            precio = producto.precio

            products.append({
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'cantidad': cantidad,
                'precio': precio,
                'subtotal': round(precio * cantidad, 2)
            })

        return products

    @property
    def total(self):
        """ Calcula el total de la orden, iterando sobre los productos y
        sumando su subtotal.
        """
        total = 0

        for product in self.products():
            total += product['subtotal']

        return round(total, 2)

    @staticmethod
    def find(order_id):
        """ Dado el ID de una orden, la busca en la base de datos y la envuelve
        en una instancia PurchaseOrder
        """
        order = models.OrdenCompra.objects.get(id=order_id)
        purchase_order = PurchaseOrder()
        purchase_order.OrdenCompra = order

        return purchase_order


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
