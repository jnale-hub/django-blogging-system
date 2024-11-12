#!/bin/sh

# Wait for PostgreSQL to be available
while ! nc -z db 5432; do
  echo "Waiting for the PostgreSQL server to be available..."
  sleep 1
done

# Run migrations, seed, and start the server
python manage.py migrate
python manage.py seed
exec "$@"
