# -*- coding: utf-8 -*-
import django
from django.conf.urls import url, patterns

from . import views
from django.views.generic import TemplateView


if django.get_version() < '1.8':
    urlpatterns = patterns('',
        url(r'^apps_list/$', views.installed_apps),
        url(r'^models_list/$', views.get_models),
        url(r'^model_fields/$', views.model_fields),
        url(r'^model_instance/$', views.model_instance),
        url(r'^autofixture/$', views.autofixture),
        url(r'^$', TemplateView.as_view(template_name='djangocms_terminal/terminal.html'))
    )
else:
    urlpatterns = [
        url(r'^apps_list/$', views.installed_apps),
        url(r'^models_list/$', views.get_models),
        url(r'^model_fields/$', views.model_fields),
        url(r'^model_instance/$', views.model_instance),
        url(r'^autofixture/$', views.autofixture),
        url(r'^$', TemplateView.as_view(template_name='djangocms_terminal/terminal.html'))
    ]