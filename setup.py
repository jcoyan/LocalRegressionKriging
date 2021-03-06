#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'numpy',
                'mpi4py',
                'scipy>=1.0.0',
                'rasterio>=0.36.0',
                'geopandas>=0.2.1',
                'scikit-learn>=0.19.1'
                ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Sudipta Basak",
    author_email='basaks@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A scalable local kriging implementation",
    entry_points={
        'console_scripts': [
            'localkriging=localkriging.cli:main',
        ],
    },
    extras_require={
        'dev': [
            'sphinx',
            'ghp-import',
            'sphinxcontrib-programoutput',
            'pytest-cov',
            'coverage == 4.4.1',
            'codecov == 2.0.9',
            'tox',
            'pytest >= 3.1.0',
            'pytest-lazy-fixture >= 0.4.0',
            'pytest-flake8 >= 0.8.1',
            'pytest-mock >= 1.6.0',
            'pytest-cov == 2.5.1',
            'pytest-regtest >= 0.15.1',
            'flake8-docstrings >= 1.1.0',
        ]
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='localkriging',
    name='localkriging',
    packages=find_packages(include=['localkriging']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/basaks/localkriging',
    version='0.1.0',
    zip_safe=False,
)
