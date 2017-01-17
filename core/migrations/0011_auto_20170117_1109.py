# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-17 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170117_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockinsection',
            name='title_type',
        ),
        migrations.RemoveField(
            model_name='blockinsection',
            name='titre',
        ),
        migrations.AddField(
            model_name='section',
            name='title_type',
            field=models.CharField(choices=[('H2', 'h2'), ('H3', 'h3')], default='h2', max_length=16, verbose_name='Type de titre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='titre',
            field=models.CharField(default='titre', max_length=256),
            preserve_default=False,
        ),
    ]
