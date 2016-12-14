from django.conf.urls import patterns, url
from .application_service import order_detail
from .application_service import ver_detalles, product_list
from .application_service import agregarProductoCarrito, adquirirCarrito

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^purchase/(?P<id>\d+)', order_detail, name='order_detail'),
    url(r'^verdetalle/(?P<idProducto>\d+)', ver_detalles, name='ver_detalles'),
    url(r'^$', product_list, name='product_list'),
    url(r'^agregarProductoCarrito', agregarProductoCarrito),
    url(r'^OrdenDeCompra', adquirirCarrito),
)
