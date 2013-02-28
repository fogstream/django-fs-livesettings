# coding=utf-8

from django.db.utils import DatabaseError

from . import settings as _settings
from . import models as _models


class LiveSettings(object):
    def __init__(self):
        try:
            _models.Setting.objects.exists()
        except DatabaseError:
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

    def __getattr__(self, name):
        try:
            _models.Setting.objects.exists()
        except DatabaseError:
            return None

        try:
            setting = _models.Setting.objects.get(key=name)
            return setting.get_value
        except _models.Setting.DoesNotExist:
            raise AttributeError('\'{0}\' object has no attribute \'{1}\''.format(type(self).__name__, name))


livesettings = LiveSettings()
