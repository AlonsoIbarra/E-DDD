import entities
 
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
    def __init__(self, pCarrito):
        self.OrdenCompra = entities.OrdenCompra(idCliente = pCarrito.idCliente, status = 1, listaProductosOrden = pCarrito.listaProductos)

    def mostrarDetalle(self):
        return self.OrdenCompra
        
        
    
        
        

