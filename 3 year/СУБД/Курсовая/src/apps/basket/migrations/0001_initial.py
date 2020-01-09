# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('bouquets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('session', models.CharField(
                    max_length=255, verbose_name='session key')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('object_id', models.UUIDField()),
                ('price', models.FloatField(
                    null=True, verbose_name='price', blank=True)),
                ('title', models.CharField(max_length=255,
                                           null=True, verbose_name='title', blank=True)),
                ('quantity', models.PositiveIntegerField(
                    default=1, verbose_name='quantity')),
                ('basket', models.ForeignKey(
                    related_name='items', to='basket.Basket')),
                ('color', models.ForeignKey(blank=True,
                                            to='bouquets.BouquetColor', null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'basket item',
                'verbose_name_plural': 'basket items',
            },
        ),
    ]
