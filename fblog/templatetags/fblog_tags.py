#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import Library, Node
from django.db.models import get_model
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from fblog.models import Post, Ptype
from django.utils.dates import MONTHS

register = Library()

@register.filter
def month_name(month_number):
    return MONTHS[int(month_number)]

@register.inclusion_tag('fblog/category_menu.html')
def category_menu(request):
    category_menu = Ptype.objects.all()
    return {'category_menu':category_menu, 'request':request}

@register.inclusion_tag('fblog/archive_menu.html')
def archive_menu(request):
    blog_month_list = Post.objects.dates('date','month',order='DESC')
    return {'blog_month_list': blog_month_list}

@register.inclusion_tag('fblog/archive_tree.html')
def archive_tree(current_entry=None):
    entry_list = Post.objects.published()
    current_entry = current_entry
    return {'entry_list': entry_list, 'current_entry': current_entry}


class LatestFeaturedContentNode(Node):

    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
        
    def render(self, context):
        site = Site.objects.get_current()
        context[self.varname] = self.model._default_manager.published().filter(is_featured=True)[:self.num]
        return ''

def get_latest_featured(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest_featured tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest_comments tag must be 'as'"
    return LatestFeaturedContentNode(bits[1], bits[2], bits[4])
    
get_latest_featured = register.tag(get_latest_featured)
