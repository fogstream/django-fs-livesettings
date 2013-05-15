# coding=utf-8

from django.contrib import admin

from livesettings import models as _models
from livesettings import forms as _forms


class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'type', 'value')
    fields = ('key', 'type', 'value')
    readonly_fields = ('key', 'type')
    form = _forms.SettingAdminForm
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(_models.Setting, SettingAdmin)
