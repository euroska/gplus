# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.static import serve

urlpatterns = [
    path(r'admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += [
        path(r'media/(?P<path>.*)', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
