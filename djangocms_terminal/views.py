# -*- coding: utf-8 -*-
import django
if django.get_version() < '1.8':
    from django.db.models import loading
else:
    from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render

from .utils import get_module_name, get_installed_apps, get_app_models

def installed_apps(request):
    res = [app + '<br>' for app in get_installed_apps()]
    return HttpResponse(res)

def get_models(request):
    app_label = get_module_name(request.GET.get('app_label', ''))
    res = [model + '<br>' for model in get_app_models(app_label)]
    return HttpResponse(res)

def model_fields(request):
    model_name = request.GET.get('model_name', '')
    for app in get_installed_apps():
        app = get_module_name(app)
        try:
            model = apps.get_model(app_label=app, model_name=model_name)
            res = [field.name + ' ('+ field.__class__.__name__ +')' + '<br>' for field in model._meta.get_fields()]
            return HttpResponse(res)
        except LookupError:
            pass
    return HttpResponse('Error')

def model_instance(request):
    model_name = request.GET.get('model_name', '').lower()
    init_values = {}
    args = request.GET.get('args', '')
    elements = args.split(';')
    for el in elements:
        key_value = el.split('=')
        key = key_value[0]
        value = key_value[1]
        init_values.update({key: value})
    try:
        model_class = ContentType.objects.get(model=model_name).model_class()
        model_class(**init_values).save()
    except Exception:
        return HttpResponse('Error!')
    return HttpResponse('Created')
