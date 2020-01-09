# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bouquets', '0003_bouquet_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bouquet',
            options={
                'ordering': ['order'],
                'get_latest_by': 'created_at',
                'verbose_name': 'bouquet',
                'verbose_name_plural': 'bouquets'},
        ),
    ]
