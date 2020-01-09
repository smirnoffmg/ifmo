# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from urlparse import urljoin

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail

from apps.core.utils import invalidate_template_fragment, nullable
from apps.opengraph.models import OpenGraphMixin

DOMAIN_NAME = getattr(settings, 'DOMAIN_NAME', 'http://127.0.0.1:8000/')


class GenericModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        verbose_name=_('created'),
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(
        verbose_name=_('updated'),
        auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['created_at', 'updated_at']
        get_latest_by = 'created_at'

    def get_content_type(self):
        return ContentType.objects.get_for_model(self)


class UsedInFiltersMixin(models.Model):
    uses_in_filters = models.BooleanField(
        _('uses in filters'),
        default=True
    )

    class Meta:
        abstract = True


class BaseCatalogueItem(OpenGraphMixin, GenericModel):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255
    )

    slug = models.SlugField(
        verbose_name=_('slug'),
        unique=True,
        **nullable
    )

    content = models.TextField(
        verbose_name=_('content'),
        **nullable
    )

    price = models.IntegerField(
        verbose_name=_('price'),
        default=0
    )

    discount_price = models.IntegerField(
        verbose_name=_('discount price'),
        default=0
    )

    favourite = models.BooleanField(
        _('favourite'),
        default=False
    )

    discount = models.BooleanField(
        _('discount'),
        default=False
    )

    class Meta:
        abstract = True

    def get_final_price(self):
        if self.discount:
            return self.discount_price
        return self.price

    def get_photo(self):
        if hasattr(self, 'photos'):
            if self.photos.exists():
                return self.photos.first()
        return None

    def get_thumb(self):
        photo = self.get_photo()
        if photo:
            return photo.get_big_thumb()
        return None

    def has_measure_units(self):
        return False

    def has_colors(self):
        return False

    def get_description_title(self):
        return 'Описание:'

    def get_ct_pair(self):
        return str(self.pk), str(self.get_content_type().pk)

    def invalidate_template_fragment_cache(self):
        invalidate_template_fragment('bouquet_snippet', self.pk)

    # opengraph

    def get_og_title(self):
        return self.title

    def get_og_description(self):
        return self.content

    def get_og_url(self):
        url = urljoin(DOMAIN_NAME, self.get_absolute_url())
        return url


class BaseCataloguePhoto(GenericModel):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255
    )

    alt_title = models.CharField(
        verbose_name='<img alt="">',
        max_length=255,
        blank=True
    )

    class Meta:
        abstract = True

    def get_big_thumb(self):
        if getattr(self, 'image'):
            return get_thumbnail(
                self.image,
                '270x270',
                padding=True,
                quality=99
            )
        return None

    def get_little_thumb(self):
        if getattr(self, 'image'):
            return get_thumbnail(
                self.image,
                '157x157',
                padding=True,
                quality=99
            )
        return None


class SeoMixin(models.Model):
    meta_title = models.CharField(
        _('SEO title'),
        max_length=255,
        blank=True
    )

    meta_keywords = models.CharField(
        _('SEO keywords'),
        max_length=255,
        **nullable
    )

    meta_description = models.CharField(
        _('SEO description'),
        max_length=255,
        **nullable
    )

    class Meta:
        abstract = True

    def clean(self):
        if not self.meta_title and hasattr(self, 'title'):
            self.meta_title = self.title

        if not self.meta_keywords and hasattr(self, 'title'):
            self.meta_keywords = self.title

        if not self.meta_description and hasattr(self, 'content'):
            self.meta_description = self.content

    def get_title(self):
        if self.meta_title:
            return self.meta_title

        return 'Цветочная мастерская | доставка цветов, букетов, корзин.'

    def get_seo_title(self):
        raise NotImplementedError

    def get_seo_description(self):
        raise NotImplementedError
