# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Max
from django.utils.safestring import mark_safe
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_fsm import ConcurrentTransitionMixin, FSMIntegerField

from apps.core import nullable
from apps.core.models import GenericModel
from apps.core.tasks import send_notification
from apps.orders.consts import (CARD_PRICE_MAPPING, CARD_TYPE_FREE, CARD_TYPES,
                                DELIVERY_COST_MAPPING, DELIVERY_PERIODS,
                                EXACT_TIME_DELIVERY_COST, FREE_DELIVERY_PERIOD,
                                PAYMENT_CASH_TO_COURIER, PAYMENT_TYPE_CHOICES,
                                STATUS_CHOICES, STATUS_CREATED)
from yandex_money.models import Payment
from yandex_money.signals import payment_completed, payment_process

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class Order(ConcurrentTransitionMixin, GenericModel):
    order_id = models.IntegerField(editable=False, default=0)

    sberbank_order_id = models.CharField(editable=False, max_length=255,
                                         blank=True)

    basket = models.OneToOneField(
        'basket.Basket',
        related_name='order',
        verbose_name=_('basket')
    )
    status = FSMIntegerField(
        verbose_name=_('status'),
        choices=STATUS_CHOICES, default=STATUS_CREATED
    )

    is_payed = models.BooleanField(
        verbose_name=_('is payed'),
        default=False
    )

    payment_type = models.IntegerField(
        verbose_name=_('payment type'),
        choices=PAYMENT_TYPE_CHOICES,
        default=PAYMENT_CASH_TO_COURIER
    )

    payment = models.OneToOneField(
        Payment,
        related_name='order',
        editable=False,
        **nullable
    )

    delivery_date = models.DateField(
        _('delivery date')
    )

    delivery_time_period = models.PositiveIntegerField(
        choices=DELIVERY_PERIODS,
        blank=True,
        null=True
    )

    exact_delivery_time = models.TimeField(
        _('exact delivery time'),
        blank=True,
        null=True
    )

    card_type = models.PositiveIntegerField(
        _('card type'),
        choices=CARD_TYPES,
        default=CARD_TYPE_FREE
    )

    card_text = models.TextField(
        _('card\'s text'),
        blank=True
    )

    sender = models.CharField(_('sender'), max_length=255)
    sender_phone = models.CharField(_('sender\'s phone'), max_length=255)
    sender_email = models.EmailField(_('sender\'s e-mail'), blank=True)
    sender_address = models.CharField(_('sender\'s address'), max_length=255,
                                      blank=True)

    sender_comment = models.TextField(
        _('sender comment'),
        blank=True
    )

    receiver = models.CharField(_('receiver'), max_length=255, blank=True)
    receiver_phone = models.CharField(_('receiver\'s phone'), max_length=255,
                                      blank=True)
    receiver_email = models.EmailField(_('receiver\'s e-mail'), blank=True)
    receiver_address = models.CharField(_('receiver\'s address'),
                                        max_length=255, blank=True)
    receiver_comment = models.TextField(
        _('receiver comment'),
        blank=True
    )

    our_comment = models.TextField(
        _('our comment'),
        blank=True
    )

    promocode = models.CharField(_('coupon'), max_length=30, blank=True)
    promocode_value = models.IntegerField(
        _('value'),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Coupon value'),
        **nullable)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return '#{} {}'.format(self.order_id, self.sender)

    @classmethod
    def get_max_order_id(cls):
        return cls.objects.aggregate(Max('order_id'))['order_id__max'] or 0

    def clean(self):
        if self.order_id == 0:
            self.order_id = self.get_max_order_id() + 1

    def get_delivery_price(self):
        if self.delivery_time_period:
            base_delivery_price = DELIVERY_COST_MAPPING[
                self.delivery_time_period]
            if self.exact_delivery_time:
                return base_delivery_price + EXACT_TIME_DELIVERY_COST
            return base_delivery_price
        return 0

    def get_card_price(self):
        for item in self.basket.items.all():
            if getattr(item, 'content_object', False):
                for _type in item.content_object.types.all():
                    if getattr(_type, 'it_is_card', False):
                        return 0
        return CARD_PRICE_MAPPING[self.card_type]

    def get_full_price(self):
        basket_price = self.basket.get_full_price()
        card_price = self.get_card_price()
        delivery_price = self.get_delivery_price()
        base_price = basket_price + card_price + delivery_price

        if self.promocode_value:
            return base_price * (100 - self.promocode_value) / 100
        return base_price

    def get_formatted_price(self):
        return mark_safe('{}&nbsp;₽'.format(self.get_full_price()))

    @classmethod
    def get_order_price_from_request(cls, request):
        delivery_time_period = request.POST.get('delivery_time_period')
        if not delivery_time_period:
            delivery_time_period = FREE_DELIVERY_PERIOD
        instance = cls(
            basket=request.basket,
            delivery_time_period=int(delivery_time_period),
            exact_delivery_time=request.POST.get('exact_delivery_time'),
            card_type=int(request.POST.get('card_type', CARD_TYPE_FREE))
        )
        return instance.get_full_price()

    def get_payment_url(self):
        return reverse('orders:payment', kwargs={'id': self.id})

    def send_notifications(self):
        if settings.SEND_NOTIFICATIONS:
            for email in settings.NOTIFICATION_EMAILS:
                send_notification.delay(
                    to=email,
                    subject='Новый заказ',
                    template_name='emails/new_order.html',
                    context={
                        'order': self
                    }
                )


def update_order_status_receiver(**kwargs):
    print kwargs
    logger.info(kwargs)


payment_completed.connect(update_order_status_receiver)
payment_process.connect(update_order_status_receiver)
