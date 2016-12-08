from django.db import models

# Create your models here.


class Entity (models.Model):
    pass


class Producto (Entity):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=30)
    precio = models.DecimalField(decimal_places=2, max_digits=8)


class Carrito (Entity):
    idCarrito = models.AutoField(primary_key=True)
    idCliente = models.IntegerField()
    listaProductos = models.TextField()
    fechaCarrito = models.DateField(auto_now=True)
    total = models.DecimalField(decimal_places=2, max_digits=8)


class OrdenCompra (Entity):
    idOrdenCompra = models.AutoField(primary_key=True)
    fechaCompra = models.DateField(auto_now_add=True)
    idCliente = models.IntegerField()
    listaProductosOrden = models.TextField()
    STATUS_CHOICES = (
        (0, "Pagada"),
        (1, "Pendiente"),
        (2, "Cancelada"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
