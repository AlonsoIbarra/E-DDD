from django.shortcuts import render
from compras.models import Producto
from compras.business_logic import Carrito
# Create your views here.


def order_detail(request, id):
    return render(request, 'order_detail.html')


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
