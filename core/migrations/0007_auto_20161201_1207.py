# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-01 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161128_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='test',
            field=models.ManyToManyField(to='core.Snippet'),
        ),
        migrations.AlterField(
            model_name='block',
            name='css_class',
            field=models.CharField(blank=True, max_length=256, verbose_name='CSS classes'),
        ),
        migrations.AlterField(
            model_name='block',
            name='css_id',
            field=models.CharField(blank=True, max_length=128, verbose_name='CDD unique id'),
        ),
        migrations.AlterField(
            model_name='block',
            name='css_inline',
            field=models.CharField(blank=True, max_length=1200, verbose_name='CSS en ligne'),
        ),
        migrations.AlterField(
            model_name='page',
            name='css_class',
            field=models.CharField(blank=True, max_length=256, verbose_name='CSS classes'),
        ),
        migrations.AlterField(
            model_name='page',
            name='css_id',
            field=models.CharField(blank=True, max_length=128, verbose_name='CDD unique id'),
        ),
        migrations.AlterField(
            model_name='page',
            name='css_inline',
            field=models.CharField(blank=True, max_length=1200, verbose_name='CSS en ligne'),
        ),
        migrations.AlterField(
            model_name='section',
            name='css_class',
            field=models.CharField(blank=True, max_length=256, verbose_name='CSS classes'),
        ),
        migrations.AlterField(
            model_name='section',
            name='css_id',
            field=models.CharField(blank=True, max_length=128, verbose_name='CDD unique id'),
        ),
        migrations.AlterField(
            model_name='section',
            name='css_inline',
            field=models.CharField(blank=True, max_length=1200, verbose_name='CSS en ligne'),
        ),
    ]