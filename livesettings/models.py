# coding=utf-8

from django.db import models

from livesettings import types as _types


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
