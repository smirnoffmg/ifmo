# -*- coding: utf-8 -*-
from itertools import chain

from django import forms
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _

from apps.bouquets.models import Bouquet, BouquetColor
from apps.goods.models import Item
from apps.orders.models import Order


class CreateOrderForm(forms.ModelForm):
    delivery_date = forms.DateField(
        label=_('delivery date'),
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'data-provide': 'datepicker',
                'data-date-format': 'dd/mm/yyyy'
            }
        )
    )

    class Meta:
        model = Order
        exclude = ('basket',)

    def __init__(self, *args, **kwargs):
        super(CreateOrderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field.required:
                field.widget.attrs['required'] = True


def get_item_choices():
    return list(chain(
        Bouquet.objects.values_list('pk', 'title'),
        Item.objects.values_list('pk', 'title')
    ))


def get_initial_item_choice():
    return get_item_choices()[0]


def get_price_by_pk(pk):
    for item in chain(Bouquet.objects.all(), Item.objects.all()):
        if str(item.pk) == str(pk):
            return item.get_final_price()


class BasketPositionForm(forms.Form):
    item = forms.ChoiceField(
        choices=lazy(get_item_choices, tuple),
        initial=lazy(get_initial_item_choice, tuple),
    )

    color = forms.ModelChoiceField(
        queryset=BouquetColor.objects.all()
    )

    quantity = forms.IntegerField(
        initial=1,
        widget=forms.NumberInput(
            attrs={'style': 'width: 100%'}
        )
    )

    one_item_price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'style': 'width: 100%'}
        )
    )
    item_full_price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'readonly': True,
                'style': 'width: 100%'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial')
        super(BasketPositionForm, self).__init__(*args, **kwargs)

        if initial.get('item'):
            initial_item_pk = initial.get('item')
        else:
            initial_item_pk = self.fields['item'].initial()[0]

        colors_queryset = BouquetColor.objects.filter(
            bouquets__in=[initial_item_pk]
        )

        self.fields['color'].queryset = colors_queryset

        if colors_queryset.exists():
            self.fields['color'].initial = colors_queryset.first()

        item_price = get_price_by_pk(initial_item_pk)
        self.fields['one_item_price'].initial = item_price
        self.fields['item_full_price'].initial = item_price
