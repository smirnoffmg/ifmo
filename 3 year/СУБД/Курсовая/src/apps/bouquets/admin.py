# -*- coding: utf-8 -*-
from adminsortable.admin import SortableAdmin
from django.contrib import admin

from apps.bouquets.forms import BouquetAdminForm
from apps.bouquets.models import (Bouquet, BouquetColor, BouquetPhoto,
                                  BouquetType, PriceCategory)


@admin.register(BouquetType)
class BouquetTypeAdmin(SortableAdmin):
    list_display = ('title',)


@admin.register(PriceCategory)
class PriceCategoryAdmin(SortableAdmin):
    list_display = ('title', 'price_from', 'price_to')


@admin.register(BouquetPhoto)
class BouquetPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'alt_title')
    search_fields = ('title',)


@admin.register(BouquetColor)
class BouquetColorAdmin(SortableAdmin):
    list_display = ('title',)


@admin.register(Bouquet)
class BouquetAdmin(SortableAdmin):
    form = BouquetAdminForm
    list_display = (
        'title', 'price', 'width',
        'height', 'weight', 'discount', 'favourite',
        'show_in_recommended_block')
    filter_horizontal = ('types', 'flowers', 'colors')
    list_filter = (
        'types', 'flowers', 'discount', 'favourite',
        'show_in_recommended_block')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
