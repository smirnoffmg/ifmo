# -*- coding: utf-8 -*-
from adminsortable.admin import SortableAdmin
from django.contrib import admin

from apps.goods.models import Item, ItemPhoto, ItemType


@admin.register(ItemType)
class ItemTypeAdmin(SortableAdmin):
    list_display = ('title', 'it_is_card')
    list_filter = ('it_is_card',)


@admin.register(ItemPhoto)
class ItemPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'alt_title')
    search_fields = ('title',)


@admin.register(Item)
class ItemAdmin(SortableAdmin):
    list_display = (
        'title', 'price', 'discount_price', 'discount',
        'show_in_additional_goods_block')
    list_filter = ('show_in_additional_goods_block', 'discount')
    filter_horizontal = ('types', 'photos')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
