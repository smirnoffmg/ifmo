# -*- coding: utf-8 -*-
from django import forms

from apps.bouquets.models import (Bouquet, BouquetColor, BouquetType,
                                  PriceCategory)
from apps.core.fields import ModelMultipleChoiceFieldWithContext
from apps.core.widgets import BouquetBlockWidget
from apps.flowers.models import Flower
from apps.goods.models import ItemType


class BouquetAdminForm(forms.ModelForm):

    class Meta:
        model = Bouquet
        fields = '__all__'
        widgets = {
            'block': BouquetBlockWidget
        }


class FilterForm(forms.Form):
    flowers = ModelMultipleChoiceFieldWithContext(
        queryset=Flower.objects.filter(uses_in_filters=True),
        widget=forms.CheckboxSelectMultiple
    )

    prices = ModelMultipleChoiceFieldWithContext(
        queryset=PriceCategory.objects.filter(uses_in_filters=True),
        widget=forms.CheckboxSelectMultiple
    )

    colors = ModelMultipleChoiceFieldWithContext(
        queryset=BouquetColor.objects.filter(uses_in_filters=True),
        widget=forms.CheckboxSelectMultiple
    )

    types = ModelMultipleChoiceFieldWithContext(
        queryset=BouquetType.objects.filter(uses_in_filters=True),
        widget=forms.CheckboxSelectMultiple
    )

    item_types = ModelMultipleChoiceFieldWithContext(
        queryset=ItemType.objects.filter(uses_in_filters=True),
        widget=forms.CheckboxSelectMultiple
    )
