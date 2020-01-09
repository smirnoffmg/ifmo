# -*- coding: utf-8 -*-
from django import forms
from django.forms.fields import ChoiceField


class ModelChoiceIteratorWithContext(forms.models.ModelChoiceIterator):

    def choice(self, obj):
        return (self.field.prepare_value(obj),
                self.field.label_from_instance(obj), obj)


class ModelMultipleChoiceFieldWithContext(forms.ModelMultipleChoiceField):

    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices

        return ModelChoiceIteratorWithContext(self)

    choices = property(_get_choices, ChoiceField._set_choices)
