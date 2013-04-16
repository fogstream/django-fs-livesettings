# coding=utf-8

from django import forms

from livesettings import types as _types


class SettingAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingAdminForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget = _types.TYPE_WIDGET.get(self.instance.type)

    def clean_value(self):
        value = self.cleaned_data['value']
        return self.instance.clean_value(value)
