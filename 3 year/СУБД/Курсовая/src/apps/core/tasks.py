# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import traceback

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.utils.html import strip_tags

from flowers.celery import app

logger = logging.getLogger(__name__)


@app.task
def send_notification(to, subject, template_name, context,
                      attach=None, from_email=None):
    try:
        if not isinstance(to, list):
            to = [to]

        htmly = get_template(template_name)

        d = Context(context)

        html_content = htmly.render(d)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(
            subject,
            text_content,
            from_email or settings.DEFAULT_FROM_EMAIL,
            to)
        msg.attach_alternative(html_content, 'text/html')

        if attach:
            msg.attach_file(attach)

        msg.send()
    except Exception as err:
        traceback.print_exc()
        logger.error(err, exc_info=True)
