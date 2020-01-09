# -*- coding: utf-8 -*-
from apps.bouquets.models import Bouquet
from apps.core.tests import BaseTestCase


class BouquetTestCase(BaseTestCase):

    def test_1_index_page(self):
        self.go_reverse('index')
        self.screenshot('index.png')

    def test_2_bouquet_page(self):
        b = Bouquet.objects.order_by('?').first()
        self.go(b.get_absolute_url())
        self.screenshot('bouquet.png')
