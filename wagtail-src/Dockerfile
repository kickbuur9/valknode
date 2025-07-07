FROM python:3.12-slim-bookworm

RUN useradd --create-home --shell /usr/sbin/nologin wagtail

ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE=blog.settings.production \
    STATIC_ROOT=/vol/web/static \
    MEDIA_ROOT=/vol/web/media \
    HOME=/home/wagtail

RUN apt-get update --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "gunicorn==23.0.0"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /vol/web/static /vol/web/media /app/blog/logs && \
    chown -R wagtail:wagtail /vol /app && \
    chmod -R u=rwX,g=rX,o=rX /vol/web && \
    chmod -R u=rwX,g=rX,o= /app/blog/logs  # logs not world-readable

COPY --chown=wagtail:wagtail . .

USER wagtail

RUN python manage.py collectstatic --noinput --clear --verbosity 2

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]
