#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

#from tagging.fields import TagField
from sorl.improved.fields import ImprovedImageWithThumbnailsField
from django.contrib.auth.models import User
from fevents.managers import PublicManager

class Etype(models.Model):
    title = models.CharField(max_length=70)
    title_plural = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    order = models.PositiveIntegerField('Display Order', blank=True, null=True)
    image = ImprovedImageWithThumbnailsField(blank=True, null=True, upload_to='etypes/',max_width=800, max_height=800,                                             # Thumbnail for admin site.
         thumbnail={
             'size': (120, 120),
             'options': ('crop','upscale')
         },
         extra_thumbnails={
             'main': {
                 'size': (200, 200),
                 'options': ('crop','upscale',)
             }
         })
    
    class Meta:
        ordering = ('order', 'title')
        verbose_name = "тип события"
        verbose_name_plural = "типы событий"
    
    def __unicode__(self):
        #dt = unicode(self.date)[:10]
        return self.title

class Event(models.Model):
    #author = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now)
    date_mod = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True,max_length=70)
    type = models.ForeignKey(Etype, blank=True, null=True)
 #   tags = TagField()
    
    description = models.TextField(blank=True, null=True)
    enable_comments = models.BooleanField(default=False)

    objects = PublicManager()
    
    class Meta:
        ordering = ["-date"]
        verbose_name = "событие"
        verbose_name_plural = "события"
    
    def __unicode__(self):
        dt = unicode(self.date)[:10]
        return "[%s]-%s" % (dt, self.title)

    @property
    def is_past_due(self):
        if datetime.now() > self.date:
            result = True
        else:
            result = False
        return result
