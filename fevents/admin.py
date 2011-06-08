#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Event, Etype
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'	
    list_display = ["title", "date", "is_published"]
    list_editable = ["is_published"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Event, EventAdmin)
admin.site.register(Etype)
