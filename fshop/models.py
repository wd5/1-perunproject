#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from fshop.managers import PublicManager


class Product(models.Model):

    # Main fields
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='fshop_images/')
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    # Publishing fields
    author = models.ForeignKey(User)
    date_publish = models.DateTimeField(default=datetime.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=70)
    enable_comments = models.BooleanField(default=False)
    
    # Manager
    objects = PublicManager()
    
    class Meta:
        ordering = ["-date_created"]
        verbose_name = "товар"
        verbose_name_plural = "товары"
    
    def __unicode__(self):
        return u"%s" % (self.title)

