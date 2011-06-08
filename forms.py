# -*- coding: utf-8 -*-

import re
from django import forms
from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import CaptchaField

class ImprovedRegistrationForm(RegistrationFormUniqueEmail):
    '''
    Allowed UTF8 logins with space
    '''
    def __init__(self, *args, **kwargs):
        super(ImprovedRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].regex = re.compile(r"^[\w\s-]+$", re.UNICODE)
    captcha = CaptchaField(label='Решите пример с картинки:')
