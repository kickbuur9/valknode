# blog/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# This line tells Django which settings file to use
# For production, this should be set by the environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings.development") # Default for local dev

application = get_wsgi_application()