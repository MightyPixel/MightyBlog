from base import *

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

ALLOWED_HOSTS = ['mightypixel.net']

DEBUG = False
TEMPLATE_DEBUG = DEBUG


WSGI_APPLICATION = 'mightyblog.wsgi.application'

INTERNAL_IPS = ("mightypixel.net", )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',# add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': keychain.name,                      # or path to database file if using sqlite3.
        # the following settings are not used with sqlite3:
        'USER': keychain.user,
        'PASSWORD': keychain.password,
        'HOST': '',                      # empty for localhost through domain sockets or '127.0.0.1' for localhost through tcp.
        'PORT': '',                      # set to empty string for default.
    }
}

#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
