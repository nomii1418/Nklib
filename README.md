# Mechanical Engineering Library Platform

A comprehensive learning platform for mechanical engineering students with a professional website and powerful Telegram bot integration.

## Features

### Website
- 📚 Browse subjects and topics
- 🎥 Video tutorials
- 📁 Downloadable study materials
- 📝 Interactive quizzes
- 💡 Tips and tricks
- 🤖 AI-powered assistant
- 👨‍💼 Admin panel for content management

### Telegram Bot
- 📱 Browse all content via Telegram
- 📤 File upload with real-time progress
- 👨‍💼 Full admin controls through bot
- 🔗 Generate public download links
- 🔄 Real-time sync with website

### Admin Features
- ➕ Add/Edit/Delete subjects
- ➕ Add/Edit/Delete topics
- ➕ Add/Edit/Delete videos
- 📤 Upload files with progress tracking
- ➕ Add/Edit/Delete quizzes
- ➕ Add/Edit/Delete tips
- 🔄 Manage content from both website and bot

## Tech Stack

### Backend
- FastAPI
- MongoDB (Motor async driver)
- Python Telegram Bot
- JWT Authentication
- Async file handling

### Frontend
- React + TypeScript
- Vite
- Tailwind CSS
- Shadcn UI components
- Axios for API calls

### Bot
- python-telegram-bot 20.7
- Async/await architecture
- Real-time file upload
- Button-based admin interface

## Installation

### Prerequisites
- Python 3.9+
- Node.js 18+
- MongoDB
- Telegram Bot Token (from @BotFather)

### Backend Setup

1. Install dependencies:
\`\`\`bash
cd backend
pip install -r requirements.txt
\`\`\`

2. Configure environment variables in \`backend/.env\`:
\`\`\`env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=mechanical_library
SECRET_KEY=your-secret-key-change-in-production
TELEGRAM_BOT_TOKEN=your-telegram-bot-token-from-botfather
ADMIN_USERNAME=nk28
ADMIN_PASSWORD=nom
FRONTEND_URL=http://localhost:3000
BACKEND_URL=http://localhost:8000
\`\`\`

3. Start the backend:
\`\`\`bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
\`\`\`

### Frontend Setup

1. Install dependencies:
\`\`\`bash
cd frontend
npm install
\`\`\`

2. Start the frontend:
\`\`\`bash
npm run dev
\`\`\`

The website will be available at http://localhost:3000

### Telegram Bot Setup

1. Get your bot token from @BotFather on Telegram
2. Add the token to \`backend/.env\`
3. Start the bot:
\`\`\`bash
cd bot
python telegram_bot.py
\`\`\`

## Usage

### Admin Login
- Username: \`nk28\`
- Password: \`nom\`

### Website Features

1. **Browse Subjects**: View all available subjects
2. **View Content**: Click on a subject to see topics, videos, files, quizzes, and tips
3. **AI Assistant**: Ask questions about mechanical engineering
4. **Admin Panel**: Manage all content (admin only)

### Telegram Bot Commands

1. \`/start\` - Show main menu
2. Browse subjects and content
3. Admin login (automatic for authorized users)
4. Upload files with real-time progress
5. Edit and delete content

### File Upload (Bot)

1. Click "Admin Panel" button
2. Select "Upload File"
3. Choose subject and topic
4. Enter title and description
5. Send the file
6. See real-time upload progress (0% → 100%)
7. Get public download link

### File Upload (Website)

1. Login as admin
2. Go to Admin Panel
3. Select "Files" tab
4. Choose subject
5. Click "Add File"
6. Fill details and select file
7. Watch upload progress bar
8. File is immediately available for download

## Project Structure

\`\`\`
/workspace
├── backend/
│   ├── app/
│   │   ├── models.py          # Database models
│   │   ├── database.py        # MongoDB connection
│   │   ├── auth.py            # Authentication
│   │   ├── main.py            # FastAPI app
│   │   └── routes/
│   │       ├── admin.py       # Admin CRUD operations
│   │       ├── public.py      # Public content APIs
│   │       ├── auth.py        # Auth endpoints
│   │       └── ai.py          # AI assistant
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/        # UI components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API services
│   │   ├── context/           # React context
│   │   └── lib/               # Utilities
│   ├── package.json
│   └── vite.config.ts
├── bot/
│   └── telegram_bot.py        # Telegram bot
├── uploads/                   # File storage
└── README.md
\`\`\`

## API Endpoints

### Public Endpoints
- \`GET /api/subjects\` - Get all subjects
- \`GET /api/subjects/{id}\` - Get subject details
- \`GET /api/subjects/{id}/content\` - Get all content for subject
- \`GET /api/topics/{id}/content\` - Get all content for topic
- \`GET /api/videos\` - Get videos (with filters)
- \`GET /api/files\` - Get files (with filters)
- \`GET /api/quizzes\` - Get quizzes (with filters)
- \`GET /api/tips\` - Get tips (with filters)
- \`GET /api/files/download/{filename}\` - Download file
- \`POST /api/ai/chat\` - Chat with AI assistant

### Admin Endpoints (Requires Authentication)
- \`POST /api/admin/subjects\` - Create subject
- \`PUT /api/admin/subjects/{id}\` - Update subject
- \`DELETE /api/admin/subjects/{id}\` - Delete subject
- (Similar endpoints for topics, videos, files, quizzes, tips)

### Auth Endpoints
- \`POST /api/auth/login\` - Login
- \`POST /api/auth/register\` - Register

## Features in Detail

### Real-time File Upload
- Progress tracking (0-100%)
- Large file support
- Error handling
- Upload cancellation

### Sync Between Website and Bot
- Instant content updates
- Shared database
- Consistent file storage
- Public download URLs

### AI Assistant
- Natural language queries
- Context-aware responses
- Topic suggestions
- Engineering-focused

### Admin Controls
- Full CRUD operations
- File management
- Content organization
- User management

## Security
- JWT authentication
- Password hashing (bcrypt)
- Admin-only routes
- Secure file uploads
- CORS configuration

## Development

### Adding New Content Types
1. Add model in \`backend/app/models.py\`
2. Add routes in \`backend/app/routes/admin.py\` and \`public.py\`
3. Add API functions in \`frontend/src/services/api.ts\`
4. Create UI components
5. Add bot handlers in \`bot/telegram_bot.py\`

### Customizing AI Assistant
- Update \`backend/app/routes/ai.py\`
- Integrate with OpenAI, Hugging Face, or other AI APIs
- Customize responses and behavior

## Troubleshooting

### MongoDB Connection Issues
- Ensure MongoDB is running
- Check connection string in .env
- Verify database permissions

### Bot Not Responding
- Check bot token is correct
- Ensure bot process is running
- Verify network connectivity

### File Upload Fails
- Check upload directory permissions
- Verify file size limits
- Check backend logs

## License
MIT License

## Support
For issues and questions, please open an issue on GitHub.
