#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import Library, Node
from django.db.models import get_model
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site

from ftrainer.models import Part, Member, Skill


register = Library()

@register.inclusion_tag('ftrainer/menu_parts.html')
def parts_menu():
    parts_menu = Part.objects.filter(is_published=True)
    return {'parts_menu':parts_menu}

@register.inclusion_tag('ftrainer/menu_skills.html')
def skills_menu():
    skills_menu = Skill.objects.filter(is_published=True)
    return {'skills_menu':skills_menu}

@register.inclusion_tag('ftrainer/menu_members.html')
def members_menu():
    members_menu = Member.objects.filter(is_published=True)
    return {'members_menu':members_menu}