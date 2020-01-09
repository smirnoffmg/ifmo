# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apps.crm.models import CRMFile


@admin.register(CRMFile)
class CRMFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'created_at', 'updated_at')
