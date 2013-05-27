from datetime import date

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import Products

def product_page(request):
    queryset = Products.objects.all()

    return render_to_response("results.html", locals(), context_instance=RequestContext(request))
