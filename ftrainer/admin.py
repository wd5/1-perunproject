#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftrainer.models import Exercise, Part, Member, Skill
from django.contrib import admin


class PartAdmin(admin.ModelAdmin):
    list_display = ["title", "position", "is_published"]
    list_editable = ["position", "is_published"]
    list_per_page = 30

class MemberAdmin(admin.ModelAdmin):
    list_display = ["title", "position", "is_published"]
    list_editable = ["position", "is_published"]
    list_per_page = 30

class SkillAdmin(admin.ModelAdmin):
    list_display = ["title", "position", "is_published"]
    list_editable = ["position", "is_published"]
    list_per_page = 30

class ExerciseAdmin(admin.ModelAdmin):
    exclude = ["user"]
    list_display = ["title", "part", "date", "is_published"]
    list_editable = ["is_published"]
    list_per_page = 30

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Skill, SkillAdmin)
