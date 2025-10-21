#!/bin/bash

# Start script for Mechanical Engineering Library Platform

echo "Starting Mechanical Engineering Library Platform..."

# Check if MongoDB is running
if ! pgrep -x "mongod" > /dev/null; then
    echo "MongoDB is not running. Please start MongoDB first."
    echo "Run: sudo systemctl start mongodb"
    exit 1
fi

# Start backend
echo "Starting backend..."
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 5

# Start frontend
echo "Starting frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait a bit
sleep 3

# Start Telegram bot
echo "Starting Telegram bot..."
cd bot
python telegram_bot.py &
BOT_PID=$!
cd ..

echo ""
echo "================================================"
echo "✅ Platform started successfully!"
echo "================================================"
echo ""
echo "🌐 Website: http://localhost:3000"
echo "🔧 API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo "🤖 Telegram bot is running"
echo ""
echo "👨‍💼 Admin credentials:"
echo "   Username: nk28"
echo "   Password: nom"
echo ""
echo "To stop all services:"
echo "   kill $BACKEND_PID $FRONTEND_PID $BOT_PID"
echo ""

# Wait for all processes
wait
