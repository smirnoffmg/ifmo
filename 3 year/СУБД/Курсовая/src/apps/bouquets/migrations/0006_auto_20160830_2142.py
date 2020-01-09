# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouquets', '0005_bouquet_meta_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquetphoto',
            name='alt_title',
            field=models.CharField(
                max_length=255,
                verbose_name='<img alt="">',
                blank=True),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='meta_description',
            field=models.CharField(
                max_length=255,
                null=True,
                verbose_name='SEO description',
                blank=True),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='meta_keywords',
            field=models.CharField(
                max_length=255,
                null=True,
                verbose_name='SEO keywords',
                blank=True),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='meta_title',
            field=models.CharField(
                max_length=255,
                verbose_name='SEO title',
                blank=True),
        ),
    ]
