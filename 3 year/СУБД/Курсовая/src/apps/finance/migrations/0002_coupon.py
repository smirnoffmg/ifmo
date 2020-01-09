# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('active', models.BooleanField(default=True,
                                               db_index=True, verbose_name='is active')),
                ('value',
                 models.IntegerField(help_text='Coupon value',
                                     verbose_name='Value',
                                     validators=[django.core.validators.MinValueValidator(0),
                                                 django.core.validators.MaxValueValidator(100)])),
                (
                    'code',
                    models.CharField(
                        help_text='Leaving this field empty will generate a random code.',
                        unique=True,
                        max_length=30,
                        verbose_name='Code',
                        blank=True)),
                (
                    'valid_until',
                    models.DateTimeField(
                        help_text='Leave empty for coupons that never expire',
                        null=True,
                        verbose_name='Valid until',
                        blank=True)),
                (
                    'max_redemptions',
                    models.PositiveIntegerField(
                        help_text='Maximum number of times this coupon can be redeemed, in total, before it is no longer valid.',
                        null=True,
                        verbose_name='max redemptions',
                        blank=True)),
                ('times_redeemed',
                 models.PositiveIntegerField(default=0,
                                             help_text='Number of times this coupon has been applied',
                                             verbose_name='times redeemed')),
            ],
            options={
                'verbose_name': 'coupon',
                'verbose_name_plural': 'coupons',
            },
        ),
    ]
