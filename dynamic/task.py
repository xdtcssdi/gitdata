# -*- coding:utf-8 -*-
# Author:muming
# date:2018/12/24 09:52
from __future__ import unicode_literals
import os

import django

from gitdata import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gitdata.settings")
django.setup()

from django.core.mail import send_mail


def sends_mail(username, email):
    frommail = settings.DEFAULT_FROM_EMAIL
    subject = '验证您的邮箱'
    context = '尊敬的用户:' + username + '：\n您好，你已经注册成功了，现在需要您激活您的账户，请您访问该链接：http://localhost:8080'
    send_mail(subject, context, frommail, [email],
              fail_silently=False)


sends_mail("muming", "1213751318@qq.com")
