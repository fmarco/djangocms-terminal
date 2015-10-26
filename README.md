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

Thank-yous
----------

This project is based on Terminal by SDA (https://github.com/SDA/terminal). Thanks!