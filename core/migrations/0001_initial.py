# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-19 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce_4.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aside',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='aside_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('css_class', models.CharField(blank=True, max_length=256, verbose_name='CSS classes')),
                ('css_id', models.CharField(blank=True, max_length=128, verbose_name='CDD unique id')),
                ('css_inline', models.CharField(blank=True, max_length=1200, verbose_name='CSS en ligne')),
                ('nom', models.CharField(max_length=512)),
                ('format', models.CharField(choices=[('FULL', 'Full width'), ('HALF', 'Half width'), ('THIRD', 'One third'), ('FOURTH', 'One fourth'), ('2FOURTH', 'Two fourth'), ('3FOURTH', 'Three fourth'), ('FIFTH', 'One fifth')], max_length=32, verbose_name='Format du bloc')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='block_author', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlockInSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Position of block in section')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Block')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='footer_author', to=settings.AUTH_USER_MODEL)),
                ('blocks', models.ManyToManyField(related_name='footer', to='core.Block')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='header_author', to=settings.AUTH_USER_MODEL)),
                ('blocks', models.ManyToManyField(related_name='header', to='core.Block')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('css_class', models.CharField(blank=True, max_length=256, verbose_name='CSS classes')),
                ('css_id', models.CharField(blank=True, max_length=128, verbose_name='CDD unique id')),
                ('css_inline', models.CharField(blank=True, max_length=1200, verbose_name='CSS en ligne')),
                ('titre', models.CharField(max_length=512)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='page_author', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('css_class', models.CharField(blank=True, max_length=256, verbose_name='CSS classes')),
                ('css_id', models.CharField(blank=True, max_length=128, verbose_name='CDD unique id')),
                ('css_inline', models.CharField(blank=True, max_length=1200, verbose_name='CSS en ligne')),
                ('nom', models.CharField(max_length=512, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='section_author', to=settings.AUTH_USER_MODEL)),
                ('pages', models.ManyToManyField(related_name='sections', to='core.Page')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=320)),
                ('slug', models.SlugField(unique=True)),
                ('contenu', tinymce_4.fields.TinyMCEModelField(verbose_name='Contenu')),
                ('pub_date', models.DateTimeField(verbose_name='date de publication')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1, verbose_name='Actif')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=512)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(1), related_name='website_author', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='page',
            name='websites',
            field=models.ManyToManyField(related_name='pages', to='core.Website'),
        ),
        migrations.AddField(
            model_name='header',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='header', to='core.Website'),
        ),
        migrations.AddField(
            model_name='footer',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer', to='core.Website'),
        ),
        migrations.AddField(
            model_name='blockinsection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Section'),
        ),
        migrations.AddField(
            model_name='aside',
            name='blocks',
            field=models.ManyToManyField(related_name='aside', to='core.Block'),
        ),
        migrations.AddField(
            model_name='aside',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aside',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aside', to='core.Website'),
        ),
    ]