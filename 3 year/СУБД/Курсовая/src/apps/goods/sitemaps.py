# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.core.sitemaps import BaseSitemap
from apps.goods.models import Item


class GoodsSitemap(BaseSitemap):

    def items(self):
        return Item.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
