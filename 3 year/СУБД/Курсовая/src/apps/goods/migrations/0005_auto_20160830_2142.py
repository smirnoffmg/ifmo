# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_item_meta_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemphoto',
            name='alt_title',
            field=models.CharField(
                max_length=255,
                verbose_name='<img alt="">',
                blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='meta_description',
            field=models.CharField(
                max_length=255,
                null=True,
                verbose_name='SEO description',
                blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='meta_keywords',
            field=models.CharField(
                max_length=255,
                null=True,
                verbose_name='SEO keywords',
                blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='meta_title',
            field=models.CharField(
                max_length=255,
                verbose_name='SEO title',
                blank=True),
        ),
    ]
