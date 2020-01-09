# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

import sorl.thumbnail.fields
from django.db import migrations, models

import apps.core.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(null=True,
                                          blank=True, unique=True, verbose_name='slug')),
                ('content', models.TextField(null=True,
                                             verbose_name='content', blank=True)),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('discount_price', models.IntegerField(
                    default=0, verbose_name='discount price')),
                ('favourite', models.BooleanField(
                    default=False, verbose_name='favourite')),
                ('discount', models.BooleanField(
                    default=False, verbose_name='discount')),
                ('meta_keywords', models.CharField(help_text='<meta name="keywords">',
                                                   max_length=255, null=True, verbose_name='SEO keywords', blank=True)),
                ('meta_description',
                 models.CharField(help_text='<meta name="description">',
                                  max_length=255,
                                  null=True,
                                  verbose_name='SEO description',
                                  blank=True)),
                ('show_in_additional_goods_block',
                 models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='ItemPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', sorl.thumbnail.fields.ImageField(
                    upload_to=apps.core.utils.PathAndRename('items/'))),
            ],
            options={
                'verbose_name': 'item photo',
                'verbose_name_plural': 'item photos',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('uses_in_filters', models.BooleanField(
                    default=True, verbose_name='uses in filters')),
                ('order', models.PositiveIntegerField(
                    default=1, editable=False, db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(null=True,
                                                 verbose_name='description', blank=True)),
                ('it_is_card', models.BooleanField(
                    default=False, verbose_name='it is card type')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'item type',
                'verbose_name_plural': 'item types',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='photos',
            field=models.ManyToManyField(
                help_text='No more than three',
                related_name='items',
                verbose_name='photos',
                to='goods.ItemPhoto'),
        ),
        migrations.AddField(
            model_name='item',
            name='types',
            field=models.ManyToManyField(
                related_name='bouquets',
                verbose_name='types',
                to='goods.ItemType'),
        ),
    ]
