# coding=utf-8

from django.db import models


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
        if self.type == self.TYPE_BOOLEAN:
            self.field = models.BooleanField()
        elif self.type == self.TYPE_CHAR:
            self.field = models.CharField()
        elif self.type == self.TYPE_DATE:
            self.field = models.DateField()
        elif self.type == self.TYPE_EMAIL:
            self.field = models.EmailField()
        elif self.type == self.TYPE_INTEGER:
            self.field = models.IntegerField()
        elif self.type == self.TYPE_URL:
            self.field = models.URLField()
        else:
            self.field = models.CharField()

    @property
    def get_value(self):
        return self.field.to_python(self.value)
