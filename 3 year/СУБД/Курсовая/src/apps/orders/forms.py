# -*- coding: utf-8 -*-
import datetime

from django import forms

from apps.orders.models import Order


class OrderForm(forms.ModelForm):
    delivery_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        initial=datetime.date.today()
    )

    class Meta:
        model = Order
        exclude = ('status', 'basket', )
