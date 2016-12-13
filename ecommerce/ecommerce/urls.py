from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    url(r'^orders/', include('compras.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product_list/', include('compras.urls')),
    
)
