# -*- coding: utf-8 -*-

from django.conf.urls import url

from apps.goods.views import ItemView

urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+)/$', ItemView.as_view(), name='detail'),
]
