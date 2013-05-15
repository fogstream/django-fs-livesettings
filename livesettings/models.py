# coding=utf-8

from django.db import models

from livesettings import types as _types
from livesettings import settings as _settings


class Setting(models.Model):
    TYPE_CHOICES = zip(_types.TYPES, _types.TYPES)

    key = models.CharField(verbose_name=u'key', max_length=50, unique=True)
    type = models.CharField(verbose_name=u'type', max_length=50, choices=TYPE_CHOICES)
    value = models.CharField(verbose_name=u'value', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = u'setting'
        verbose_name_plural = u'settings'

    def __unicode__(self):
        return self.key

    def _get_field(self):
        return _types.TYPE_FIELD.get(self.type)

    def get_value(self):
        field = self._get_field()
        return field.to_python(self.value)

    def clean_value(self, value):
        field = self._get_field()
        return field.clean(value)


def init_livesettings():
    keys = []
    for conf_item in _settings.CONF:
        key = conf_item[0]
        setting, created = Setting.objects.get_or_create(key=key)
        type = conf_item[1]
        assert type in _types.TYPES
        if setting.type != type:
            setting.type = type
            setting.value = None
            setting.save()
        keys.append(key)
    Setting.objects.exclude(key__in=keys).delete()


init_livesettings()
