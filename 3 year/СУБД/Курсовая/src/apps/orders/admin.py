# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    change_form_template = 'admin/orders/change_form.html'

    def full_price_formatted(self, obj):
        return '{}&nbsp;₽'.format(obj.get_full_price())

    full_price_formatted.allow_tags = True
    full_price_formatted.short_description = 'Полная стоимость'

    def get_delivery_price_formatted(self, obj):
        return '{}&nbsp;₽'.format(obj.get_delivery_price())

    get_delivery_price_formatted.allow_tags = True
    get_delivery_price_formatted.short_description = 'Стоимость доставки'

    def get_card_price_formatted(self, obj):
        return '{}&nbsp;₽'.format(obj.get_card_price())

    get_card_price_formatted.allow_tags = True
    get_card_price_formatted.short_description = 'Стоимость открытки'

    list_display = (
        'order_id', 'sender', 'sender_phone', 'receiver', 'receiver_phone',
        'get_delivery_price_formatted',
        'get_card_price_formatted',
        'promocode',
        'promocode_value',
        'full_price_formatted',
        'created_at', 'is_payed', 'status')

    list_filter = ('is_payed', 'status')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': (
                'status', ('payment_type', 'is_payed'), 'delivery_date',
                'promocode',
                'promocode_value',
                'delivery_time_period',
                'exact_delivery_time')
        }),
        (_('Card'), {
            'fields': ('card_type', 'card_text')
        }),
        (_('Sender'), {
            'fields': (
                'sender', 'sender_phone', 'sender_email', 'sender_address',
                'sender_comment')
        }),
        (_('Receiver'), {
            'fields': (
                'receiver', 'receiver_phone', 'receiver_email',
                'receiver_address',
                'receiver_comment')
        }),
    )
