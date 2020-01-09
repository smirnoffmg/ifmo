# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.bouquets.views import BouquetView, CatalogueView

urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+)/$', BouquetView.as_view(), name='detail'),
    url(r'$', CatalogueView.as_view(), name='list'),

]
