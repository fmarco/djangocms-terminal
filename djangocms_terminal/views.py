# -*- coding: utf-8 -*-
import django
from django.http import HttpResponse
from django.shortcuts import render

from .utils import get_installed_apps, get_app_models, get_app_model, get_model_fields, get_model_instance, get_autofixture

def installed_apps(request):
    res = [app + '<br>' for app in get_installed_apps()]
    return HttpResponse(res)

def get_models(request):
    app_label = request.GET.get('app_label', '')
    res = [model + '<br>' for model in get_app_models(app_label)]
    return HttpResponse(res)

def model_fields(request):
    app_label = request.GET.get('app_label', '')
    model_name = request.GET.get('model_name', '')
    try:
        model_fields = get_model_fields(app_label, model_name)
        res = [field.name + ' ('+ field.__class__.__name__ +')' + '<br>' for field in model_fields]
        return HttpResponse(res)
    except Exception as e:
        print e
    return HttpResponse('Error')

def model_instance(request):
    app_label = request.GET.get('app_label', '')
    model_name = request.GET.get('model_name', '').lower()
    args = request.GET.get('args', '')
    msg = get_model_instance(app_label, model_name, args)
    return HttpResponse(msg)

def autofixture(request):
    app_label = request.GET.get('app_label', '')
    model_name = request.GET.get('model_name', '').lower()
    f_key = request.GET.get('f_key', '')
    f_key = f_key.split("=")[1]
    n_instances = int(request.GET.get('n_instances', ''))
    msg = get_autofixture(app_label, model_name, f_key, n_instances)
    return HttpResponse(msg)
