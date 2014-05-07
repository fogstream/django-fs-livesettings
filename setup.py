# coding=utf-8

from setuptools import setup


setup(
    name='django-livesettings',
    version = '0.1',
    packages = ['livesettings'],
    include_package_data = True,
    install_requires = ['django-picklefield'],
    author = 'Yuri Lya',
    author_email = 'yuri.lya@fogstream.ru',
    url = 'https://bitbucket.org/fogstream/django-livesettings',
    license = 'The MIT License (MIT)',
    description = 'The Django-related reusable app provides the ability to store settings in a database and change them from an admin interface.',
    long_description = open('README.txt').read(),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
