#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from models import Photo, Album, Video
from form_utils.widgets import ImageWidget
from django.contrib.contenttypes import generic
from fevents.models import EventRelation


class EventAdminInline(generic.GenericTabularInline):
    model = EventRelation
    extra = 1

class PhotoForm(forms.ModelForm):
    image = forms.FileField(widget=ImageWidget(width=140,height=140))
    class Meta:
        model = Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    form = PhotoForm
    fields = ('image', 'title', 'seo_title', 'tags')

class AlbumAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    #exclude = ["author"]
    search_fields = ["title"]
    list_display = ["get_cover", "title", "date", "is_published"]
    list_editable = ["title", "is_published"]    
    list_filter = ["date"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [EventAdminInline, PhotoInline,]

class PhotoAdmin(admin.ModelAdmin):
    exclude = ['author']
    date_hierarchy = 'date'		
    search_fields = ["title"]
    list_display = ["image_thumb", "title", "date", "album", "is_cover", "position"]
    list_editable = ["title", "album", "is_cover", "position"]
    list_filter = ["date", "album"]
    #prepopulated_fields = {"slug": ("title",)}

    fieldsets = [
        (None,               {'fields': ['is_published','album','image','title','tags']}),
        ('Additional', {'fields': ['seo_title', 'date','position','is_cover','rating','enable_comments',], 'classes': ['collapse']}),
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()
    
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Video)
