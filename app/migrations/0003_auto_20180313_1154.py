# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_snippet_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
        migrations.AddField(
            model_name='snippet',
            name='sleep',
            field=models.IntegerField(default=0, help_text='\u5ef6\u8fdf\u65f6\u95f4', verbose_name='\u5ef6\u8fdf\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='code',
            field=models.TextField(default='', help_text='\u7f16\u7801', max_length=1000, verbose_name='\u7f16\u7801'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(default='', help_text='\u6807\u9898', max_length=100, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='url',
            field=models.CharField(default='', help_text='\u5730\u5740', max_length=100, verbose_name='\u5730\u5740'),
        ),
    ]
