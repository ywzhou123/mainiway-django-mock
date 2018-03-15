# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name=u'标题',help_text=u'标题')
    url = models.CharField(max_length=100, default='', unique=True, verbose_name=u'地址',help_text=u'地址')
    code = models.TextField(default='', verbose_name=u'编码',help_text=u'编码')
    sleep = models.IntegerField(default=0, verbose_name=u'延迟时间', help_text=u'延迟时间')
    # owner = models.ForeignKey('auth.User', related_name='snippets')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

# # 为每个用户添加token值
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

