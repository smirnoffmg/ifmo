# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_sberbank_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promocode',
            field=models.CharField(
                max_length=30,
                verbose_name='coupon',
                blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='promocode_value',
            field=models.IntegerField(
                blank=True,
                help_text='Coupon value',
                null=True,
                verbose_name='value',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100)]),
        ),
    ]
