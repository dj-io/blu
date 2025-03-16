#!/bin/bash

set -e  # Exit immediately if a command fails

echo "📌 Stopping existing Docker containers..."
docker-compose down

echo "🚀 Rebuilding and starting containers in detached mode..."
docker-compose up --build -d

echo "🛠 Running Alembic migration..."
docker-compose run app alembic -c resources/alembic.ini revision --autogenerate -m "V2_Migration"

echo "✅ Applying database migration..."
docker-compose run app alembic -c resources/alembic.ini upgrade head

echo "🎉 Setup complete! Sundays Services are now running."
