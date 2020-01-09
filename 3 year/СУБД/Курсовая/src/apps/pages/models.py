# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core import GenericModel, nullable


class Feedback(GenericModel):
    phone = models.CharField(_('phone'), max_length=255, **nullable)
    fio = models.CharField(_('fio'), max_length=255, **nullable)
    email = models.EmailField(_('email'), max_length=255, **nullable)
    text = models.TextField(_('text'), **nullable)
