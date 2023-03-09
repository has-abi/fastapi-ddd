#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z ddd-db 5432; do
    sleep 1.0
done

echo "postgres started"

python3 ./src/server.py