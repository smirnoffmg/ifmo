# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.db import migrations

from apps.crm import formatted_phone

logger = logging.getLogger(__name__)


def reformat_phones(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')

    for c in Customer.objects.all():
        try:
            c.phone = formatted_phone(c.phone)
            c.save()
        except Exception as err:
            logger.error(err, exc_info=True)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0002_fill_customers'),
    ]

    operations = [
        migrations.RunPython(reformat_phones, reverse_code=noop)
    ]
