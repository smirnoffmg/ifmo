# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

import colorful.fields
from django.db import migrations, models

import apps.core.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
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
                ('color', colorful.fields.RGBColorField(verbose_name='color')),
                ('description', models.TextField(null=True,
                                                 verbose_name='description', blank=True)),
                ('image', models.ImageField(upload_to=apps.core.utils.PathAndRename(
                    b'flowers/'), null=True, verbose_name='image', blank=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name': 'flower',
                'verbose_name_plural': 'flowers',
            },
        ),
    ]
