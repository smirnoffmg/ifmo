# -*- coding: utf-8 -*-

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from apps.goods.models import Item


def get_additional_block_items():
    cache_gragment_key = make_template_fragment_key('additional_block_items')
    if cache.get(cache_gragment_key):
        return []
    return Item.objects.filter(show_in_additional_goods_block=True)[:5]
