# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import migrations, models

import apps.core.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRMFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4,
                                        serialize=False, editable=False, primary_key=True)),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created', db_index=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated', db_index=True)),
                ('file', models.FileField(
                    upload_to=apps.core.utils.PathAndRename('bouquets/'))),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
    ]
