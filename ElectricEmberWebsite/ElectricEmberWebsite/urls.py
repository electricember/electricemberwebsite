from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ElectricEmberWebsite.views.home', name='home'),
    # url(r'^ElectricEmberWebsite/', include('ElectricEmberWebsite.foo.urls')),
    #url(r'^$', 'homepage.views.hello', name='home'),
    #url(r'^APP/', include('APP.urls', namespace="APP")),
    url(r'^products/', include('products.urls', namespace="products")),

    # Use a 32-char randomly generated URL path for the Project Admin
    url(r'^FqA244qADyMjNhZK6wkRDwGu2qTTcjW2/doc/', include('django.contrib.admindocs.urls')),
    url(r'^FqA244qADyMjNhZK6wkRDwGu2qTTcjW2/', include(admin.site.urls)),
)
