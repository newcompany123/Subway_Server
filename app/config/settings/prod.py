from .base import *


DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '.elasticbeanstalk.com',
    '.amazonaws.com',
    '.smallbee.kr',
    '.my-subway.com',
]
WSGI_APPLICATION = 'config.wsgi.prod.application'

INSTALLED_APPS += [
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'

import_secrets()
