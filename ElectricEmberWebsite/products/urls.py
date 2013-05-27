from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'products.views.product_page'),

)
