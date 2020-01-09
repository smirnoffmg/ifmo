# -*- coding: utf-8 -*-
import datetime
import json
from collections import Counter, defaultdict

from braces.views import LoginRequiredMixin
from cache_utils.decorators import cached
from django.views.generic import TemplateView

from apps.basket.models import BasketItem
from apps.orders.models import Order


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        data = super(DashboardView, self).get_context_data(**kwargs)
        data.update({
            'popular_in_basket_data': self.get_popular_in_basket_data(),
            'popular_in_order_data': self.get_popular_in_order_data(),
            'orders_per_day_data': self.get_orders_per_day_data(),
            'money_per_day_data': self.get_money_per_day_data()
        })
        return data

    @cached(60)
    def get_popular_in_basket_data(self):
        result = []
        items = [item.content_object for item in BasketItem.objects.all()]
        counter = Counter(items)
        for key, value in counter.most_common(5):
            if key:
                result.append({
                    'title': key.title,
                    'count': value
                })
        return json.dumps(result)

    @cached(60)
    def get_orders_per_day_data(self):
        first_day = datetime.datetime.now() - datetime.timedelta(days=14)
        result = []
        temp_result = defaultdict(int)

        for order in Order.objects.filter(created_at__gte=first_day):
            temp_result[order.created_at.strftime('%Y-%m-%d')] += 1

        for key, value in dict(temp_result).iteritems():
            result.append({
                'day': key,
                'orders': value
            })
        return json.dumps(result)

    @cached(60)
    def get_money_per_day_data(self):
        first_day = datetime.datetime.now() - datetime.timedelta(days=14)
        one_day = datetime.timedelta(days=1)
        result = []

        for offset in range(15):
            day = (first_day + datetime.timedelta(days=offset)).date()
            _sum = 0
            _payed = 0
            for order in Order.objects.filter(created_at__gte=day,
                                              created_at__lte=day + one_day):
                _sum += order.get_full_price()
                if order.is_payed:
                    _payed += order.get_full_price()

            result.append({
                'day': day.strftime('%Y-%m-%d'),
                'ordered': _sum,
                'payed': _payed
            })

        return json.dumps(result)

    @cached(60)
    def get_popular_in_order_data(self):
        result = []
        items = [item.content_object for item in
                 BasketItem.objects.filter(basket__order__isnull=False)]
        counter = Counter(items)
        for key, value in counter.most_common(5):
            if key:
                result.append({
                    'title': key.title,
                    'count': value
                })
        return json.dumps(result)
