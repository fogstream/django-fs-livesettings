# coding=utf-8

from django.contrib import admin

from . import models as _models
from . import forms as _forms


class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    fields = ('type', 'key', 'value')
    readonly_fields = ('type', 'key')
    form = _forms.SettingAdminForm
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return None


admin.site.register(_models.Setting, SettingAdmin)
