from .base import *

DEBUG = True

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage

#STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.StaticFilesStorage"


ALLOWED_HOSTS = ["kickb.dev", "wagtail-service", "*"]

CSRF_TRUSTED_ORIGINS = [
    "https://kickb.dev",
]

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECRET_KEY = os.environ.get('SECRET_KEY')

if not SECRET_KEY:
    SECRET_KEY = "_6y5lq+@*-b7qd^t#1pw%i3_f4+2w(-&ex@53r7!21kab*&vau" # temporary fix!


try:
    from .local import *
except ImportError:
    pass
