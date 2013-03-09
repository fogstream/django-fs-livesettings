# coding=utf-8

from django.db import connections

from livesettings import settings as _settings
from livesettings import models as _models


def model_installed(model):
    opts = model._meta
    connection = connections['default']
    tables = connection.introspection.table_names()
    converter = connection.introspection.table_name_converter
    return ((converter(opts.db_table) in tables) or (opts.auto_created and converter(opts.auto_created._meta.db_table) in tables))


def init_livesettings():
    if not model_installed(_models.Setting):
        return

    key_list = []
    for type_key_item in _settings.TYPE_KEY_LIST:
        key = type_key_item[1]
        setting, created = _models.Setting.objects.get_or_create(key=key)
        type = type_key_item[0]
        if setting.type != type:
            setting.type = type
            setting.save()
        key_list.append(key)
    _models.Setting.objects.exclude(key__in=key_list).delete()


init_livesettings()
