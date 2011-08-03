#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('fgallery.views',
    url(r'^$', 'albums', name='gallery'),
    url(r'^(?P<falbum_id>\d+)/$', 'album1', name='gallery_album'),
    url(r'^(?P<falbum_id>\d+)/(?P<fphoto_id>\d+)/$', 'photo_detail', name='gallery_photo'),
    url(r'^(?P<falbum_id>\d+)/comments/$', 'album1c', name='gallery_comments'),
    url(r'^(?P<falbum_id>\d+)/edit/$', 'album_edit', name='gallery_edit'),
    url(r'^tags/$', direct_to_template, {'template': 'fgallery/tag_list.html'}),
    url(r'^tags/(?P<slug>[^/]+)/$', view='tag_detail', name='gallery_tag'),
    url(r'^video/$', 'video_list', name='gallery_videolist'),
    url(r'^video/(?P<fvideo_id>\d+)/$', 'video_detail', name='gallery_video'),
)
