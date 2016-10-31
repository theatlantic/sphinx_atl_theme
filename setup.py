# -*- coding: utf-8 -*-
"""`sphinx_atl_theme` lives on `Github`_.

.. _github: https://www.github.com/theatlantic/sphinx_atl_theme

"""
from setuptools import setup
from sphinx_atl_theme import __version__


setup(
    name='sphinx_atl_theme',
    version=__version__,
    url='https://github.com/theatlantic/sphinx_atl_theme/',
    license='MIT',
    author='Dave Snider',
    author_email='dave.snider@gmail.com',
    description='ReadTheDocs.org theme for Sphinx, 2013 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_atl_theme'],
    package_data={'sphinx_atl_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
