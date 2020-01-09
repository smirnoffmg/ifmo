# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.utils.functional import curry

from apps.crm.views import DashboardView

login = curry(login, template_name='crm/login.html')
urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^orders/', include('apps.crm.orders.urls', namespace='orders')),
    url(r'^customers/',
        include('apps.crm.customers.urls', namespace='customers')),
    url(r'^finance/', include('apps.crm.finance.urls', namespace='finance')),
    url(r'^files/', include('apps.crm.files.urls', namespace='files')),
]
