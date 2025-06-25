FROM python:3.12-slim-bookworm

RUN useradd --no-create-home --shell /bin/false wagtail
EXPOSE 8000

# Build arguments
ARG DJANGO_SECRET_KEY_BUILD
ARG DJANGO_ALLOWED_HOSTS_BUILD

ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=blog.settings.production \
    STATIC_ROOT=/vol/web/static \
    MEDIA_ROOT=/vol/web/media \
    SECRET_KEY=${DJANGO_SECRET_KEY_BUILD:-temp-secret-key-do-not-use} \
    ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS_BUILD:-192.168.178.155,192.168.178.35,localhost,127.0.0.1}

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "gunicorn==20.1.0"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /vol/web/static /vol/web/media && \
    chown -R wagtail:wagtail /vol/web && \
    chmod -R 755 /vol/web

COPY --chown=wagtail:wagtail . .

USER wagtail

RUN python manage.py collectstatic --noinput --clear --verbosity 3

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]
