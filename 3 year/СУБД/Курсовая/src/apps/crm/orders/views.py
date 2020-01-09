# -*- coding: utf-8 -*-
import traceback
from uuid import uuid4

from braces.views import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView

from apps.basket.models import Basket
from apps.core.decorators import ajax
from apps.crm.base import CRMListView
from apps.crm.orders.forms import BasketPositionForm, CreateOrderForm
from apps.orders.models import Order


class OrdersListView(CRMListView):
    model = Order
    template_name = 'crm/orders/list.html'
    context_object_name = 'orders'
    ordering = '-created_at'
    list_url = reverse_lazy('crm:orders:list')
    create_url = reverse_lazy('crm:orders:create')

    def get_queryset(self):
        qs = super(OrdersListView, self).get_queryset()
        query = self.get_search_query()
        if query:
            filter_query = Q(order_id=query) | \
                Q(sender__contains=query) | \
                Q(sender_phone__contains=query) | \
                Q(sender_email__contains=query) | \
                Q(sender_address__contains=query) | \
                Q(sender_comment__contains=query) | \
                Q(receiver__contains=query) | \
                Q(receiver_phone__contains=query) | \
                Q(receiver_email__contains=query) | \
                Q(receiver_address__contains=query) | \
                Q(receiver_comment__contains=query) | \
                Q(our_comment__contains=query)
            qs = qs.filter(filter_query)
        return qs


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'crm/orders/detail.html'
    context_object_name = 'order'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'crm/orders/create.html'
    success_url = reverse_lazy('crm:orders:list')

    def form_valid(self, form):
        raw_data = self.request.POST.copy()
        old_basket = self.request.basket  # saving old basket from user session

        new_order = form.save(commit=False)
        new_basket = Basket.from_request(self.request)
        new_basket.add_bulk_from_crm(
            pks=raw_data.getlist('item'),
            quantities=raw_data.getlist('quantity'),
            prices=raw_data.getlist('one_item_price'),
            colors=raw_data.getlist('color')
        )

        new_order.basket = new_basket

        new_order.save()

        self.request.basket = old_basket

        return redirect('crm:orders:list')


@login_required
@ajax
def add_basket_item_row(request):
    result = {
        'success': True
    }

    try:
        item_pk = request.GET.get('item')

        form = BasketPositionForm(initial={'item': item_pk})
        uuid = uuid4()
        result.update({
            'content': render_to_string(
                template_name='crm/orders/basket_item_row.html',
                context={
                    'form': form,
                    'uuid': uuid
                }
            ),
            'uuid': str(uuid)
        })
    except Exception as err:
        result.update({
            'success': False,
            'error': str(err)
        })
        if settings.DEBUG:
            traceback.print_exc()
    finally:
        return result
