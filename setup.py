# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='geoipdat',
    version='0.0.1',
    author=u'Arthur Rio',
    author_email='arthur@punchtab.com',
    packages=find_packages(),
    url='https://github.com/PunchTab/geo-ip',
    license='BSD licence, see LICENCE',
    description='.dat file for pygeoip',
    long_description=open('README.md').read(),
    zip_safe=False,
)

