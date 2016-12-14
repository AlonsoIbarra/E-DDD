from django.shortcuts import render, render_to_response
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from compras.models import Producto
from compras.business_logic import Carrito, PurchaseOrder, ListProduct
from django.shortcuts import redirect


def order_detail(request, id):
    try:
        order = PurchaseOrder.find(id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Orden de compra no existe!</h1>')

    return render(request, 'order_detail.html', {'order': order})


def ver_detalles(request, idProducto):
    detalleProducto = Producto.objects.get(idProducto=idProducto)
    return render(request, 'detalles_producto.html', {'productoDetalle': detalleProducto})


def product_list(request):
    request.session['idCliente'] = 1
    carrito = Carrito(request.session['idCliente'])
    request.session['idCarrito'] = carrito.get()

    if request.method == "GET" and 'consulta' in request.GET:
        product_list = ListProduct.findByConsulta(request.GET['consulta'])
    else:
        product_list = ListProduct.findAll()
    context_list = {'products': product_list, 'carrito': carrito.carrito}
    return render(request, 'product_list.html', context_list)


def agregarProductoCarrito(request):
    carrito = Carrito(request.session['idCliente'])
    if request.method == "POST" and 'idProducto' in request.POST:
        carrito.agregarProducto(request.POST['idProducto'], request.POST['Cantidad'])
    elif request.method == "GET" and 'idProducto' in request.GET:
        carrito.agregarProducto(int(request.GET['idProducto']), int(request.GET['Cantidad']))
    else:
        pass

    return redirect("/orders/")


def adquirirCarrito(request):
    purchaseOrder = PurchaseOrder(int(request.session['idCarrito']))
    purchaseOrder.buyArticles()

    return redirect('/orders/purchase/{}'.format(
        purchaseOrder.oc.idOrdenCompra))
