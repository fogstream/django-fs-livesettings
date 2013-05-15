# coding=utf-8

from django.contrib import admin

from livesettings import models as _models
from livesettings import forms as _forms
from livesettings import settings as _settings
from livesettings import types as _types


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


def init_livesettings():
    keys = []
    for conf_item in _settings.CONF:
        key = conf_item[0]
        setting, created = _models.Setting.objects.get_or_create(key=key)
        type = conf_item[1]
        assert type in _types.TYPES
        if setting.type != type:
            setting.type = type
            setting.value = None
            setting.save()
        keys.append(key)
    _models.Setting.objects.exclude(key__in=keys).delete()


init_livesettings()
