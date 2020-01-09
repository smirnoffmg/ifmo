# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView

from apps.crm.base import CRMListView
from apps.customers.models import Customer


class CustomersListView(CRMListView):
    model = Customer
    template_name = 'crm/customers/list.html'
    context_object_name = 'customers'
    list_url = reverse_lazy('crm:customers:list')

    def get_queryset(self):
        return super(CustomersListView, self).get_queryset().order_by('id')


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'crm/customers/detail.html'
    context_object_name = 'customer'
