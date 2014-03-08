from base import *

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

ALLOWED_HOSTS = ['*']#['mightypixel.net']

DEBUG = True
TEMPLATE_DEBUG = DEBUG


WSGI_APPLICATION = 'mightyblog.wsgi.application'

INTERNAL_IPS = ("mightypixel.net", )

#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
