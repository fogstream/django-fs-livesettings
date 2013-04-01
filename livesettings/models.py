# coding=utf-8

from django.db import models
from django.forms import fields


class Setting(models.Model):
    TYPE_BOOLEAN = 'b'
    TYPE_CHAR = 'c'
    TYPE_DATE = 'd'
    TYPE_EMAIL = 'e'
    TYPE_INTEGER = 'i'
    TYPE_URL = 'u'
    TYPE_CHOICES = (
        (TYPE_BOOLEAN, 'boolean'),
        (TYPE_CHAR, 'char'),
        (TYPE_DATE, 'date'),
        (TYPE_EMAIL, 'email'),
        (TYPE_INTEGER, 'integer'),
        (TYPE_URL, 'url'),
    )

    TYPE_FIELD = {
        TYPE_BOOLEAN: fields.BooleanField(),
        TYPE_CHAR: fields.CharField(),
        TYPE_DATE: fields.DateField(),
        TYPE_EMAIL: fields.EmailField(),
        TYPE_INTEGER: fields.IntegerField(),
        TYPE_URL: fields.URLField(),
    }

    type = models.CharField(verbose_name=u'type', max_length=1, choices=TYPE_CHOICES)
    key = models.CharField(verbose_name=u'key', max_length=100, unique=True)
    value = models.CharField(verbose_name=u'value', max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = u'settings'
        verbose_name_plural = u'settings'

    def __unicode__(self):
        return self.key

    def __init__(self, *args, **kwargs):
        super(Setting, self).__init__(*args, **kwargs)
        self.field = self.TYPE_FIELD.get(self.type, models.CharField())

    @property
    def get_value(self):
        return self.field.to_python(self.value)
