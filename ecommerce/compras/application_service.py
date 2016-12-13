from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from compras.models import Producto, OrdenCompra
from compras.business_logic import Carrito, PurchaseOrder
from django.db.models import Q


def order_detail(request, id):
    print('Ordenes existentes son: ')
    for o in OrdenCompra.objects.all():
        print('ID: {} | IdOrdenCompra: {}'.format(o.id, o.idOrdenCompra))

    try:
        order = PurchaseOrder.find(id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Orden de compra no existe!</h1>')

    return render(request, 'order_detail.html', {'order': order})


def ver_detalles(request, idProducto):
    detalleProducto = Producto.objects.get(idProducto=idProducto)
    return render(request, 'detalles_producto.html', {'productoDetalle': detalleProducto})


def product_list(request):
    product_list = Producto.objects.order_by('nombre')[:10]
    carrito = Carrito(request.session['idCliente'])
    context_list = {'products': product_list, 'carrito': carrito.carrito}
    return render(request, 'product_list.html', context_list)


def product_search(request, consulta):
    products = Producto.objects.filter(Q(descripcion__icontains=consulta) | Q(descripcion__icontains=consulta))
    context_list = {'products': products}
    return render(request, 'product_list.html', context_list)


def agregarProductoCarrito(request):
    request.session['idCliente'] = 1
    carrito = Carrito(request.session['idCliente'])
    if request.method == "POST" and 'idProducto' in request.POST:
        carrito.agregarProducto(request.POST['idProducto'], request.POST['Cantidad'])
    elif request.method == "GET" and 'idProducto' in request.GET:
        carrito.agregarProducto(request.GET['idProducto'], request.GET['Cantidad'])
    else:
        pass

    return render(request, 'product_list.html', {'carrito': carrito.carrito})

def adquirirCarrito(request):
    if request.method == 'GET' and 'adquirir' in request.GET:
        purchaseOrder = PurchaseOrder(int(request.session['idCliente']))
        purchaseOrder.buyArticles()
        return render(request, 'product_list.html', {'purchaseOrder': purchaseOrder})
    return render(request, 'product_list.html')
