from unipath import Path

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from settings.base import STATIC_ROOT, MEDIA_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ElectricEmberWebsite.views.home', name='home'),
    # url(r'^ElectricEmberWebsite/', include('ElectricEmberWebsite.foo.urls')),
    #url(r'^$', 'homepage.views.hello', name='home'),
    #url(r'^APP/', include('APP.urls', namespace="APP")),
    url(r'^products/', include('products.urls', namespace="products")),

    # Admin and Admin Docs (Using a 32-char randomly generated URL path for the Project Admin)
    url(r'^FqA244qADyMjNhZK6wkRDwGu2qTTcjW2/doc/', include('django.contrib.admindocs.urls')),
    url(r'^FqA244qADyMjNhZK6wkRDwGu2qTTcjW2/', include(admin.site.urls)),

    # Serve static assets
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': STATIC_ROOT }),
)
