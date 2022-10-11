#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/humai_decorator.svg
        :target: https://pypi.python.org/pypi/humai_decorator
.. image:: https://img.shields.io/travis/sniroo@github.com/humai_decorator.svg
        :target: https://travis-ci.org/sniroo@github.com/humai_decorator

Python Boilerplate contains all the boilerplate you need to create a Python package.


Links:
---------
* `Github <https://github.com/sniroo@github.com/humai_decorator>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', 'numpy>=1.23.3' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Leafnoise_Funcionales",
    author_email='fniro@leafnoise.io',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'humai_decorator=humai_decorator.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='humai_decorator',
    name='humai_decorator',
    packages=find_packages(include=['humai_decorator']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sniroo@github.com/humai_decorator',
    version='0.1.0',
    zip_safe=False,
)
