from django.shortcuts import render
from compras.models import Producto
from compras.business_logic import Carrito 
# Create your views here.

def order_detail(request, id):
    return render(request, 'order_detail.html')

def ver_detalles(request, idProducto):
	detalleProducto = Producto.objects.get(id=idProducto)
	return render(request,'detalles_producto.html',{'productoDetalle' : producto})
	
def agregarProductoCarrito(request, idProducto, cantidad):
    request.session['idCliente'] = 1
    if 'idCarito' not in request.session:
        carrito = Carrito(request.session['idCliente'])
        request.session['idCarrito'] =  carrito.get()
    else:
    	carrito = Carrito.find(request.session['idCarrito'])
    carrito.agregarProducto(idProducto, cantidad)
    return render(request, 'detalles_producto.html',{'carrito':carrito})