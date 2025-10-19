#!/bin/bash

echo "================================================"
echo "Mechanical Engineering Library - Setup Script"
echo "================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi
echo "✅ Python found: $(python3 --version)"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
fi
echo "✅ Node.js found: $(node --version)"

# Check MongoDB
if ! command -v mongod &> /dev/null; then
    echo "⚠️  MongoDB not found. Installing MongoDB..."
    # Ubuntu/Debian
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y mongodb
    # macOS
    elif command -v brew &> /dev/null; then
        brew tap mongodb/brew
        brew install mongodb-community
    else
        echo "❌ Please install MongoDB manually."
        exit 1
    fi
fi
echo "✅ MongoDB found"

# Start MongoDB if not running
if ! pgrep -x "mongod" > /dev/null; then
    echo "Starting MongoDB..."
    if command -v systemctl &> /dev/null; then
        sudo systemctl start mongodb || sudo systemctl start mongod
    elif command -v brew &> /dev/null; then
        brew services start mongodb-community
    else
        mongod --fork --logpath /var/log/mongodb.log
    fi
    sleep 3
fi
echo "✅ MongoDB is running"

# Setup backend
echo ""
echo "Setting up backend..."
cd backend
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate || . venv/Scripts/activate
pip install -r requirements.txt
cd ..
echo "✅ Backend setup complete"

# Setup frontend
echo ""
echo "Setting up frontend..."
cd frontend
npm install
cd ..
echo "✅ Frontend setup complete"

# Create uploads directory
mkdir -p uploads
echo "✅ Uploads directory created"

echo ""
echo "================================================"
echo "✅ Setup complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit backend/.env and add your Telegram bot token"
echo "2. Run: ./start.sh"
echo ""
echo "To get a Telegram bot token:"
echo "1. Open Telegram and search for @BotFather"
echo "2. Send /newbot and follow instructions"
echo "3. Copy the token and add it to backend/.env"
echo ""
