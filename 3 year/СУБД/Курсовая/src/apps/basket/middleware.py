# -*- coding: utf-8 -*-
from apps.basket.models import Basket


class BasketMiddleware(object):

    def process_request(self, request):
        if not request.session.session_key:
            request.session.save()

        if not hasattr(request, 'basket'):
            baskets = Basket.objects.filter(
                session=request.session.session_key)
            if baskets.exists():
                request.basket = baskets.first()
            else:
                request.basket = Basket.from_request(request)

        request.session['basket_id'] = str(request.basket.id)
