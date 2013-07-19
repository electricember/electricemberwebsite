from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'products.views.products_index', name='products_index'),
    url(r'^(?P<slug>[-\w]+)/$', 'products.views.product_detail', name='product_detail'),

)
