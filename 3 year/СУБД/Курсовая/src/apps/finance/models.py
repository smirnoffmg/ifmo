# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from apps.core import GenericModel, nullable
from apps.orders.models import Order

CODE_CHARS = getattr(settings, 'COUPONS_CODE_CHARS',
                     string.ascii_letters + string.digits)

CODE_LENGTH = getattr(settings, 'COUPONS_CODE_LENGTH', 15)


@python_2_unicode_compatible
class FinanceOperation(GenericModel):
    TYPE_INCOMING = 1
    TYPE_OUTCOMING = 2
    OPERATION_TYPES = (
        (TYPE_INCOMING, _('incoming')),
        (TYPE_OUTCOMING, _('outcoming'))
    )

    amount = models.FloatField(_('amount'), default=0.0)
    type = models.PositiveIntegerField(
        _('type'),
        choices=OPERATION_TYPES,
        default=TYPE_INCOMING)

    order = models.ForeignKey(
        Order,
        related_name='finance_operations',
        verbose_name=_('order'),
        **nullable
    )

    def __str__(self):
        return '{} {}'.format(self.amount, self.get_type_display())


@python_2_unicode_compatible
class Coupon(GenericModel):
    active = models.BooleanField(_('is active'), default=True, db_index=True)

    value = models.IntegerField(
        _('Value'),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text=_('Coupon value'))

    code = models.CharField(
        _('Code'), max_length=30,
        help_text=_('Leaving this field empty will generate a random code.'),
        unique=True,
        blank=True
    )

    valid_until = models.DateTimeField(
        _('Valid until'),
        help_text=_('Leave empty for coupons that never expire'),
        **nullable)

    max_redemptions = models.PositiveIntegerField(
        _('max redemptions'),
        help_text=_('Maximum number of times this coupon can be redeemed, '
                    'in total, before it is no longer valid.'),
        **nullable
    )

    times_redeemed = models.PositiveIntegerField(
        _('times redeemed'),
        help_text='Number of times this coupon has been applied',
        default=0
    )

    class Meta:
        verbose_name = _('coupon')
        verbose_name_plural = _('coupons')

    def __str__(self):
        return '{} ({})'.format(self.code, self.value)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = Coupon.generate_code()

        super(Coupon, self).save(*args, **kwargs)

    @classmethod
    def generate_code(cls, prefix=''):
        code = ''.join(random.choice(CODE_CHARS) for i in range(CODE_LENGTH))
        return prefix + code

    def increase_times_redeemed(self):
        self.times_redeemed += 1

        if self.max_redemptions and self.times_redeemed >= self.max_redemptions:
            self.active = False

        self.save(update_fields=['times_redeemed', 'active'])
