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

gunicorn -c config/wsgi/config.py
