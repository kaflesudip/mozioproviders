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
        regex=r'^(?P<lon>(-?\d+(?:\.\d+)?))/(?P<lat>(-?\d+(?:\.\d+)?))/$',
        view=views.ServiceAreaCollection.as_view(),
        name='servicearea_collection'
    ),

]
