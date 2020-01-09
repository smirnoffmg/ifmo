# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sberbank_order_id',
            field=models.CharField(max_length=255, editable=False, blank=True),
        ),
    ]
