from django.db import models
import ast

# Create your models here.
class ListProduct(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):

        super(ListProduct, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

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
    listaProductos = ListProduct()
    fechaCarrito = models.DateField(auto_now=True)
    total = models.DecimalField(decimal_places=2, max_digits=8)

class OrdenCompra (Entity):
    idOrdenCompra = models.AutoField(primary_key=True)
    fechaCompra = models.DateField(auto_now_add=True)
    idCliente = models.IntegerField()
    listaProductosOrden = ListProduct()
    STATUS_CHOICES = (
	(0, "Pagada"),
	(1, "Pendiente"),
	(2, "Cancelada"),
    )
    status = models.IntegerField(choices = STATUS_CHOICES)
