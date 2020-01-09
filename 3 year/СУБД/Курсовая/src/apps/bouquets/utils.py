# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from apps.bouquets.models import Bouquet


def get_recommended_block_items():
    cache_gragment_key = make_template_fragment_key('recommended_block_items')
    if cache.get(cache_gragment_key):
        return []
    return Bouquet.objects.filter(show_in_recommended_block=True)[:5]
