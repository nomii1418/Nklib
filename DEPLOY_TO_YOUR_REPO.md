# 🚀 Deploy to Your Repository: https://github.com/nomii1418/Nklib

## ✅ WHAT I'VE PREPARED FOR YOU

All files are ready in `/workspace/`. You need to:
1. Push these files to your GitHub repo
2. Get credentials (MongoDB + Telegram)
3. Click deploy button

---

## 📤 STEP 1: Push Files to GitHub

### Option A: Using Git Commands (Recommended)

```bash
# Navigate to workspace
cd /workspace

# Initialize git if not already
git init

# Add remote (if not already added)
git remote add origin https://github.com/nomii1418/Nklib.git

# Or if already exists, update it
git remote set-url origin https://github.com/nomii1418/Nklib.git

# Add all files
git add .

# Commit
git commit -m "Add deployment configurations and complete platform

- Added backend API (FastAPI + MongoDB)
- Added frontend (React + TypeScript + Shadcn UI)
- Added Telegram bot with admin controls
- Added deployment configs for Render, Railway, Vercel, Netlify, Fly.io
- Added comprehensive documentation (12 guides)
- All features implemented: CRUD, file upload, AI assistant, real-time sync
- Ready for one-click deployment"

# Push to main branch
git push -u origin main

# Or if you're on a different branch
git push -u origin cursor/develop-mechanical-aspirant-platform-with-website-and-bot-6e81
```

### Option B: Using GitHub Web Interface

1. Go to https://github.com/nomii1418/Nklib
2. Click "Add file" > "Upload files"
3. Drag and drop all files from `/workspace/`
4. Commit changes

---

## 🔑 STEP 2: Get Your Credentials

You need 2 things (both FREE, takes 3 minutes):

### 1. MongoDB Atlas Connection String

```bash
# Go to: https://mongodb.com/cloud/atlas/register
1. Sign up (free)
2. Create M0 FREE cluster
3. Create database user (username: admin, password: choose one)
4. Whitelist IP: 0.0.0.0/0
5. Get connection string:
   mongodb+srv://admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/mechanical_library

SAVE THIS! ✍️
```

### 2. Telegram Bot Token

```bash
# Open Telegram
1. Search: @BotFather
2. Send: /newbot
3. Name: Mechanical Library
4. Username: nklib_mechanical_bot
5. Copy token: 7364728191:AAGvH5xKz...

SAVE THIS! ✍️
```

**Full guide:** See `YOUR_CREDENTIALS.md`

---

## 🚀 STEP 3: Deploy to Render + Vercel (RECOMMENDED)

### 3A. Deploy Backend to Render

1. **Go to Render**
   ```
   → https://dashboard.render.com
   → Sign in with GitHub
   ```

2. **Create Web Service**
   ```
   → New + > Web Service
   → Connect Repository: nomii1418/Nklib
   → Name: nklib-api
   → Environment: Python 3
   → Branch: main (or your branch)
   → Root Directory: (leave empty)
   → Build Command: cd backend && pip install -r requirements.txt
   → Start Command: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   → Plan: Free
   
   ⚠️ Note: Do NOT add region for free tier
   ⚠️ Note: Free tier has ephemeral storage (files are temporary)
   ```

3. **Add Environment Variables**
   ```
   Click "Advanced" > "Add Environment Variable"
   
   MONGODB_URL = mongodb+srv://admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/mechanical_library
   TELEGRAM_BOT_TOKEN = 7364728191:AAGvH5xKz...
   SECRET_KEY = (click "Generate" for random value)
   DATABASE_NAME = mechanical_library
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = YourSecurePassword123 (NOT "nom"!)
   ```

4. **Create Service**
   ```
   → Click "Create Web Service"
   → Wait 5-10 minutes
   → Note your URL: https://nklib-api.onrender.com
   
   SAVE THIS URL! ✍️
   ```

### 3B. Deploy Bot Worker to Render

1. **Create Background Worker**
   ```
   → Render Dashboard > New + > Background Worker
   → Connect Repository: nomii1418/Nklib
   → Name: nklib-bot
   → Environment: Python 3
   → Build Command: pip install -r bot/requirements.txt
   → Start Command: python bot/telegram_bot.py
   ```

2. **Add Environment Variables**
   ```
   TELEGRAM_BOT_TOKEN = 7364728191:AAGvH5xKz... (same as before)
   BACKEND_URL = https://nklib-api.onrender.com
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = YourSecurePassword123 (same as backend)
   ```

3. **Create Worker**
   ```
   → Click "Create Background Worker"
   → Wait 2 minutes
   → Bot is now running!
   ```

### 3C. Deploy Frontend to Vercel

1. **Go to Vercel**
   ```
   → https://vercel.com
   → Sign in with GitHub
   ```

2. **Import Repository**
   ```
   → New Project
   → Import Git Repository
   → Select: nomii1418/Nklib
   → Framework Preset: Vite
   → Root Directory: frontend
   ```

3. **Add Environment Variable**
   ```
   Name: VITE_API_URL
   Value: https://nklib-api.onrender.com
   ```

4. **Deploy**
   ```
   → Click "Deploy"
   → Wait 2 minutes
   → Note your URL: https://nklib.vercel.app
   
   SAVE THIS URL! ✍️
   ```

### 3D. Update Backend URLs

1. **Go back to Render**
   ```
   → Your nklib-api service
   → Environment
   → Add variables:
   
   FRONTEND_URL = https://nklib.vercel.app
   BACKEND_URL = https://nklib-api.onrender.com
   ```

2. **Save** (will auto-redeploy)

---

## ✅ STEP 4: Verify Deployment

### Test Backend
```
Visit: https://nklib-api.onrender.com/health
Should return: {"status":"healthy"}

Visit: https://nklib-api.onrender.com/docs
Should show: API documentation
```

### Test Frontend
```
Visit: https://nklib.vercel.app
Should show: Beautiful homepage

Try login:
Username: nk28
Password: YourSecurePassword123
```

### Test Bot
```
Open Telegram
Search: @nklib_mechanical_bot (or your bot username)
Send: /start
Should show: Main menu with buttons
```

### Test Sync
```
1. Login to website admin panel
2. Create a test subject
3. Open bot > Browse Subjects
4. Your subject should appear!
```

---

## 🔄 STEP 5: Keep It Awake (Optional but Recommended)

**Problem:** Render free tier sleeps after 15 min

**Solution:** Use UptimeRobot (FREE)

```bash
1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add New Monitor:
   - Monitor Type: HTTP(s)
   - Friendly Name: NkLib API
   - URL: https://nklib-api.onrender.com/health
   - Monitoring Interval: Every 5 minutes
4. Save

Your app stays awake 24/7! ⏰
```

---

## 🎉 YOU'RE LIVE!

### Your Platform URLs:

**Website:**
```
🌐 https://nklib.vercel.app
```

**API:**
```
🔧 https://nklib-api.onrender.com
📚 https://nklib-api.onrender.com/docs
```

**Telegram Bot:**
```
🤖 @nklib_mechanical_bot (or your username)
```

**Admin Login:**
```
👤 Username: nk28
🔑 Password: YourSecurePassword123
```

---

## 📊 Deployment Summary

**What's Running:**
- ✅ Backend API on Render
- ✅ Telegram Bot on Render
- ✅ Frontend on Vercel
- ✅ Database on MongoDB Atlas

**Cost:**
- 💰 Backend: $0/month
- 💰 Bot: $0/month
- 💰 Frontend: $0/month
- 💰 Database: $0/month
- 💰 **TOTAL: $0/month** ✅

**Performance:**
- ⚡ Website: Lightning fast (Vercel CDN)
- ⚡ API: Good (may take 30s to wake from sleep)
- ⚡ Bot: Always responsive
- ⚡ Database: Fast (MongoDB Atlas)

---

## 🔧 Update Your Deployment

**To update code:**
```bash
# Make changes locally
git add .
git commit -m "Your update message"
git push origin main

# Render & Vercel auto-deploy!
```

**To update environment variables:**
```
Render: Dashboard > Service > Environment
Vercel: Dashboard > Project > Settings > Environment Variables
```

---

## 🆘 Troubleshooting

### Backend Not Starting?
```
→ Check Render logs: Dashboard > nklib-api > Logs
→ Verify MONGODB_URL is correct
→ Check all environment variables are set
```

### Frontend Can't Connect?
```
→ Verify VITE_API_URL in Vercel
→ Should be: https://nklib-api.onrender.com
→ Redeploy after changing
```

### Bot Not Responding?
```
→ Check Render logs: Dashboard > nklib-bot > Logs
→ Verify TELEGRAM_BOT_TOKEN
→ Check bot worker is running
```

---

## 📞 Need Help?

**Repository:** https://github.com/nomii1418/Nklib

**Documentation:**
- Quick Deploy: `DEPLOY_NOW.md`
- Platform Comparison: `PLATFORMS.md`
- All Guides: `DEPLOYMENT_INDEX.md`

**Support:**
- Render: support@render.com
- Vercel: vercel.com/support
- MongoDB: support.mongodb.com

---

## 🎓 Next Steps

1. **Add Content**
   - Login as admin
   - Create subjects (Thermodynamics, Mechanics, etc.)
   - Upload study materials
   - Add videos and quizzes

2. **Customize**
   - Change admin password (not "nom"!)
   - Update bot name/description
   - Add custom domain (optional)

3. **Share**
   - Share website URL with students
   - Share bot link: t.me/nklib_mechanical_bot
   - Post on social media

4. **Monitor**
   - Setup UptimeRobot
   - Check MongoDB storage usage
   - Review Render logs occasionally

---

## 🌟 Congratulations!

**You've successfully deployed a professional mechanical engineering platform!**

**What you achieved:**
- ✅ Full-stack application live
- ✅ Professional website
- ✅ Telegram bot with admin controls
- ✅ Real-time file uploads
- ✅ AI assistant
- ✅ All on free hosting
- ✅ $0/month cost

**Time taken:** ~15 minutes
**Cost:** $0
**Impact:** Help thousands of students! 🎓

**Your platform is ready to change lives!** 🚀
