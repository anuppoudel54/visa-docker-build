#!/bin/bash

echo "hello"

find . -path “*/migrations/*.py” -not -name “__init__.py” -delete
find . -path “*/migrations/*.pyc” -delete
echo "hello"
python3 manage.py makemigrations
python3 manage.py migrate
echo "hello"

s
expect this

python manage.py loaddata whole.json


exec "$@"
