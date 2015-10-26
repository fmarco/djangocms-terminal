# -*- coding: utf-8 -*-
import os

import django
if django.get_version() < '1.8':
    from django.db.models import loading, get_app, get_model
    from django.db.models import get_models
else:
    from django.apps import apps
    from django.apps.apps import get_model
    from django.apps.apps import get_models



def get_module_name(complete_name):
    _, app_label = os.path.splitext(complete_name)
    app_label = app_label[1:] if app_label else _
    return app_label

def get_installed_apps():
    if django.get_version() < '1.8':
        return [app.__name__ for app in loading.get_apps()]
    else:
        return [app.name for app in apps.get_app_configs()]

def get_app_models(app_label):
    if django.get_version() < '1.8':
        return get_models(get_app(app_label))
    else:
        return [model.__name__ for model in apps.get_app_config(app_label).get_models()]

def get_app_model(app_label, model_name):
    return get_model(app_label=app_label, model_name=model_name)