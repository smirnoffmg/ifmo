# -*- coding: utf-8 -*-
from itertools import chain

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import F
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from apps.bouquets.models import Bouquet, BouquetColor
from apps.core import nullable
from apps.core.models import GenericModel
from apps.crm.exceptions import ItemNotFoundException
from apps.goods.models import Item


class Basket(GenericModel):
    session = models.CharField(
        _('session key'),
        max_length=255
    )

    class Meta:
        ordering = ('-created_at',)

    def get_full_price(self):
        return sum(map(lambda x: x.get_full_price(), self.items.all()))

    def add_item(self, obj_id, ct_id, quantity=1, color=None, price=None):
        obj_ct = ContentType.objects.get(id=ct_id)

        if color and isinstance(color, basestring):
            color = BouquetColor.objects.get(pk=color)
        else:
            color = None

        if quantity and not isinstance(quantity, int):
            quantity = int(quantity)
        else:
            quantity = 1

        if price and not isinstance(price, float):
            price = float(price)
        else:
            price = None

        if self.items.filter(object_id=obj_id, content_type=obj_ct,
                             color=color).exists():
            self.items.filter(object_id=obj_id, content_type=obj_ct,
                              color=color).update(
                quantity=F('quantity') + quantity
            )
        else:
            self.items.create(
                content_type=obj_ct,
                object_id=obj_id,
                quantity=quantity,
                color=color,
                price=price
            )

    def add_bulk_from_crm(self, pks, quantities, prices, colors):
        assert len(pks) == len(quantities) == len(prices) == len(colors) > 0

        def get_item_id_and_ct_pair(pk):
            for item in chain(Bouquet.objects.all(), Item.objects.all()):
                if str(item.pk) == str(pk):
                    return item.get_ct_pair()
            raise ItemNotFoundException('Item with pk={} not found'.format(pk))

        for pk, quantity, price, color in zip(pks, quantities, prices, colors):
            obj_id, ct_id = get_item_id_and_ct_pair(pk)
            self.add_item(obj_id, ct_id, quantity, color, price)

    @classmethod
    def from_request(cls, request):
        session_key = request.session.session_key
        basket = cls.objects.create(session=session_key)
        request.basket = basket
        return basket

    def get_formatted_price(self):
        return mark_safe('{}&nbsp;₽'.format(self.get_full_price()))

    def freeze_prices(self):
        for item in self.items.all():
            item.price = item.get_price()
            item.save()


class BasketItem(GenericModel):
    basket = models.ForeignKey(Basket, related_name='items')

    content_type = models.ForeignKey(ContentType)
    object_id = models.UUIDField()
    content_object = GenericForeignKey('content_type', 'object_id')

    price = models.FloatField(_('price'), **nullable)
    title = models.CharField(_('title'), max_length=255, **nullable)
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    color = models.ForeignKey('bouquets.BouquetColor', **nullable)

    class Meta:
        verbose_name = _('basket item')
        verbose_name_plural = _('basket items')

    def __str__(self):
        if self.title:
            return self.title
        return self.content_object.title

    def get_price(self):
        obj = self.content_object
        if obj:
            return obj.get_final_price()
        return self.price

    def get_full_price(self):
        return self.get_price() * self.quantity

    def get_formatted_price(self):
        return mark_safe('{}&nbsp;₽'.format(self.get_full_price()))
