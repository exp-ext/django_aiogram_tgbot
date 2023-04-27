#!/bin/sh

until cd /app/

do
    echo "Waiting for server volume..."
done

until python3 manage.py migrate
do
    echo "Waiting for db to be ready... No migrate..."
    sleep 2
done

uvicorn backend.asgi:application --host 0.0.0.0 --port 8080  --workers 5
