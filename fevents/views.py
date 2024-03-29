#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.list_detail import object_list
from fevents.models import Event, Etype

def event_list(request):
    events_list = Event.objects.published().select_related().order_by('-date')
    return object_list(request, queryset=events_list, paginate_by=50)

def category_detail(request, slug, **kwargs):
    events_list = Event.objects.published().filter(type__slug__exact=slug)
    category = Etype.objects.get(slug=slug)
    return object_list(
        request, queryset=events_list, paginate_by=50,
        template_name='fevents/category_detail.html',
        extra_context={'category':category.title_plural},
        **kwargs)
