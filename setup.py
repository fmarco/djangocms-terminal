#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from django_terminal import __version__


REQUIREMENTS = [
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='django-terminal',
    version=__version__,
    description='Terminal on your Django pages project.',
    author='Marco Federighi',
    author_email='federighi.marco@gmail.com',
    url='https://github.com/fmarco/django-terminal',
    packages=['django_terminal'],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=[],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)