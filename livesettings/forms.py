# coding=utf-8

from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.forms import widgets

from livesettings import models as _models


class SettingAdminForm(forms.ModelForm):
    TYPE_WIDGET = {
        _models.Setting.TYPE_BOOLEAN: widgets.CheckboxInput(),
        _models.Setting.TYPE_CHAR: admin_widgets.AdminTextInputWidget(),
        _models.Setting.TYPE_DATE: admin_widgets.AdminDateWidget(),
        _models.Setting.TYPE_EMAIL: admin_widgets.AdminTextInputWidget(),
        _models.Setting.TYPE_INTEGER: admin_widgets.AdminIntegerFieldWidget(),
        _models.Setting.TYPE_URL: admin_widgets.AdminURLFieldWidget(),
    }

    def __init__(self, *args, **kwargs):
        super(SettingAdminForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget = self.TYPE_WIDGET.get(self.instance.type, admin_widgets.AdminTextInputWidget())

    def clean_value(self):
        value = self.cleaned_data['value']
        self.instance.field.clean(value, None)
        return value
