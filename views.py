# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template
from fblog.models import Post
from fevents.models import Event


# TODO: templatetags instead of this
def mainpage(request):

    event_list = Event.objects.order_by('-date')[:4]
    news_list = Post.objects.published()[:10]
    featured_list = Post.objects.published().filter(is_featured=True)

    return direct_to_template(request, 'main.html', {'news_list': news_list, 'event_list': event_list, 'featured_list': featured_list})
