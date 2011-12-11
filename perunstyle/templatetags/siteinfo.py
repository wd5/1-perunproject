from django import template
from django.contrib.sites.models import Site

register = template.Library()

@register.simple_tag()
def site():
    site_object = Site.objects.get_current()
    return site_object.domain
