# Quick Start Guide

## Installation Options

### Option 1: Local Setup (Recommended for Development)

1. **Run setup script:**
   \`\`\`bash
   ./setup.sh
   \`\`\`

2. **Configure Telegram Bot:**
   - Get token from @BotFather on Telegram
   - Edit `backend/.env` and add your token:
     \`\`\`
     TELEGRAM_BOT_TOKEN=your_token_here
     \`\`\`

3. **Start all services:**
   \`\`\`bash
   ./start.sh
   \`\`\`

4. **Access the platform:**
   - Website: http://localhost:3000
   - API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Option 2: Docker Setup (Recommended for Production)

1. **Configure environment:**
   \`\`\`bash
   export TELEGRAM_BOT_TOKEN=your_token_here
   \`\`\`

2. **Start with Docker Compose:**
   \`\`\`bash
   docker-compose up -d
   \`\`\`

3. **Access the platform:**
   - Website: http://localhost:3000
   - API: http://localhost:8000

## First Steps

### 1. Login as Admin
- Username: `nk28`
- Password: `nom`

### 2. Create Your First Subject
1. Go to Admin Panel
2. Click "Add Subject"
3. Fill in:
   - Name: e.g., "Thermodynamics"
   - Description: e.g., "Study of heat and energy"
   - Icon: e.g., "🔥"
4. Click Save

### 3. Add Topics
1. Select the subject
2. Click "Add Topic"
3. Fill in details
4. Click Save

### 4. Upload Content
You can upload via:
- **Website**: Admin Panel → Files → Add File
- **Telegram Bot**: /start → Admin Panel → Upload File

### 5. Setup Telegram Bot

1. **Get Bot Token:**
   - Open Telegram
   - Search for @BotFather
   - Send `/newbot`
   - Follow instructions
   - Copy the token

2. **Configure:**
   - Add token to `backend/.env`
   - Restart services

3. **Use Bot:**
   - Search your bot on Telegram
   - Send `/start`
   - Explore content or login as admin

## Common Tasks

### Add a Video
\`\`\`
1. Admin Panel → Videos → Add Video
2. Fill in:
   - Subject: Select from dropdown
   - Topic: (Optional)
   - Title: Video title
   - Description: Brief description
   - URL: YouTube/Video URL
3. Save
\`\`\`

### Upload a File (with Progress)
\`\`\`
Website:
1. Admin Panel → Files → Add File
2. Select subject and topic
3. Choose file
4. Watch upload progress (0-100%)
5. File is live!

Telegram Bot:
1. /start → Admin Panel → Upload File
2. Select subject and topic
3. Enter title and description
4. Send file
5. See real-time progress
6. Get public download link
\`\`\`

### Create a Quiz
\`\`\`
1. Admin Panel → Quizzes → Add Quiz
2. Fill in basic info
3. Add questions in JSON format:
   [
     {
       "question": "What is the first law of thermodynamics?",
       "options": ["Energy conservation", "Entropy", "Temperature", "Pressure"],
       "correct": 0
     }
   ]
4. Save
\`\`\`

### Add Tips
\`\`\`
1. Admin Panel → Tips → Add Tip
2. Select subject/topic
3. Write helpful tip
4. Save
\`\`\`

## Bot Commands

- `/start` - Show main menu
- Browse subjects and content
- Admin panel (automatic login for nk28)
- Upload files with progress tracking

## Features

### For Students
- ✅ Browse all subjects freely
- ✅ Watch video tutorials
- ✅ Download study materials
- ✅ Take quizzes
- ✅ Get expert tips
- ✅ Ask AI assistant
- ✅ Access via website or Telegram

### For Admins
- ✅ Full CRUD operations
- ✅ Upload files with progress
- ✅ Manage from website or bot
- ✅ Real-time sync
- ✅ Public download links
- ✅ Organized content structure

## Troubleshooting

### MongoDB won't start
\`\`\`bash
# Linux
sudo systemctl start mongodb

# macOS
brew services start mongodb-community

# Docker
docker-compose up mongodb
\`\`\`

### Bot not responding
1. Check token is correct in .env
2. Verify bot process is running
3. Check bot logs: `tail -f bot.log`

### File upload fails
1. Check uploads directory exists
2. Verify permissions: `chmod 777 uploads`
3. Check disk space

### Frontend won't start
\`\`\`bash
cd frontend
rm -rf node_modules
npm install
npm run dev
\`\`\`

## Support

For issues:
1. Check logs in respective directories
2. Verify all services are running
3. Check MongoDB connection
4. Review .env configuration

## Next Steps

1. Customize subjects for your needs
2. Upload your content
3. Share bot link with students
4. Customize AI assistant responses
5. Add more features!

Enjoy your Mechanical Engineering Library! 🎓
