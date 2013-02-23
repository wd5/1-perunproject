#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


GROUP_CHOICES_LIST = (
    (0, _('Common')),
    (1, _('Central fighter')),
    (2, _('Attacking squad')),
    (3, _('Mixed')),
)


GROUP_CHOICES = getattr(
    settings, 'FTRAINER_GROUP_CHOICES', GROUP_CHOICES_LIST)