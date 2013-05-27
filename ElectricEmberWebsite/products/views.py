from datetime import date

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Products

def product_page(request):
    products = Products.objects.all()

    return render_to_response("products.html", locals(), context_instance=RequestContext(request))
