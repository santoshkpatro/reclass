import os
from reclass.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PG_NAME', 'reclass_development'),
        'USER': os.environ.get('PG_USER', 'reclass'),
        'PASSWORD': os.environ.get('PG_PASSWORD', 'reclass'),
        'HOST': os.environ.get('PG_HOST', 'localhost'),
        'PORT': os.environ.get('PG_PORT', '5432'),
    }
}