from fevents.models import Event, Etype
from django import template
register = template.Library()
 
@register.inclusion_tag('fevents/category_menu.html')
def category_menu(request):
    events_category_menu = Etype.objects.all()
    return {'events_category_menu':events_category_menu, 'request':request}
 
#@register.inclusion_tag('fevents/archive_menu.html')
#def archive_menu(request):
#events_month_list = Event.objects.dates('date','month',order='DESC')
#return {'events_month_list': events_month_list}
