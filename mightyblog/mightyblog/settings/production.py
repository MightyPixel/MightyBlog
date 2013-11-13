from base import *

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

ALLOWED_HOSTS = ['*']#['mightypixel.net']

DEBUG = False 
TEMPLATE_DEBUG = DEBUG


WSGI_APPLICATION = 'mightyblog.wsgi.application'

INTERNAL_IPS = ("127.0.0.1", )

import dj_database_url
DATABASES['default'] =  dj_database_url.config()
