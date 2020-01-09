# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.crm.orders.views import (OrderCreateView, OrderDetailView,
                                   OrdersListView, add_basket_item_row)

urlpatterns = [
    url(r'^$', OrdersListView.as_view(), name='list'),
    url(r'^create/$', OrderCreateView.as_view(), name='create'),
    url(r'^add-basket-position/$',
        add_basket_item_row,
        name='add-basket-position'),
    url(r'^(?P<pk>[^/]+)/$', OrderDetailView.as_view(),
        name='detail'),
]
