# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(
                related_name='order',
                null=True,
                blank=True,
                editable=False,
                to='yandex_money.Payment'),
        ),
    ]
