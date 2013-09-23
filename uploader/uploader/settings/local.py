# encoding: utf-8
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT('db', 'local.sqlite'),
    }
}

INSTALLED_APPS += (
    'upmedia',
)
