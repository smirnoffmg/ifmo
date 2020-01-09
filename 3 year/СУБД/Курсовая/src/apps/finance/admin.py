# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'valid_until', 'active',
                    'created_at', 'updated_at')
    list_filter = ('active', 'valid_until', )
    search_fields = ['code', ]
