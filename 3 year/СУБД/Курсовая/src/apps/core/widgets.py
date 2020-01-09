# -*- coding: utf-8 -*-

from django import forms
from django.template.loader import render_to_string

from apps.bouquets.models import Bouquet


class BouquetBlockWidget(forms.Select):

    def _get_selected_blocks(self):
        selected_block = Bouquet.objects.filter(block__isnull=False) \
            .values_list('block', flat=True)

        dict_keys = dict(Bouquet.BLOCK_CHOICES).keys()
        result = dict.fromkeys(dict_keys)
        result.update(dict(zip(selected_block, selected_block)))
        return result

    def render(self, name, value, attrs=None, choices=()):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        options = self.render_options(choices, [value])
        context = {
            'attrs': final_attrs,
            'options': options,
            'value': value,
            'selected_blocks': self._get_selected_blocks()
        }
        return render_to_string(
            'admin/select_block_widget.html',
            dictionary=context
        )
