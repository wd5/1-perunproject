from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.comments.forms import CommentForm
from fcomments.threadlocals import get_request
from captcha.fields import CaptchaField

class FCommentForm(CommentForm):
    def __init__(self, *args, **kwargs):
        super(FCommentForm, self).__init__(*args, **kwargs)
        request = get_request()
        if not request.user.is_authenticated():
            self.fields['captcha'] = CaptchaField()
        else:
            self.fields['email'] = forms.EmailField(label=_("Email address"), required=False)
