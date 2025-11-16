# Use an official Python runtime based on Debian 12 "bookworm" as a parent image.
FROM python:3.12-slim-bookworm

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=website.settings.production

# Install system packages required by Wagtail and Django
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Gunicorn application server
RUN pip install "gunicorn==20.0.4"

# Install the project requirements
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Set working directory
WORKDIR /app

# Set ownership for the wagtail user
RUN chown wagtail:wagtail /app

# Copy project files into container
COPY --chown=wagtail:wagtail . .

# Switch to the wagtail user
USER wagtail

# Runtime command: migrate DB and start Gunicorn
CMD set -xe; \
    python manage.py migrate --noinput; \
    python manage.py collectstatic --noinput; \
    gunicorn website.wsgi:application --bind 0.0.0.0:$PORT
