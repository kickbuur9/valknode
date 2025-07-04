FROM python:3.12-slim-bookworm

# Create non-root user and group with home directory
RUN useradd --create-home --shell /usr/sbin/nologin wagtail

# Environment configuration
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=blog.settings.production \
    STATIC_ROOT=/vol/web/static \
    MEDIA_ROOT=/vol/web/media \
    HOME=/home/wagtail

# Install system dependencies
RUN apt-get update --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Gunicorn
RUN pip install --no-cache-dir "gunicorn==23.0.0"

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create static/media directories with correct permissions
RUN mkdir -p /vol/web/static /vol/web/media /app/blog/logs && \
    chown -R wagtail:wagtail /vol /app && \
    chmod -R u=rwX,g=rX,o=rX /vol/web && \
    chmod -R u=rwX,g=rX,o= /app/blog/logs  # logs not world-readable

# Copy app source code
COPY --chown=wagtail:wagtail . .

# Switch to non-root user
USER wagtail

# Run collectstatic safely as non-root
RUN python manage.py collectstatic --noinput --clear --verbosity 2

# Expose app port
EXPOSE 8000

# Launch the app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]
