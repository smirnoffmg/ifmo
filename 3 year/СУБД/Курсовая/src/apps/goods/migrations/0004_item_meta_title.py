# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20160506_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='meta_title',
            field=models.CharField(
                help_text='<title>',
                max_length=255,
                verbose_name='SEO title',
                blank=True),
        ),
    ]
