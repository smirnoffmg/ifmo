# -*- coding: utf-8 -*-
from django.contrib import admin

from apps.pages.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('phone', 'fio', 'email')
