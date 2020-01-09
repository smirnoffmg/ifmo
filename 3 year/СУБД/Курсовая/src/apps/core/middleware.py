# -*- coding: utf-8 -*-

import logging


class Sentry403CatchMiddleware(object):

    def process_response(self, request, response):
        from raven.contrib.django.models import client

        if response.status_code != 403:
            return response

        data = client.get_data_from_request(request)
        data.update({
            'level': logging.INFO,
            'logger': 'http403',
        })
        result = client.captureMessage(
            message='403 exception: %s' % request.build_absolute_uri(),
            data=data)
        if not result:
            return

        request.sentry = {
            'project_id': data.get('project', client.remote.project),
            'id': client.get_ident(result),
        }
        return response
