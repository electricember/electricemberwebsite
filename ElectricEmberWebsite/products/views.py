from datetime import date

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Products


def products_index(request):
    queryset = Products.objects.all()

    return render_to_response("products/index.html", locals(),
                              context_instance=RequestContext(request))


def product_detail(request, slug):
    query = Products.objects.get(slug=slug)
    return render_to_response("products/detail.html", locals(),
                              context_instance=RequestContext(request))
