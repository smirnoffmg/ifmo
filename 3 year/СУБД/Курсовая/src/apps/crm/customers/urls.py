# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.crm.customers.views import CustomerDetailView, CustomersListView

urlpatterns = [
    url(r'^$', CustomersListView.as_view(), name='list'),
    url(r'^(?P<pk>[^/]+)/$', CustomerDetailView.as_view(),
        name='detail'),
]
