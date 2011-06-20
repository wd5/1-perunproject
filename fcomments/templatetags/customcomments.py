from django.db.models import get_model
from django.template import Library, Node
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site

register = Library()

class LatestCommentsNode(Node):

    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
        
    def render(self, context):
        site = Site.objects.get_current()
        context[self.varname] = Comment._default_manager.for_model(self.model).filter(site = site, is_public = True, is_removed = False)[:self.num]
        return ''

def get_latest_comments(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest_comments tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest_comments tag must be 'as'"
    return LatestCommentsNode(bits[1], bits[2], bits[4])
    
get_latest = register.tag(get_latest_comments)
