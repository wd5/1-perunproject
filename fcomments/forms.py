from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.comments.forms import CommentForm
from captcha.fields import CaptchaField

class FCommentForm(CommentForm):
    def __init__(self, *args, **kwargs):
        super(FCommentForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = CaptchaField()

class AuthCommentForm(CommentForm):
    def __init__(self, *args, **kwargs):
        super(AuthCommentForm, self).__init__(*args, **kwargs)
        # email not required, because user may authenticated via oauth
        self.fields['email'].required = False

