from fblog.models import Post, Ptype
from django import template
register = template.Library()

@register.inclusion_tag('fblog/category_menu.html')
def category_menu(request):
    category_menu = Ptype.objects.all()
    return {'category_menu':category_menu, 'request':request}

@register.inclusion_tag('fblog/archive_menu.html')
def archive_menu(request):
    blog_month_list = Post.objects.dates('date','month',order='DESC')
    return {'blog_month_list': blog_month_list}
