#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url
from fblog.feeds import BlogFeed

urlpatterns = patterns('fblog.views',

    url(r'^$', view='post_list', name='blog_index'),
    url(r'^rss/$',
        view=BlogFeed(),
        name='blog_rss'
    ),

    #url(r'^(?P<fnews_id>\d+)/$', 'news1', name='blog_entry'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        view='post_detail',
        name='blog_detail'
    ),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/edit/$',
        view='post_edit',
        name='blog_post_edit'
    ),

    url(r'^new/$',
        view='post_new',
        name='blog_post_new'
    ),


    url(r'^category/(?P<slug>[-\w]+)/$',
        view='category_detail',
        name='blog_category_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        view='post_archive_day',
        name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        view='post_archive_month',
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        view='post_archive_year',
        name='blog_archive_year'
    ),
)
