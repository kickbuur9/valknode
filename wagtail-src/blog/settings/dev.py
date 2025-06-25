from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-cqt6taff=lewn8#+ke65yu=1$kyov18*1wqe66f9kq=kp$c#4*"

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = [
    "192.168.178.155",  # IP of the server where the pods (Wagtail) are running
    "192.168.178.35",   # Your personal machine (developer/admin access)
    "localhost",        # Access via localhost if you're port-forwarding or testing locally
    "127.0.0.1",        # Loopback access
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
