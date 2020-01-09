# -*- coding: utf-8 -*-
from apps.core.tests import BaseTestCase


class BasketTestCase(BaseTestCase):

    def test_1_basket_page(self):
        self.go_reverse('basket:basket')
        self.screenshot('basket.png')
