#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a Sphinx extension to make very nice.
'''

requires = ['Sphinx>=0.6', 'setuptools']


setup(name='numbered_blocks',
      version='6.9',
      description='Sphinx numbered blocks extension',
      author='todo',
      author_email='bleh@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requires,
      namespace_packages=['numbered_blocks'],
     )
