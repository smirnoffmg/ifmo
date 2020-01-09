# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import traceback

import ujson as json
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.cache import patch_response_headers

logger = logging.getLogger(__name__)


class DisableAdditionalBlocksMixin(object):

    def get_context_data(self, **kwargs):
        context = super(DisableAdditionalBlocksMixin, self).get_context_data(
            **kwargs)
        context.update({
            'disable_additional_blocks': True
        })
        return context


class PartialResponseMixin(object):
    partial_template_name = None

    def get(self, request, *args, **kwargs):
        base_response = super(PartialResponseMixin, self).get(
            request,
            *args,
            **kwargs)
        if request.is_ajax():
            return self.render_json_to_response()
        return base_response

    def get_partial_template_name(self):
        if self.partial_template_name is None:
            raise ImproperlyConfigured(
                'PartialResponseMixin requires either a definition of '
                "'partial_template_name' or an implementation of 'get_partial"
                "_template_name()'")
        else:
            return self.partial_template_name

    def get_json_content(self):
        return render_to_string(
            self.get_partial_template_name(),
            dictionary=self.get_context_data()
        )

    def render_json_to_response(self):
        result = {
            'success': True,
            'errors': [],
            'path': self.request.get_full_path()
        }

        try:
            result.update({
                'content': self.get_json_content()
            })
        except Exception as err:
            traceback.print_exc()
            result.update({
                'success': False,
                'errors': [str(err)]
            })
        finally:
            return HttpResponse(
                json.dumps(result),
                content_type='application/json'
            )


class CacheControlMixin(object):
    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        response = super(CacheControlMixin, self).dispatch(*args, **kwargs)
        patch_response_headers(response, self.get_cache_timeout())
        return response
