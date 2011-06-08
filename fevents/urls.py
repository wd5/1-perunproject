#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('fevents.views',
    url(r'^$', 'event_list', name='events'),
    url(r'^category/(?P<slug>[-\w]+)/$',
        view='category_detail',
        name='fevents_category_detail'
    ),
)
