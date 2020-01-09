# -*- coding: utf-8 -*-
from adminsortable.models import Sortable
from colorful.fields import RGBColorField
from django import forms
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from apps.core import GenericModel, PathAndRename, nullable
from apps.core.models import UsedInFiltersMixin

photo_dir = PathAndRename('flowers/')


@python_2_unicode_compatible
class Flower(Sortable, UsedInFiltersMixin, GenericModel):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255
    )

    color = RGBColorField(
        verbose_name=_('color'),
    )

    description = models.TextField(
        verbose_name=_('description'),
        **nullable
    )

    image = models.ImageField(
        _('image'),
        upload_to=photo_dir,
        **nullable
    )

    class Meta(Sortable.Meta):
        verbose_name = _('flower')
        verbose_name_plural = _('flowers')

    def __str__(self):
        return self.title

    def clean(self):
        if self.uses_in_filters and not self.image:
            raise forms.ValidationError('You cannot use in filters flowers '
                                        'without image')
