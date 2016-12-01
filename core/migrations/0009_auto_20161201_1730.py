# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-01 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_page_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='aside',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='block',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='footer',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='header',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='page',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='section',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='website',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Actif'),
        ),
    ]