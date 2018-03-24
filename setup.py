# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='taskmanager',
    version='1.0',
    description='Task managaer test project',
    author='Martin Miksanik',
    author_email='miksanik@gmail.com',
    url='https://github.com/euroska/uplus',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
    ],
    scripts=[
        'bin/taskmanager'
    ],
)
