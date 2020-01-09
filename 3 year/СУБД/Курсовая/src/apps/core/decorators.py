# -*- coding: utf-8 -*-

import ujson as json
from django.http import HttpResponse, HttpResponseBadRequest


def ajax(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        result = f(request, *args, **kwargs)
        return HttpResponse(
            json.dumps(result),
            content_type='application/json'
        )

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
