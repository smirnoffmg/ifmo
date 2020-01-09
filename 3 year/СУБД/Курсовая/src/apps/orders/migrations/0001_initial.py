# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

import django_fsm
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('order_id', models.IntegerField(default=0, editable=False)),
                ('status', django_fsm.FSMIntegerField(default=1, verbose_name='status', choices=[
                 (1, 'created'), (2, 'confirmed'), (3, 'on delivery'), (4, 'delivered'), (5, 'cancelled')])),
                ('is_payed', models.BooleanField(
                    default=False, verbose_name='is payed')),
                (
                    'payment_type',
                    models.IntegerField(
                        default=1,
                        verbose_name='payment type',
                        choices=[
                            (1,
                             b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xbc\xd0\xb8 \xd0\xba\xd1\x83\xd1\x80\xd1\x8c\xd0\xb5\xd1\x80\xd1\x83'),
                            (2,
                             b'\xd0\x9e\xd0\xbd\xd0\xbb\xd0\xb0\xd0\xb9\xd0\xbd'),
                            (3,
                             b'\xd0\xa1\xd0\xb0\xd0\xbc\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb2\xd0\xbe\xd0\xb7 \xd0\xb8\xd0\xb7 \xd0\xbe\xd1\x84\xd0\xb8\xd1\x81\xd0\xb0'),
                            (4,
                             b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x8c\xd0\xb5\xd1\x80\xd0\xbe\xd0\xbc \xd0\xbd\xd0\xb0 \xd0\xb4\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')])),
                ('delivery_date', models.DateField(verbose_name='delivery date')),
                (
                    'delivery_time_period',
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        choices=[
                            (1,
                             b'\xd0\xa1 7 \xd0\xb4\xd0\xbe 9 \xe2\x80\x94 300 \xd1\x80\xd1\x83\xd0\xb1.'),
                            (2,
                             b'C 9 \xd0\xb4\xd0\xbe 11 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (3,
                             b'C 10 \xd0\xb4\xd0\xbe 12 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (4,
                             b'C 11 \xd0\xb4\xd0\xbe 13 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (5,
                             b'C 12 \xd0\xb4\xd0\xbe 14 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (6,
                             b'C 13 \xd0\xb4\xd0\xbe 15 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (7,
                             b'C 14 \xd0\xb4\xd0\xbe 16 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (8,
                             b'C 15 \xd0\xb4\xd0\xbe 17 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (9,
                             b'C 16 \xd0\xb4\xd0\xbe 18 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (10,
                             b'C 17 \xd0\xb4\xd0\xbe 19 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (11,
                             b'C 18 \xd0\xb4\xd0\xbe 20 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (12,
                             b'C 19 \xd0\xb4\xd0\xbe 21 \xe2\x80\x94 \xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe'),
                            (13,
                             b'\xd0\xa1 21 \xd0\xb4\xd0\xbe 23 \xe2\x80\x94 300 \xd1\x80\xd1\x83\xd0\xb1.'),
                            (14,
                             b'\xd0\xa1 23 \xd0\xb4\xd0\xbe 01 \xe2\x80\x94 600 \xd1\x80\xd1\x83\xd0\xb1.'),
                            (15,
                             b'\xd0\xa1 01 \xd0\xb4\xd0\xbe 03 \xe2\x80\x94 600 \xd1\x80\xd1\x83\xd0\xb1.'),
                            (16,
                             b'\xd0\xa1 03 \xd0\xb4\xd0\xbe 05 \xe2\x80\x94 600 \xd1\x80\xd1\x83\xd0\xb1.'),
                            (17,
                             b'\xd0\xa1 05 \xd0\xb4\xd0\xbe 07 \xe2\x80\x94 600 \xd1\x80\xd1\x83\xd0\xb1.')])),
                ('exact_delivery_time', models.TimeField(null=True,
                                                         verbose_name='exact delivery time', blank=True)),
                (
                    'card_type',
                    models.PositiveIntegerField(
                        default=1,
                        verbose_name='card type',
                        choices=[
                            (1,
                             b'\xd0\x91\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbe\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xba\xd0\xb0'),
                            (2,
                             b'\xd0\x9f\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbe\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xba\xd0\xb0')])),
                ('card_text', models.TextField(
                    verbose_name="card's text", blank=True)),
                ('sender', models.CharField(max_length=255, verbose_name='sender')),
                ('sender_phone', models.CharField(
                    max_length=255, verbose_name="sender's phone")),
                ('sender_email', models.EmailField(max_length=254,
                                                   verbose_name="sender's e-mail", blank=True)),
                ('sender_address', models.CharField(max_length=255,
                                                    verbose_name="sender's address", blank=True)),
                ('sender_comment', models.TextField(
                    verbose_name='sender comment', blank=True)),
                ('receiver', models.CharField(max_length=255,
                                              verbose_name='receiver', blank=True)),
                ('receiver_phone', models.CharField(max_length=255,
                                                    verbose_name="receiver's phone", blank=True)),
                ('receiver_email', models.EmailField(max_length=254,
                                                     verbose_name="receiver's e-mail", blank=True)),
                ('receiver_address', models.CharField(max_length=255,
                                                      verbose_name="receiver's address", blank=True)),
                ('receiver_comment', models.TextField(
                    verbose_name='receiver comment', blank=True)),
                ('our_comment', models.TextField(
                    verbose_name='our comment', blank=True)),
                ('basket', models.OneToOneField(related_name='order',
                                                verbose_name='basket', to='basket.Basket')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
    ]
