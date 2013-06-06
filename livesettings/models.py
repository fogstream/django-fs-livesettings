# coding=utf-8

import re

from django.db import models
from django.db import connection
from django.db.utils import DatabaseError

from picklefield import fields as picklefield_fields

from livesettings import types as _types
from livesettings import settings as _settings


class Setting(models.Model):
    TYPE_CHOICES = zip(_types.TYPES, _types.TYPES)

    key = models.CharField(verbose_name=u'key', max_length=50, unique=True)
    type = models.CharField(verbose_name=u'type', max_length=50, choices=TYPE_CHOICES)
    value = picklefield_fields.PickledObjectField(verbose_name=u'value', editable=True, blank=True, null=True)

    class Meta:
        verbose_name = u'setting'
        verbose_name_plural = u'settings'

    def __unicode__(self):
        return self.key


key_re = re.compile(r'^[a-zA-Z0-9_]+$')


def fill_in_settings():
    try:
        Setting.objects.count()
    except DatabaseError:
        connection._rollback()
        return
    keys = []
    for key, type in _settings.CONFIG.iteritems():
        if (not key_re.match(key)) or (type not in _types.TYPES):
            from django.core.exceptions import ImproperlyConfigured
            raise ImproperlyConfigured('LiveSettings is improperly configured.')
        setting, created = Setting.objects.get_or_create(key=key)
        if setting.type != type:
            setting.type = type
            setting.value = None
            setting.save()
        keys.append(key)
    Setting.objects.exclude(key__in=keys).delete()


fill_in_settings()
