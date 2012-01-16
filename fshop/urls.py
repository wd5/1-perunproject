# -*- coding: utf-8 -*-

from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('fshop.views',
    url(r'^$', 'product_list', name='product_list'),
    url(r'^product/(?P<id>\d+)/$', 'product_detail', name='product_detail'),
)
