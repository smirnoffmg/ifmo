# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from urlparse import urljoin

from adminsortable.models import Sortable
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

from apps.core import GenericModel, PathAndRename, nullable
from apps.core.models import (BaseCatalogueItem, BaseCataloguePhoto, SeoMixin,
                              UsedInFiltersMixin)
from apps.core.utils import invalidate_template_fragment

items_photo_dir = PathAndRename('items/')
DOMAIN_NAME = getattr(settings, 'DOMAIN_NAME', 'http://127.0.0.1:8000/')


@python_2_unicode_compatible
class ItemPhoto(BaseCataloguePhoto):
    image = ImageField(upload_to=items_photo_dir)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('item photo')
        verbose_name_plural = _('item photos')


@python_2_unicode_compatible
class ItemType(Sortable, UsedInFiltersMixin, GenericModel):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_('description'),
        **nullable
    )

    it_is_card = models.BooleanField(
        verbose_name=_('it is card type'),
        default=False
    )

    def __str__(self):
        return self.title

    class Meta(Sortable.Meta):
        verbose_name = _('item type')
        verbose_name_plural = _('item types')


@python_2_unicode_compatible
class Item(Sortable, SeoMixin, BaseCatalogueItem):
    types = models.ManyToManyField(
        ItemType,
        verbose_name=_('types'),
        related_name='bouquets'
    )

    photos = models.ManyToManyField(
        ItemPhoto,
        verbose_name=_('photos'),
        related_name='items',
        help_text=_('No more than three')
    )

    show_in_additional_goods_block = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('goods:detail', kwargs={'slug': self.slug})

    # opengraph

    def get_og_image(self):
        photo = self.photos.first().image
        url = urljoin(DOMAIN_NAME, photo.url)
        return url


@receiver(post_save, sender=Item)
def update_item_related_cache(instance, **kwargs):
    instance.invalidate_template_fragment_cache()

    if instance.show_in_additional_goods_block:
        invalidate_template_fragment('additional_block_items')


@receiver(post_save, sender=ItemPhoto)
def update_item_photo_related_cache(instance, **kwargs):
    for item in instance.items.all():
        item.invalidate_template_fragment_cache()

        if item.show_in_additional_goods_block:
            invalidate_template_fragment('additional_block_items')
