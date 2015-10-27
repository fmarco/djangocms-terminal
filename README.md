DjangoCMS-Terminal
===============
[![PyPI](https://img.shields.io/pypi/pyversions/djangocms-terminal.svg)](https://pypi.python.org/pypi/djangocms-terminal/)
[![PyPI](https://img.shields.io/pypi/l/djangocms-terminal.svg)](https://pypi.python.org/pypi/djangocms-terminal/)
[![Latest Version](https://img.shields.io/pypi/v/djangocms-terminal.svg)](https://pypi.python.org/pypi/djangocms-terminal/)
[![PyPI](https://img.shields.io/pypi/dm/djangocms-terminal.svg)](https://pypi.python.org/pypi/djangocms-terminal/)

This package provides a terminal application.

Supported Django versions:

* Django 1.8, 1.7
* Django < 1.7 (wip, highly supported)


Supported django CMS versions:

* django CMS 3.x


Features
--------

* Terminal app
* Terminal plugin

Quickstart
----------

Install django-terminal:

    pip install djangocms-terminal

Add ``djangocms_terminal`` to INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        'djangocms_terminal',
        ...
    ]

Add the following to your ``urls.py``:

    url(r'^terminal/', include('djangocms_terminal.urls')),

Usage
----------

List of supported commands:

* ``apps_list`` : get the list of the installed apps
* ``models_list some_app_label`` : get the list of the models given an app label
* ``model_fields some_app_label model_name``: get the list of the fields given a couple of app_label/model_name
* ``model_instance model_name key1=value1,key2=value2...`` : create an instance of a model given a model name and a set of CSV keys/values (format: key=value)
* ``autofixture model_name f_key=True 5`` : create n instance of a model given a model name, a boolean value for the f_key parameter and a integer as an instances number


Thank-yous
----------

This project is based on Terminal by SDA (https://github.com/SDA/terminal). Thanks!