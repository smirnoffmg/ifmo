# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template

register = template.Library()


@register.inclusion_tag('tags/opengraph.html')
def render_opengraph(_object):
    seo_kwargs = {}
    if hasattr(_object, 'get_og_info'):
        seo_kwargs = _object.get_og_info()
    return seo_kwargs
