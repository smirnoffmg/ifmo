# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceOperation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('amount', models.FloatField(default=0.0, verbose_name='amount')),
                ('type', models.PositiveIntegerField(
                    default=1, verbose_name='type', choices=[(1, 'incoming'), (2, 'outcoming')])),
                ('order', models.ForeignKey(related_name='finance_operations',
                                            verbose_name='order', blank=True, to='orders.Order', null=True)),
            ],
            options={
                'ordering': ['created_at', 'updated_at'],
                'abstract': False,
                'get_latest_by': 'created_at',
            },
        ),
    ]
