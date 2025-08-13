from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_editable = ("name",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "menu", "title", "parent", "url")
    list_filter = ("menu", "parent")
    search_fields = ("title", "url")
    raw_id_fields = ("parent",)
    autocomplete_fields = ("menu", "parent")
    list_select_related = ("menu", "parent")
    ordering = ("menu", "parent", "title")
    list_editable = ("parent", "title", "url")
