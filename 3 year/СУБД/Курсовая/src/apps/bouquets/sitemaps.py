# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.bouquets.models import Bouquet
from apps.core.sitemaps import BaseSitemap


class BouquetSitemap(BaseSitemap):

    def items(self):
        return Bouquet.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
