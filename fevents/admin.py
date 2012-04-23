#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Event, Etype, EventRelation
from django.contrib import admin
from genericadmin.admin import GenericAdminModelAdmin

class EventRelationInline(admin.TabularInline):
    model = EventRelation

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'	
    list_display = ["title", "date", "is_published"]
    list_editable = ["is_published"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [EventRelationInline,]

admin.site.register(Event, EventAdmin)
admin.site.register(Etype)
