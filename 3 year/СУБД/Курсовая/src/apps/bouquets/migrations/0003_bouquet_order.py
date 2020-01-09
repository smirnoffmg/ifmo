# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouquets', '0002_auto_20160320_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='order',
            field=models.PositiveIntegerField(
                default=0, editable=False, db_index=True),
        ),
    ]
