# -*- coding: utf-8 -*-
from itertools import chain

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, TemplateView

from apps.bouquets.forms import FilterForm
from apps.bouquets.models import Bouquet
from apps.core.mixins import CacheControlMixin, PartialResponseMixin
from apps.goods.models import Item


class IndexPageView(PartialResponseMixin, TemplateView):
    template_name = 'index.html'
    partial_template_name = 'index_content.html'

    def get_blocks(self):
        result = {}
        for bouquet in Bouquet.objects.prefetch_related().filter(
                block__isnull=False):
            result[bouquet.block] = bouquet

        return result

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({
            'blocks': self.get_blocks()
        })
        return context


class CatalogueView(CacheControlMixin, PartialResponseMixin, ListView):
    model = Bouquet
    template_name = 'catalogue/list.html'
    partial_template_name = 'catalogue/list_content.html'
    context_object_name = 'bouquets'

    def get_filter_form(self):
        if self.request.GET:
            return FilterForm(self.request.GET)
        return None

    def get_filters(self):
        filter_form = self.get_filter_form()
        if filter_form:
            filter_form.full_clean()
            data = filter_form.clean()
            return data
        return None

    def get_bouquets_qs(self, filters):
        if filters:
            bouquets_filters = ['flowers', 'colors', 'types', 'prices']
            if any(i in bouquets_filters for i in filters.keys()):
                b_qs = Bouquet.objects.all()
                if 'flowers' in filters.keys():
                    b_qs = b_qs.filter(flowers__contains=filters['flowers'])

                if 'colors' in filters.keys():
                    b_qs = b_qs.filter(colors__contains=filters['colors'])

                if 'types' in filters.keys():
                    b_qs = b_qs.filter(types__contains=filters['types'])

                if 'prices' in filters.keys():
                    min_price = min(
                        map(lambda x: x.price_from, filters['prices']))
                    max_price = max(
                        map(lambda x: x.price_to, filters['prices']))

                    if min_price:
                        b_qs = b_qs.filter(price__gte=min_price)

                    if max_price:
                        b_qs = b_qs.filter(price__lte=max_price)
                return b_qs.order_by('order').distinct().all()
            return []
        return Bouquet.objects.all()

    def get_goods_qs(self, filters):
        if filters:
            if 'item_types' in filters.keys():
                g_qs = Item.objects.filter(
                    types__contains=filters['item_types'])
                return g_qs
            return []
        return Item.objects.all()

    def get_queryset(self):
        filters = self.get_filters()
        b_qs = self.get_bouquets_qs(filters)
        g_qs = self.get_goods_qs(filters)

        return chain(b_qs, g_qs)


class BouquetView(CacheControlMixin, PartialResponseMixin, DetailView):
    model = Bouquet
    template_name = 'catalogue/bouquet.html'
    partial_template_name = 'catalogue/bouquet_content.html'
    context_object_name = 'bouquet'

    def get_context_data(self, **kwargs):
        context = super(BouquetView, self).get_context_data(**kwargs)
        context.update({
            'photos': self.get_object().photos.all(),
            'colors': self.get_object().colors.all()
        })
        return context
