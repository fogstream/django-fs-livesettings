# Generated by Django 4.2.16 on 2024-12-09 11:40

from django.db import migrations, models
import livesettings.fields
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('key', livesettings.fields.KeyField(max_length=255, primary_key=True, serialize=False, verbose_name='key')),
                ('tpe', models.CharField(blank=True, choices=[('boolean', 'boolean'), ('char', 'char'), ('date', 'date'), ('datetime', 'datetime'), ('decimal', 'decimal'), ('email', 'email'), ('file', 'file'), ('image', 'image'), ('integer', 'integer'), ('time', 'time'), ('url', 'url')], max_length=255, null=True, verbose_name='type')),
                ('value', picklefield.fields.PickledObjectField(blank=True, editable=False, null=True, verbose_name='value')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'settings',
            },
        ),
    ]
