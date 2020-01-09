# -*- coding: utf-8 -*-


def basket_context_processor(request):
    return {
        'basket': request.basket
    }
