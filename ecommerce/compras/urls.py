from django.conf.urls import patterns, url
from .application_service import order_detail
from .application_service import ver_detalles

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^(?P<id>\d+)', order_detail, name='order_detail'),
    url(r'^verdetalle/(?P<idProducto>\d+)', ver_detalles, name='ver_detalles'),
)
