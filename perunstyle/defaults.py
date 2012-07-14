# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from mezzanine.conf import register_setting

register_setting(
    name="SITE_SLOGAN",
    label=_("Slogan"),
    description=_("Slogan"),
    editable=True,
    default="",
)
