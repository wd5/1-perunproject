#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Post, Ptype
from django.contrib import admin
from django.contrib.contenttypes import generic
from fevents.models import EventRelation
from fgallery.models import ImageRelation


class ImageAdminInline(generic.GenericTabularInline):
    model = ImageRelation
    raw_id_fields = ('image',)
    extra = 1

class EventAdminInline(generic.GenericTabularInline):
    model = EventRelation
    extra = 1

class PostAdmin(admin.ModelAdmin):
    exclude = ["author"]
    date_hierarchy = 'date'
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 20

    filter_horizontal = ["related_entries"]
    list_display = ["title", "date", "is_published"]
    list_editable = ["is_published"]

    fieldsets = (
        (None, {
            'fields': ('is_published', 'type', 'title', 'slug', 'content')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('preview', 'related_entries', 'date', 'is_featured', 'enable_comments')
        }),
        ('Meta fields', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords',)
        }),
    )
#    filter_horizontal = ['images',]

    inlines = [EventAdminInline,ImageAdminInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Ptype)
