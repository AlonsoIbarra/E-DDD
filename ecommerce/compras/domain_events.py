# Clases base para los eventos de dominio
class ClientDomainEvent:
    pass


class ProductDomainEvent:
    pass


class CarritoDomainEvent:
    pass


class OrdenCompraDomainEvent:
    pass


# Eventos de dominio de Cliente
class SesionIniciada(ClientDomainEvent):
    pass


class UsuarioRegistrado(ClientDomainEvent):
    pass


# Eventos de dominio de Producto
class ProductoAgregadoCarrito(ProductDomainEvent):
    pass


class ProductoCreado(ProductDomainEvent):
    pass


class ProductoMostrado(ProductDomainEvent):
    pass


class ProductoActualizado(ProductDomainEvent):
    pass


# Eventos de dominio de Carrito
class CarritoActualizado(CarritoDomainEvent):
    pass


class CarritoAdquirido(CarritoDomainEvent):
    pass


class CarritoDesechado(CarritoDomainEvent):
    pass


# Eventos de dominio de OrdenCompra
class DescuentoAplicado(OrdenCompraDomainEvent):
    pass


class OrdenPagada(OrdenCompraDomainEvent):
    pass


class OrdenCancelada(OrdenCompraDomainEvent):
    pass
