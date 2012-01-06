from django.db.models import get_model
from django.template import Library, Node
from django.template.loader import render_to_string
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site
from django.contrib.comments.templatetags.comments import BaseCommentNode
import fcomments

register = Library()

class LatestCommentsNode(Node):

    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
        
    def render(self, context):
        site = Site.objects.get_current()
        context[self.varname] = Comment._default_manager.for_model(self.model).filter(site = site, is_public = True, is_removed = False).order_by('-submit_date')[:self.num]
        return ''

def get_latest_comments(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest_comments tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest_comments tag must be 'as'"
    return LatestCommentsNode(bits[1], bits[2], bits[4])
    
get_latest = register.tag(get_latest_comments)


class AuthCommentFormNode(BaseCommentNode):
    """Insert a form for the comment model into the context."""

    def get_auth_form(self, context):
        ctype, object_pk = self.get_target_ctype_pk(context)
        if object_pk:
            return fcomments.get_auth_form()(ctype.get_object_for_this_type(pk=object_pk))
        else:
            return None

    def render(self, context):
        context[self.as_varname] = self.get_auth_form(context)
        return ''

class RenderAuthCommentFormNode(AuthCommentFormNode):
    """Render the comment form directly"""

    #@classmethod
    def handle_token(cls, parser, token):
        """Class method to parse render_comment_form and return a Node."""
        tokens = token.contents.split()
        if tokens[1] != 'for':
            raise template.TemplateSyntaxError("Second argument in %r tag must be 'for'" % tokens[0])

        # {% render_comment_form for obj %}
        if len(tokens) == 3:
            return cls(object_expr=parser.compile_filter(tokens[2]))

        # {% render_comment_form for app.models pk %}
        elif len(tokens) == 4:
            return cls(
                ctype = BaseCommentNode.lookup_content_type(tokens[2], tokens[0]),
                object_pk_expr = parser.compile_filter(tokens[3])
            )
    handle_token = classmethod(handle_token)

    def render(self, context):
        ctype, object_pk = self.get_target_ctype_pk(context)
        if object_pk:
            template_search_list = [
                "comments/%s/%s/auth_form.html" % (ctype.app_label, ctype.model),
                "comments/%s/auth_form.html" % ctype.app_label,
                "comments/auth_form.html"
            ]
            context.push()
            formstr = render_to_string(template_search_list, {"form" : self.get_auth_form(context)}, context)
            context.pop()
            return formstr
        else:
            return ''

#@register.tag
def get_auth_comment_form(parser, token):
    """
    Get a (new) form object to post a new comment.

    Syntax::

        {% get_auth_comment_form for [object] as [varname] %}
        {% get_auth_comment_form for [app].[model] [object_id] as [varname] %}
    """
    return AuthCommentFormNode.handle_token(parser, token)

#@register.tag
def render_auth_comment_form(parser, token):
    """
    Render the comment form (as returned by ``{% render_comment_form %}``) through
    the ``comments/form.html`` template.

    Syntax::

        {% render_auth_comment_form for [object] %}
        {% render_auth_comment_form for [app].[model] [object_id] %}
    """
    return RenderAuthCommentFormNode.handle_token(parser, token)

register.tag(get_auth_comment_form)
register.tag(render_auth_comment_form)
