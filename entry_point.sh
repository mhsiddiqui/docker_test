#!/bin/sh
kill -KILL $(lsof -t -i tcp:5432)
python manage.py migrate
exec "$@"