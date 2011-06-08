#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Post, Ptype
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    exclude = ["author"]
    date_hierarchy = 'date'
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 20

    list_display = ["title", "is_published"]
    list_editable = ["is_published"]

    fieldsets = (
        (None, {
            'fields': ('is_published', 'type', 'title', 'slug', 'content')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('preview', 'date', 'is_featured', 'enable_comments', 'event')
        }),
        ('SEO options', {
            'classes': ('collapse',),
            'fields': ('seo_title', 'meta_description', 'meta_keywords')
        }),
    )
#    filter_horizontal = ['images',]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Ptype)
