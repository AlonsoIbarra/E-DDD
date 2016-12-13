from django.shortcuts import render
from compras.models import Producto
<<<<<<< HEAD
from compras.business_logic import Carrito, PurchaseOrder
=======
from compras.business_logic import Carrito
from django.shortcuts import redirect
>>>>>>> b9db573a0f61b998235271c0755db8d162adb6de
# Create your views here.


def order_detail(request, id):
    return render(request, 'order_detail.html')


def ver_detalles(request, idProducto):
    detalleProducto = Producto.objects.get(idProducto=idProducto)
    return render(request, 'detalles_producto.html', {'productoDetalle': detalleProducto})


def product_list(request):
    product_list = Producto.objects.order_by('nombre')[:10]
    carrito = Carrito(request.session['idCliente'])
    context_list = {'products': product_list, 'carrito': carrito.carrito}
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
