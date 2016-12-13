from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from compras.models import Producto
from compras.business_logic import OrdenCompra, Carrito


def order_detail(request, id):
    try:
        order = OrdenCompra.find(id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Orden de compra no existe!</h1>')

    return render(request, 'order_detail.html', {'order': order})


def ver_detalles(request, idProducto):
    # detalleProducto = Producto.objects.get(id=idProducto)
    producto = Producto.objects.create(
        entity_ptr_id=3,
        nombre="Camisa",
        descripcion="Camisa blanca tipo polo tamaño regular",
        marca="Polo",
        precio=540.50
    )

    return render(request, 'detalles_producto.html', {'productoDetalle': producto})


def product_list(request):
    product_list = Producto.objects.order_by('nombre')[:10]
    context_list = {'products': product_list}
    return render(request, 'product_list.html', context_list)


def agregarProductoCarrito(request, idProducto, cantidad):
    request.session['idCliente'] = 1
    if 'idCarito' not in request.session:
        carrito = Carrito(request.session['idCliente'])
        request.session['idCarrito'] = carrito.get()
    else:
        carrito = Carrito.find(request.session['idCarrito'])
    carrito.agregarProducto(idProducto, cantidad)
    return render(request, 'detalles_producto.html', {'carrito': carrito.carrito})
