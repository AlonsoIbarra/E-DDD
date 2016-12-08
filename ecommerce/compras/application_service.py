from django.shortcuts import render
from entities import Producto
# Create your views here.

def order_detail(request, id):
    return render(request, 'order_detail.html')

def ver_detalles(request, idProducto):
	detalleProducto = Producto.objects.get(id=idProducto)

	return render(request, 'ver_detalles.html', 'idProducto'=detalleProducto)