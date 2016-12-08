from django.conf.urls import patterns, url
from .application_service import order_detail


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^(?P<id>\d+)', order_detail, name='order_detail'),
)
