# coding=utf-8

from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.forms import widgets

from . import models as _models


class SettingAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingAdminForm, self).__init__(*args, **kwargs)
        if self.instance.type == _models.Setting.TYPE_BOOLEAN:
            self.fields['value'].widget = widgets.CheckboxInput()
        elif self.instance.type == _models.Setting.TYPE_CHAR:
            self.fields['value'].widget = admin_widgets.AdminTextInputWidget()
        elif self.instance.type == _models.Setting.TYPE_DATE:
            self.fields['value'].widget = admin_widgets.AdminDateWidget()
        elif self.instance.type == _models.Setting.TYPE_EMAIL:
            self.fields['value'].widget = admin_widgets.AdminTextInputWidget()
        elif self.instance.type == _models.Setting.TYPE_INTEGER:
            self.fields['value'].widget = admin_widgets.AdminIntegerFieldWidget()
        elif self.instance.type == _models.Setting.TYPE_URL:
            self.fields['value'].widget = admin_widgets.AdminURLFieldWidget()

    def clean_value(self):
        value = self.cleaned_data['value']
        self.instance.field.clean(value, None)
        return value
