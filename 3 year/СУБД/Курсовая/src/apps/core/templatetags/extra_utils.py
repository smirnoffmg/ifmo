# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter(name='chunks')
def chunks(iterable, chunk_size):
    for i in xrange(0, len(iterable), chunk_size):
        yield iterable[i:i + chunk_size]


def multiply(value, arg):
    return value * arg
