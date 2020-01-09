# -*- coding: utf-8 -*-

from django.views.generic import DetailView

from apps.goods.models import Item


class ItemView(DetailView):
    model = Item
    template_name = 'item.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({
            'photos': self.get_object().photos.all()
        })
        return context
