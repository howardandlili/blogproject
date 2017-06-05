#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
]