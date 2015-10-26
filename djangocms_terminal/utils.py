# -*- coding: utf-8 -*-
import os

import django


def installed_apps():
    return []

def module_import(arg):
    pass

if django.get_version() < '1.7':
    # Old versions
    from django.db.models import loading, get_app, get_apps, get_model, get_models
    from django.conf import settings
    from django.utils.module_loading import import_module

    def installed_apps():
        # TODO: Improve the method to retrieve installed apps names
        return settings.INSTALLED_APPS

    def app_models(app_label):
        return get_models(get_app(app_label))

    def module_import(app_label):
        return import_module(app_label).__name__

else:
    # Django 1.7, 1.8
    from django.apps import apps
    get_model = apps.get_model
    get_models = apps.get_models

    def installed_apps():
        return apps.get_app_configs()

    def app_models(app_label):
        return apps.get_app_config(app_label).get_models()


def get_module_name(complete_name):
    _, app_label = os.path.splitext(complete_name)
    app_label = app_label[1:] if app_label else _
    return app_label

def get_installed_apps():
    return [getattr(app, 'name', module_import(app)) for app in installed_apps()]

def get_app_models(app_label):
    return [model.__name__ for model in app_models(app_label)]

def get_app_model(app_label, model_name):
    return get_model(app_label=app_label, model_name=model_name)