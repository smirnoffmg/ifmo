# -*- coding: utf-8 -*-
from adminsortable.admin import SortableAdmin
from django.contrib import admin

from apps.flowers.models import Flower


@admin.register(Flower)
class FlowerAdmin(SortableAdmin):
    list_display = ('title', 'color')
