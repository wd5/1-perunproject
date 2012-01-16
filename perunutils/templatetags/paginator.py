#  Based on: http://www.djangosnippets.org/snippets/73/
#
#  Modified by Sean Reifschneider to be smarter about surrounding page
#  link context.  For usage documentation see:
#
#     http://www.tummy.com/Community/Articles/django-pagination/

from django import template
from django.conf import settings

register = template.Library()

def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    startPage = max(context['page'] - adjacent_pages, 1)
    if startPage <= 3: startPage = 1
    endPage = context['page'] + adjacent_pages + 1
    if endPage >= context['pages'] - 1: endPage = context['pages'] + 1
    page_numbers = [n for n in range(startPage, endPage) \
            if n > 0 and n <= context['pages']]
    page_obj = context['page_obj']
    paginator = context['paginator']

    return {
        'page_obj': page_obj,
        'paginator': paginator,
        'hits': context['hits'],
        'results_per_page': context['results_per_page'],
        'page': context['page'],
        'pages': context['pages'],
        'page_numbers': page_numbers,
        'next': context['next'],
        'previous': context['previous'],
        'has_next': context['has_next'],
        'has_previous': context['has_previous'],
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
    }

register.inclusion_tag('paginator.html', takes_context=True)(paginator)


DEFAULT_PAGINATION = getattr(settings, 'PAGINATION_DEFAULT_PAGINATION', 20)
DEFAULT_WINDOW = getattr(settings, 'PAGINATION_DEFAULT_WINDOW', 20)

@register.inclusion_tag('object_paginate.html', takes_context=True)
def object_paginate(context, base_url, count, paginate_by=DEFAULT_PAGINATION, window=DEFAULT_WINDOW):
    if not isinstance(paginate_by, int):
        paginate_by = template.Variable(paginate_by)
    if not isinstance(window, int):
        window = template.Variable(paginate_by)
    page_count = count / paginate_by
    if count % paginate_by > 0:
        page_count += 1
    context['page_count'] = page_count
    pages = []
    if page_count == 1:
        pass
    elif window >= page_count:
        pages = [e + 1 for e in range(page_count)]
    else:
        pages = [e + 1 for e in range(window-1)]
    context['base_url'] = base_url
    context['pages'] = pages
    context['window'] = window
    return context
