#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

from fblog.managers import PublicManager
from fevents.models import Event
#from sorl.improved.fields import ImprovedImageWithThumbnailsField
#from tagging.fields import TagField
from django.contrib.auth.models import User

class Ptype(models.Model):
    title = models.CharField(max_length=70)
    title_plural = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    order = models.PositiveIntegerField('Display Order', blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='ptypes/')#max_width=800, max_height=800, # Thumbnail for admin site.
    hidden_related = models.BooleanField(default=False)

    class Meta:
        ordering = ('order','title')
        verbose_name = "тип статьи"
        verbose_name_plural = "типы статей"

    def __unicode__(self):
        #dt = unicode(self.date)[:10]
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('fblog.views.category_detail',[str(self.slug)])


class Post(models.Model):

    # Owned
    author = models.ForeignKey(User, related_name='author')

    # Category
    type = models.ForeignKey(Ptype, blank=True, null=True)

    # Published
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,max_length=70)

    # Title
    title = models.CharField(max_length=100)

    # Content
    content = models.TextField()
    preview = models.TextField(blank=True)

    # Self-related
    related_entries = models.ManyToManyField('self', blank=True, null=True)

    # Special
    is_featured = models.BooleanField(default=False)

    # Comments
    enable_comments = models.BooleanField(default=True)

    # TimeStamped
    date = models.DateTimeField(default=datetime.now)
    date_mod = models.DateTimeField(auto_now=True)

    # Stats
    view_count = models.PositiveIntegerField(default=0, editable=False)

    objects = PublicManager()

#    tags = TagField()

    class Meta:
        ordering = ['-date']
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def __unicode__(self):
        dt = unicode(self.date)[:10]
        return "[%s]-%s" % (dt, self.title)

    def preview_or_content(self):
        return self.preview or self.content

    @models.permalink
    def get_absolute_url(self):
        return ('fblog.views.post_detail', [str(self.date.year),str(self.date.strftime("%m")),str(self.date.strftime("%d")),str(self.slug)])
