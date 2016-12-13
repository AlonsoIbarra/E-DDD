from django.shortcuts import render
from compras.models import Producto
from compras.business_logic import Carrito, PurchaseOrder
from django.shortcuts import redirect
from django.db.models import Q
# Create your views here.


def order_detail(request, id):
    return render(request, 'order_detail.html')


def ver_detalles(request, idProducto):
    detalleProducto = Producto.objects.get(idProducto=idProducto)
    return render(request, 'detalles_producto.html', {'productoDetalle': detalleProducto})


def product_list(request):
    request.session['idCliente'] = 1
    product_list = Producto.objects.order_by('nombre')[:10]
    carrito = Carrito(request.session['idCliente'])
    context_list = {'products': product_list, 'carrito': carrito.carrito}
    return render(request, 'product_list.html', context_list)


def product_search(request):
    consulta = request.GET.get('consulta')
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
