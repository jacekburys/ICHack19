#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of server.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018, Jacek Burys <jacekburys@gmail.com>

from setuptools import setup, find_packages
from server import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='server',
    version=__version__,
    description='an incredible python package',
    long_description='''
an incredible python package
''',
    keywords='',
    author='Jacek Burys',
    author_email='jacekburys@gmail.com',
    url='https://github.com/someuser/somepackage',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'Flask>=0.10.0,<0.11.0',
        'derpconf>=0.7.0,<0.8.0',
        'flask-debugtoolbar>=0.9.0,<0.10.0',
        'flask-assets>=0.10',
        'cssmin>=0.2.0,<0.3.0',
        'Flask-Script>=2.0.0,<2.1.0',



        'Flask-Admin>=1.2.0,<1.3.0',



    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'server=server.app:main',
            'server-manage=server.manage:main',

        ],
    },
)
