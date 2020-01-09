# -*- coding: utf-8 -*-

from django import forms

from apps.finance.models import FinanceOperation


class FinanceOperationCreateForm(forms.ModelForm):

    class Meta:
        model = FinanceOperation
        fields = '__all__'
