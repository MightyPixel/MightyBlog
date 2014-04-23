from .base import *

import keychain

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

INTERNAL_IPS = ("127.0.0.1", )

WSGI_APPLICATION = 'mightyblog.wsgi_dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',# add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': keychain.name,                      # or path to database file if using sqlite3.
        # the following settings are not used with sqlite3:
        'USER': keychain.user,
        'PASSWORD': keychain.password,
        'HOST': '',                      # empty for localhost through domain sockets or '127.0.0.1' for localhost through tcp.
        'PORT': '',                      # set to empty string for default.
    }
}
