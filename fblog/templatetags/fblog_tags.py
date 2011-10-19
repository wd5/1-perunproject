from fblog.models import Post, Ptype
from django import template
from django.utils.translation import ugettext as _
import calendar

register = template.Library()

@register.filter
def month_name(month_number):
    return _(calendar.month_name[int(month_number)])

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
