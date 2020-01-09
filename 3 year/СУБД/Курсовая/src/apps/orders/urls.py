# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.orders.views import PaymentView

urlpatterns = [
    url(r'(?P<id>[^/]+)/payment/$', PaymentView.as_view(), name='payment')
]
