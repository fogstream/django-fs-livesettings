Introduction
============

django-livesettings is the Django-related reusable app provides the ability to store settings in a database and change them from an admin interface.


Installation
============

1. Install ``fogstream-livesettings`` using ``pip`` or ``easy_install``::

    $ pip install django-livesettings

2. Add the ``'livesettings'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file::

    INSTALLED_APPS = (
        ...
        'livesettings',
        ...
    )

3. Add ``LIVESETTINGS_CONF`` to a ``settings.py`` file::

    LIVESETTINGS_CONF = (
        ('MY_SETTING', 'email', u'Description of this setting.'),
    )


Usage
=====

    from livesettings.conf import livesettings
    print livesettings.MY_SETTING
