# -*- coding: utf-8 -*-
from django.conf.urls import url

from apps.pages.views import (AboutUsPageView, ContactsPage, CorporatePage,
                              CreateCallbackView, DeliveryPage,
                              FeedbackPageView, WarrantyPage)

urlpatterns = [
    url(r'about/$', AboutUsPageView.as_view(), name='about'),
    url(r'feedback/$', FeedbackPageView.as_view(), name='feedback'),
    url(r'callback/$', CreateCallbackView.as_view(), name='callback'),
    url(r'delivery/$', DeliveryPage.as_view(), name='delivery'),
    url(r'warranty/$', WarrantyPage.as_view(), name='warranty'),
    url(r'corporate/$', CorporatePage.as_view(), name='corporate'),
    url(r'contacts/$', ContactsPage.as_view(), name='contacts'),

]
