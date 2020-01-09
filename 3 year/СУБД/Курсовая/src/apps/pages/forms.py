# -*- coding: utf-8 -*-
from django import forms

from apps.pages.models import Feedback


class FeedbackForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\+?7?\d{9,15}$')

    class Meta:
        model = Feedback
        fields = '__all__'


class CallbackForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
