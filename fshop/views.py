#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from django.views.generic.simple import direct_to_template
from fshop.models import Product

def product_list(request):
    product_queryset = Product.objects.all().select_related().order_by('-date_publish')
    return object_list(request, queryset=product_queryset, paginate_by=20)

def product_detail(request, id, **kwargs):
    product = Product.objects.get(pk=id)
    return direct_to_template(request,'fshop/product_detail.html', {'object': product})

