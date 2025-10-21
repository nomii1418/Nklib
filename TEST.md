# Testing Guide

## Pre-deployment Testing Checklist

### Backend Tests

1. **Start Backend:**
   \`\`\`bash
   cd backend
   python -m uvicorn app.main:app --reload --port 8000
   \`\`\`

2. **Test Endpoints:**
   \`\`\`bash
   # Health check
   curl http://localhost:8000/health
   
   # Get subjects (should be empty initially)
   curl http://localhost:8000/api/subjects
   
   # Login
   curl -X POST http://localhost:8000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username":"nk28","password":"nom"}'
   \`\`\`

3. **Test Admin Endpoints:**
   \`\`\`bash
   # Get token from login response above
   TOKEN="your_token_here"
   
   # Create subject
   curl -X POST http://localhost:8000/api/admin/subjects \
     -H "Authorization: Bearer $TOKEN" \
     -F "name=Thermodynamics" \
     -F "description=Study of heat and energy" \
     -F "icon=🔥" \
     -F "order=0"
   \`\`\`

### Frontend Tests

1. **Install Dependencies:**
   \`\`\`bash
   cd frontend
   npm install
   \`\`\`

2. **Start Frontend:**
   \`\`\`bash
   npm run dev
   \`\`\`

3. **Test Pages:**
   - Home: http://localhost:3000
   - Subjects: http://localhost:3000/subjects
   - Login: http://localhost:3000/login
   - Admin: http://localhost:3000/admin (after login)
   - AI Assistant: http://localhost:3000/ai-assistant

4. **Test Features:**
   - [ ] Navigation works
   - [ ] Login with nk28/nom
   - [ ] View admin panel
   - [ ] Add subject
   - [ ] Browse subjects
   - [ ] AI assistant responds

### Telegram Bot Tests

1. **Get Bot Token:**
   - Message @BotFather on Telegram
   - Create new bot
   - Copy token

2. **Configure:**
   \`\`\`bash
   # Edit backend/.env
   TELEGRAM_BOT_TOKEN=your_token_here
   \`\`\`

3. **Start Bot:**
   \`\`\`bash
   cd bot
   python telegram_bot.py
   \`\`\`

4. **Test Bot:**
   - [ ] Send /start command
   - [ ] Browse subjects
   - [ ] Access admin panel
   - [ ] Upload file
   - [ ] See upload progress
   - [ ] Get download link
   - [ ] Ask AI assistant

### File Upload Tests

1. **Website Upload:**
   - [ ] Login as admin
   - [ ] Go to Files tab
   - [ ] Click Add File
   - [ ] Select file
   - [ ] See progress bar (0-100%)
   - [ ] File appears in list
   - [ ] Download works

2. **Bot Upload:**
   - [ ] Open bot
   - [ ] Admin Panel → Upload File
   - [ ] Select subject
   - [ ] Select topic
   - [ ] Enter title
   - [ ] Enter description
   - [ ] Send file
   - [ ] See progress (0% → 25% → 50% → 75% → 100%)
   - [ ] Get success message
   - [ ] Get download link
   - [ ] Link works outside Telegram

### Sync Tests

1. **Website → Bot:**
   - [ ] Add subject on website
   - [ ] Check bot shows new subject
   - [ ] Add file on website
   - [ ] Check bot shows new file

2. **Bot → Website:**
   - [ ] Upload file via bot
   - [ ] Check website shows new file
   - [ ] Download from website works

### AI Assistant Tests

1. **Website:**
   - [ ] Ask: "What is thermodynamics?"
   - [ ] Get response
   - [ ] Ask follow-up question
   - [ ] Conversation continues

2. **Bot:**
   - [ ] Send message to bot
   - [ ] Get AI response
   - [ ] Continue conversation

### CRUD Operations Tests

**Subjects:**
- [ ] Create subject
- [ ] View subject
- [ ] Update subject
- [ ] Delete subject

**Topics:**
- [ ] Create topic
- [ ] View topic
- [ ] Update topic
- [ ] Delete topic

**Videos:**
- [ ] Create video
- [ ] View video
- [ ] Update video
- [ ] Delete video

**Files:**
- [ ] Upload file
- [ ] View file
- [ ] Update file
- [ ] Delete file
- [ ] Download file

**Quizzes:**
- [ ] Create quiz
- [ ] View quiz
- [ ] Update quiz
- [ ] Delete quiz

**Tips:**
- [ ] Create tip
- [ ] View tip
- [ ] Update tip
- [ ] Delete tip

## Performance Tests

### File Upload
- [ ] Small file (< 1MB) - should be instant
- [ ] Medium file (1-10MB) - should show progress
- [ ] Large file (10-100MB) - should show smooth progress

### Page Load
- [ ] Home page loads in < 2s
- [ ] Subjects page loads in < 2s
- [ ] Subject detail loads in < 3s
- [ ] Admin panel loads in < 2s

### Bot Response
- [ ] /start responds in < 2s
- [ ] Browse responds in < 2s
- [ ] File upload starts in < 2s

## Error Handling Tests

1. **Invalid Login:**
   - [ ] Wrong username
   - [ ] Wrong password
   - [ ] Empty fields

2. **Unauthorized Access:**
   - [ ] Access admin without login
   - [ ] Access admin as non-admin user

3. **File Upload Errors:**
   - [ ] Very large file
   - [ ] Invalid file type
   - [ ] Network error during upload

4. **Database Errors:**
   - [ ] MongoDB not running
   - [ ] Connection lost
   - [ ] Invalid data

## Security Tests

- [ ] JWT token required for admin endpoints
- [ ] Token expires after 30 days
- [ ] Passwords are hashed
- [ ] File paths are sanitized
- [ ] CORS is configured
- [ ] No sensitive data in responses

## Browser Compatibility

- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers

## Integration Tests

1. **Full User Flow:**
   - [ ] User opens website
   - [ ] Browses subjects
   - [ ] Views videos
   - [ ] Downloads files
   - [ ] Takes quiz
   - [ ] Asks AI assistant

2. **Full Admin Flow:**
   - [ ] Admin logs in
   - [ ] Creates subject
   - [ ] Adds topics
   - [ ] Uploads videos
   - [ ] Uploads files (with progress)
   - [ ] Creates quizzes
   - [ ] Adds tips
   - [ ] Views on website
   - [ ] Views on bot
   - [ ] Edits content
   - [ ] Deletes content

## Automated Test Commands

\`\`\`bash
# Test backend
cd backend
python -m pytest tests/

# Test frontend
cd frontend
npm test

# Lint backend
cd backend
flake8 app/

# Lint frontend
cd frontend
npm run lint

# Type check frontend
npm run type-check
\`\`\`

## Post-deployment Verification

- [ ] All services running
- [ ] Website accessible
- [ ] API responding
- [ ] Bot responding
- [ ] Files downloadable
- [ ] Database persisting data
- [ ] Logs are clean
- [ ] No memory leaks
- [ ] No performance issues

## Known Issues

Document any known issues here:
- None currently

## Test Results

Date: ___________
Tester: ___________
Environment: ___________

Summary:
- Total tests: ___
- Passed: ___
- Failed: ___
- Skipped: ___

Critical issues: ___________
