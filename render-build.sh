#!/bin/bash
# Render.com build script

set -e

echo "🔨 Building Mechanical Engineering Library..."

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

# Install bot dependencies
echo "🤖 Installing bot dependencies..."
pip install -r bot/requirements.txt

echo "✅ Build complete!"
