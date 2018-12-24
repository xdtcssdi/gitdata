# -*- coding:utf-8 -*-
# Author:muming
# date:2018/12/24 13:58
from __future__ import unicode_literals

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render


def send_activate_mail(request, to, subject, template, **kwargs):
    html = render(request, template + '.html', {'token': kwargs['token'], 'username': kwargs['username']})
    text = render(request, template + '.txt', {'token': kwargs['token'], 'username': kwargs['username']})
    msg = EmailMultiAlternatives(subject, text.content.decode('utf-8'), 'mumin_g1208@163.com', [to])
    msg.attach_alternative(html.content.decode('utf-8'), "text/html")
    msg.send()
