from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from .models import *
from django import forms


class UrlInline(admin.TabularInline):
    model = UrlSet.url_set.through


class UrlSetAdmin(admin.ModelAdmin):
    exclude = ("url_set",)
    inlines = [
        UrlInline,
    ]


class UrlAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return False


admin.site.register(Url, UrlAdmin)
admin.site.register(UrlSet, UrlSetAdmin)
