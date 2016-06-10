# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [

    url(
        regex=r'^$',
        view=views.ServiceAreaCreate.as_view(),
        name='servicearea_create'
    ),

    url(
        regex=r'(?P<lat>[0-9]+)/(?P<lon>[0-9]+)/^$',
        view=views.ServiceAreaCollection.as_view(),
        name='servicearea_collection'
    ),

]
