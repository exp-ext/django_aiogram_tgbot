"""Gunicorn *development* config file"""
import multiprocessing

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = 'backend.wsgi:application'
# The granularity of Error log outputs
loglevel = 'debug'
# The number of worker processes for handling requests
workers = (multiprocessing.cpu_count() * 2) + 1
# The socket to bind
bind = '0.0.0.0:8000'
# Restart workers when code changes (development only!)
reload = True
