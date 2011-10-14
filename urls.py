#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings

from forms import ImprovedRegistrationForm

from djangobb_forum import settings as forum_settings

from sitemap import SitemapForum, SitemapTopic, SitemapPage
sitemaps = {
    'page': SitemapPage,
    #'forum': SitemapForum,
    #'topic': SitemapTopic,
}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # (r'^$', 'views.mainpage'),

    (r'^about/$', 'django.views.generic.simple.redirect_to', {'url': '/tradition/'}),
    (r'^services/$', 'django.views.generic.simple.redirect_to', {'url': '/strely/'}),
    (r'^training/$', 'django.views.generic.simple.redirect_to', {'url': '/contacts/'}),

    # BLOG
    (r'^blog/', include('fblog.urls')),
    # backward compatible
    (r'^news/', 'django.views.generic.simple.redirect_to', {'url': '/blog/'}),
    (r'^sgb/', 'django.views.generic.simple.redirect_to', {'url': '/tradition/'}),
    (r'^post/(?P<fnews_id>\d+)/$', 'fblog.views.news1'), # REDIRECTED

    # EVENTS
    (r'^events/', include('fevents.urls')),

    # GALLERY
    (r'^gallery/', include('fgallery.urls')),
    # backward compatible
    (r'^album/(?P<falbum_id>\d+)/$', 'django.views.generic.simple.redirect_to', {'url': '/gallery/%(falbum_id)s/'}),
    #(r'^album/(?P<falbum_id>\d+)/$', 'fgallery.views.album1'),
    (r'^photo/(?P<fphoto_id>\d+)/$', 'fgallery.views.photo1'), # REDIRECTED

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # Registration
    url(r'^accounts/register/$', 'registration.views.register', {'backend': 'registration.backends.default.DefaultBackend', 'form_class': ImprovedRegistrationForm}, name='registration_register'),
    #(r'^forum/account/', include(authopenid_urlpatterns)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^auth/', include( 'netauth.urls')),

    # Forum
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
    # Sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'^simplepages/', include('simplepages.urls')), 
    url(r'^captcha/', include('captcha.urls')),

    (r'^d3c503b7e78d.html$', 'django.views.static.serve', {'path':"/d3c503b7e78d.html",'document_root': settings.MEDIA_ROOT,'show_indexes': False }),
    (r'^yandex_5ad2946d08ecab92.html$', 'django.views.static.serve', {'path':"/yandex_master.html",'document_root': settings.MEDIA_ROOT,'show_indexes': False }),
    (r'^googlecb919a27ff82c271.html$', 'django.views.static.serve', {'path':"/googlecb919a27ff82c271.html",'document_root': settings.MEDIA_ROOT,'show_indexes': False }),
)


# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('messages.urls')),
   )


# routing static files
if settings.LOCALSERVER:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
