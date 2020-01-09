# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.basket.views import (BasketView, add_to_basket,
                               change_item_in_basket, change_order_details,
                               check_coupon, delete_from_basket)

urlpatterns = [
    url(r'basket/$', BasketView.as_view(), name='basket'),
    url(r'add-item/$', add_to_basket, name='add'),
    url(r'delete-item/$', delete_from_basket, name='delete'),
    url(r'change-item/$', change_item_in_basket, name='change'),
    url(r'change-order-details/$',
        change_order_details,
        name='change-order-details'),
    url(r'check-coupon/$', check_coupon, name='check-coupon')
]
