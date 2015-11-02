# -*- coding: utf-8 -*-
import os

import django
from django.contrib.contenttypes.models import ContentType

from autofixture import AutoFixture


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
    app_label = get_module_name(app_label)
    return [model.__name__ for model in app_models(app_label)]

def get_app_model(app_label, model_name):
    app_label = get_module_name(app_label)
    return get_model(app_label=app_label, model_name=model_name)

def get_model_fields(app_label, model_name):
    app_label = get_module_name(app_label)
    model = get_app_model(app_label=app_label, model_name=model_name)
    model_fields = getattr(model._meta, 'get_fields()', model._meta.fields)
    return model_fields

def get_model_instance(app_label, model_name, args=None):
    app_label = get_module_name(app_label)
    init_values = {}
    if args:
        elements = args.split(',')
        for el in elements:
            key_value = el.split(':')
            key = key_value[0]
            value = key_value[1]
            init_values.update({key: value})
    try:
        model_class = get_app_model(app_label, model_name) #ContentType.objects.get(model=model_name).model_class()
        model_class(**init_values).save()
    except Exception as e:
        print e
        return "Error!"
    return "Created!"

def get_autofixture(app_label, model_name, f_key=False, n_instances=1):
    app_label = get_module_name(app_label)
    try:
        model_class = get_app_model(app_label, model_name) #ContentType.objects.get(model=model_name).model_class()
        fixtures = AutoFixture(model_class, generate_fk=f_key)
        entries = fixtures.create(n_instances)
    except Exception as e:
        print e
        return 'Error!'
    return 'Created(s)!'
