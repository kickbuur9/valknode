import os
from .base import *

DEBUG = False

STATIC_ROOT = '/vol/web/static'
STATIC_URL = '/static/'
MEDIA_ROOT = '/vol/web/media'
MEDIA_URL = '/media/'

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DEFAULT_ALLOWED = [
    "192.168.178.155",
    "192.168.178.35",
    "localhost",
    "127.0.0.1",
]
for host in DEFAULT_ALLOWED:
    if host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(host)

# Append Kubernetes-injected pod IP if provided
POD_IP = os.environ.get('POD_IP')
if POD_IP and POD_IP not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(POD_IP)

# Database config
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', ''), 
        conn_max_age=600,
    )
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    'https://kickb.dev',
    'http://192.168.178.155',
    'http://localhost',
    'http://127.0.0.1',
    'http://192.168.178.35',
    'http://192.168.178.155:31527'
]

WAGTAILADMIN_BASE_URL = os.environ.get('WAGTAILADMIN_BASE_URL', 'http://192.168.178.155')

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}
