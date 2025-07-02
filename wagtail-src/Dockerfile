FROM python:3.12-slim-bookworm

# Create user 'wagtail' with no shell or home dir
RUN useradd --no-create-home --shell /bin/false wagtail

EXPOSE 8000

# Create logging directory with ownership
RUN mkdir -p /app/blog/logs && chown -R wagtail:wagtail /app/blog/logs

# Build arguments
ARG DJANGO_SECRET_KEY_BUILD
ARG DJANGO_ALLOWED_HOSTS_BUILD

# Environment configuration
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=blog.settings.production \
    STATIC_ROOT=/vol/web/static \
    MEDIA_ROOT=/vol/web/media \
    SECRET_KEY=${DJANGO_SECRET_KEY_BUILD:-temp-secret-key-do-not-use} \
    ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS_BUILD:-192.168.178.155,192.168.178.35,localhost,127.0.0.1,*}

# Install system dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Gunicorn
RUN pip install "gunicorn==20.1.0"

# Set workdir and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create static/media folders with permissive permissions for testing
RUN mkdir -p /vol/web/static /vol/web/media && chmod -R 777 /vol/web

# Copy project files with correct ownership
COPY --chown=wagtail:wagtail . .

# Switch to Wagtail user
USER wagtail

# Collect static files
RUN python manage.py collectstatic --noinput --clear --verbosity 3

# Switch back to root to fix permissions on collected static/media (make fully open for testing)
USER root

RUN chmod -R 777 /vol/web

# Final switch to Wagtail user for running the app
USER wagtail


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]