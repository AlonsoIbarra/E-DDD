from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from compras.models import Producto
from compras.business_logic import OrdenCompra


def order_detail(request, id):
    try:
        order = OrdenCompra.find(id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Orden de compra no existe!</h1>')

    return render(request, 'order_detail.html', {'order': order})


def ver_detalles(request, idProducto):
#	detalleProducto = Producto.objects.get(id=idProducto)
	producto = Producto.objects.create(
        nombre  = "Camisa",
        descripcion = "Camisa blanca tipo polo tamaño regular",
        marca = "Polo",
        precio = 540.50
    )
	return render(request,'detalles_producto.html',{'productoDetalle' : producto})
