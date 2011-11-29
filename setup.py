#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-rickroll',
    version='0.1',
    description='Rickrolling middleware to annoy potential hackers',
    long_description=open('README.rst').read(),
    author='David Winterbottom',
    author_email='david.winterbottom@gmail.com',
    license='BSD',
    packages=find_packages(exclude=('tests',)),
    tests_require=[
        'django>=1.3'
    ],
)