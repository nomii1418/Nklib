#!/bin/bash
# Render.com start script

set -e

echo "🚀 Starting Mechanical Engineering Library..."

# Create uploads directory
mkdir -p /workspace/uploads

# Start backend
cd backend
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
