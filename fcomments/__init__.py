"""
Custom comments app for authenticated users.

Views copied from django.contrib.comments.views.comments
Changes in views.post_comment:

    # Construct the comment form
    if request.user.is_authenticated():
        form = fcomments.get_auth_form()(target, data=data)
    else:
        form = comments.get_form()(target, data=data)

Settings:

    # urls.py
    ('^comments/post', 'fcomments.views.post_comment'),
    (r'^comments/', include('django.contrib.comments.urls')),
"""

from fcomments.forms import FCommentForm, AuthCommentForm

def get_form():
    return FCommentForm

def get_auth_form():
    return AuthCommentForm
