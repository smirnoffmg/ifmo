# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView

from apps.crm.base import CRMListView
from apps.finance.forms import FinanceOperationCreateForm
from apps.finance.models import FinanceOperation


class FinanceListView(CRMListView):
    model = FinanceOperation
    template_name = 'crm/finance/list.html'
    context_object_name = 'operations'
    list_url = reverse_lazy('crm:finance:list')
    create_url = reverse_lazy('crm:finance:create')

    def get_queryset(self):
        qs = super(FinanceListView, self).get_queryset()
        query = self.get_search_query()
        if query:
            filter_query = Q(amount__contains=query) | \
                Q(order__sender__contains=query) | \
                Q(order__sender_phone__contains=query) | \
                Q(order__sender_email__contains=query) | \
                Q(order__sender_address__contains=query) | \
                Q(order__sender_comment__contains=query) | \
                Q(order__receiver__contains=query) | \
                Q(order__receiver_phone__contains=query) | \
                Q(order__receiver_email__contains=query) | \
                Q(order__receiver_address__contains=query) | \
                Q(order__receiver_comment__contains=query) | \
                Q(order__our_comment__contains=query)
            qs = qs.filter(filter_query)
        return qs


class FinanceCreateView(LoginRequiredMixin, CreateView):
    model = FinanceOperation
    form_class = FinanceOperationCreateForm
    template_name = 'crm/finance/create.html'
    success_url = reverse_lazy('crm:finance:list')
