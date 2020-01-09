# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.utils.deconstruct import deconstructible
from pytils.translit import slugify

nullable = dict(null=True, blank=True)


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        old_filename, _ext = os.path.splitext(filename)
        new_filename = '{}{}'.format(slugify(old_filename), _ext)
        return os.path.join(self.path, new_filename)


def invalidate_template_fragment(fragment_name, *variables):
    cache_key = make_template_fragment_key(
        fragment_name, vary_on=variables)
    cache.delete(cache_key)
