# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.crm.finance.views import FinanceCreateView, FinanceListView

urlpatterns = [
    url(r'^$', FinanceListView.as_view(), name='list'),
    url(r'^create/$', FinanceCreateView.as_view(), name='create'),
]
