# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='zpp',
    version='0.1.0',
    description='Simple install for Zemax Post Processor',
    long_description=readme,
    author='Nick Konidaris',
    author_email='npk@carnegiescience.edu',
    url='https://github.com/nickkonidaris',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'sample'))
)

