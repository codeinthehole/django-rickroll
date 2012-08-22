#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-rickroll',
    version='0.1.1',
    description='Rickrolling Django middleware to annoy potential hackers',
    long_description=open('README.rst').read(),
    author='David Winterbottom',
    author_email='david.winterbottom@gmail.com',
    url='https://github.com/codeinthehole/django-rickroll',
    license=open('LICENSE').read(),
    packages=find_packages(exclude=('tests',)),
    tests_require=['django>=1.3'])
