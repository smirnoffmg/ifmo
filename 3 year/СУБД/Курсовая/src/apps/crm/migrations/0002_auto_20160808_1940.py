# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import apps.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmfile',
            name='file',
            field=models.FileField(
                upload_to=apps.core.utils.PathAndRename('bouquets/'),
                verbose_name='file'),
        ),
    ]
