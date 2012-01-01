# -*- coding: utf-8 -*-

"""
Unicode usernames support for UserCreation/ChangeForms in admin.

Usage: include this app in settings.INSTALLED_APPS
"""

from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import re

class UnicodeUserCreationForm(UserCreationForm):
    username = forms.RegexField(label=_("Username"), max_length=30, regex=re.compile(ur'^[\w.@+-]+$', re.UNICODE),
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

class UnicodeUserChangeForm(UserChangeForm):
    username = forms.RegexField(label=_("Username"), max_length=30, regex=re.compile(ur'^[\w.@+-]+$', re.UNICODE),
        help_text = _("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

class UnicodeUserAdmin(UserAdmin):
    form = UnicodeUserChangeForm
    add_form = UnicodeUserCreationForm

admin.site.unregister(User)
admin.site.register(User, UnicodeUserAdmin)
