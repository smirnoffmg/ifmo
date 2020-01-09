# -*- coding: utf-8 -*-

import logging

from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from apps.core import GenericModel
from apps.crm.utils import formatted_phone

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class Customer(GenericModel):
    name = models.CharField(_('name'), max_length=255)
    phone = models.CharField(_('phone'), max_length=255)
    email = models.EmailField(_('email'), blank=True)
    address = models.TextField(_('address'))

    orders_as_sender = models.PositiveIntegerField(editable=False, default=0)
    orders_as_receiver = models.PositiveIntegerField(editable=False, default=0)

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __str__(self):
        return self.name

    def clean(self):
        if self.phone:
            try:
                self.phone = formatted_phone(self.phone)
            except Exception as err:
                logger.error(err, exc_info=True)
