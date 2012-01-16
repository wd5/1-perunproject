# -*- coding: utf-8 -*-

from django.conf import settings

SHOP_TITLE = getattr(settings, 'FSHOP_SHOP_TITLE', 'Shop')
SHOP_DESCRIPTION = getattr(settings, 'FSHOP_SHOP_DESCRIPTION', '')
