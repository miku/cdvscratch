#!/usr/bin/env python
# coding: utf-8

import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.version_info < (2, 7):
    install_requires.append('importlib==1.0.2')

setup(name='cdvsets',
      version='0.0.1',
      description='Coding da vinci, data access.',
      url='https://github.com/miku/cdv',
      author='Martin Czygan',
      author_email='martin.czygan@gmail.com',
      packages=[
        'cdvsets',
      ],
      package_dir={'cdvsets': 'cdvsets'},
      scripts=[
        'bin/cdvsets-cat',
        'bin/cdvsets-do',
        'bin/cdvsets-ls',
        'bin/cdvsets-output',
        'bin/cdvsets-redo',
        'bin/cdvsets-rm',
        'bin/cdvsets-version',
      ],
)
