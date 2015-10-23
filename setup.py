#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_terminal import __version__


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
    name='djangocms-terminal',
    version=__version__,
    description='Terminal for Django CMS project.',
    author='Marco Federighi',
    author_email='federighi.marco@gmail.com',
    url='https://github.com/fmarco/djangocms-terminal',
    packages=['djangocms_terminal'],
    license='MIT',
    platforms=['OS Independent'],
    install_requires=[],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    keywords=['terminal', 'django', 'debug', 'djangocms'],
)