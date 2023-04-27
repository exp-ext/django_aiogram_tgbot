FROM python:3.11-slim-bullseye

WORKDIR /app

ARG DJANGO_SECRET_KEY

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

RUN --mount=type=cache,target=/var/cache/apt/archives/ \
    apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
        gcc \
        libpq-dev \
        python3-dev \
        postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip/ \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install psycopg2-binary --no-binary psycopg2-binary

COPY . .

RUN groupadd -r app-group && \
    useradd -r -g app-group app-user && \
    chown -R app-user:app-group /app

RUN python3 manage.py collectstatic --no-input

USER app-user
