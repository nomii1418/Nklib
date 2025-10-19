# 🚀 START HERE - Deploy to https://github.com/nomii1418/Nklib

## ⚡ QUICK ACTION PLAN (15 minutes total)

### ✅ PHASE 1: Get Credentials (3 minutes)

**You need 2 things - both FREE:**

#### 1. MongoDB Atlas (2 min)
```
→ Go to: https://mongodb.com/cloud/atlas/register
→ Sign up with Google (fastest)
→ Create FREE M0 cluster
→ Create user: admin / (your password)
→ Whitelist IP: 0.0.0.0/0
→ Get connection string:
  mongodb+srv://admin:PASSWORD@cluster0.xxxxx.mongodb.net/mechanical_library
```

#### 2. Telegram Bot Token (1 min)
```
→ Open Telegram
→ Search: @BotFather
→ Send: /newbot
→ Name: Mechanical Library
→ Username: nklib_mechanical_bot
→ Copy token: 7364728191:AAG...
```

**📖 Detailed guide:** `YOUR_CREDENTIALS.md`

---

### ✅ PHASE 2: Push to GitHub (2 minutes)

**Option A: Automated (Recommended)**
```bash
cd /workspace
./push-to-github.sh
```

**Option B: Manual**
```bash
cd /workspace
git init
git remote add origin https://github.com/nomii1418/Nklib.git
git add .
git commit -m "Add complete platform with deployment configs"
git push -u origin main
```

---

### ✅ PHASE 3: Deploy (10 minutes)

**Recommended: Render + Vercel (100% FREE)**

#### 3A. Deploy Backend to Render (5 min)

1. Go to: https://dashboard.render.com
2. New → Web Service
3. Connect repo: nomii1418/Nklib
4. Settings:
   - Name: `nklib-api`
   - Environment: Python 3
   - Build: `cd backend && pip install -r requirements.txt`
   - Start: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Environment Variables:
   ```
   MONGODB_URL = (your MongoDB URL from Phase 1)
   TELEGRAM_BOT_TOKEN = (your token from Phase 1)
   SECRET_KEY = (click Generate)
   DATABASE_NAME = mechanical_library
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = YourSecurePassword123
   ```
6. Create Service → Wait 5 min
7. Save URL: `https://nklib-api.onrender.com`

#### 3B. Deploy Bot Worker to Render (2 min)

1. Render Dashboard → New → Background Worker
2. Connect same repo
3. Settings:
   - Name: `nklib-bot`
   - Build: `pip install -r bot/requirements.txt`
   - Start: `python bot/telegram_bot.py`
4. Environment Variables:
   ```
   TELEGRAM_BOT_TOKEN = (same as before)
   BACKEND_URL = https://nklib-api.onrender.com
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = (same as backend)
   ```
5. Create Worker

#### 3C. Deploy Frontend to Vercel (2 min)

1. Go to: https://vercel.com
2. New Project → Import from GitHub
3. Select: nomii1418/Nklib
4. Settings:
   - Framework: Vite
   - Root Directory: `frontend`
5. Environment Variable:
   ```
   VITE_API_URL = https://nklib-api.onrender.com
   ```
6. Deploy → Wait 2 min
7. Save URL: `https://nklib.vercel.app`

#### 3D. Update Backend URLs (1 min)

1. Go back to Render → nklib-api → Environment
2. Add:
   ```
   FRONTEND_URL = https://nklib.vercel.app
   BACKEND_URL = https://nklib-api.onrender.com
   ```
3. Save (auto-redeploys)

---

### ✅ PHASE 4: Test & Go Live! (2 minutes)

#### Test Backend:
```
Visit: https://nklib-api.onrender.com/health
Should return: {"status":"healthy"}
```

#### Test Frontend:
```
Visit: https://nklib.vercel.app
Login: nk28 / YourSecurePassword123
```

#### Test Bot:
```
Telegram: @nklib_mechanical_bot
Send: /start
```

#### Test Sync:
```
1. Create subject on website
2. Check bot - should appear!
```

---

### ✅ PHASE 5: Keep It Awake (2 minutes)

**Setup UptimeRobot (prevents sleep):**

```
1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add Monitor:
   - Type: HTTP(s)
   - URL: https://nklib-api.onrender.com/health
   - Interval: 5 minutes
4. Save

Your app stays awake 24/7! ⏰
```

---

## 📊 SUMMARY

**What you'll have:**
- ✅ Professional website at `https://nklib.vercel.app`
- ✅ Backend API at `https://nklib-api.onrender.com`
- ✅ Telegram bot `@nklib_mechanical_bot`
- ✅ MongoDB database (512MB free)
- ✅ All features working!

**Cost:** $0/month forever ✅

**Time:** 15 minutes ✅

**Students helped:** Unlimited! 🎓

---

## 📚 HELPFUL GUIDES

**Credential Setup:**
- `CREDENTIALS_NEEDED.txt` - Quick reference
- `YOUR_CREDENTIALS.md` - Detailed step-by-step

**Deployment:**
- `DEPLOY_TO_YOUR_REPO.md` - Complete deployment guide
- `DEPLOY_NOW.md` - Alternative deployment
- `PLATFORMS.md` - Compare all platforms

**Reference:**
- `README.md` - Main documentation
- `FEATURES_CHECKLIST.md` - All features
- `DEPLOYMENT_INDEX.md` - All guides index

---

## 🆘 NEED HELP?

**Common Issues:**

**Can't push to GitHub?**
```bash
# Use force push if you own the repo
git push -u origin main --force
```

**MongoDB connection failed?**
```
→ Check password is correct
→ Verify IP whitelist: 0.0.0.0/0
→ Database name: mechanical_library
```

**Bot not responding?**
```
→ Check bot token with @BotFather
→ Verify bot worker is running on Render
→ Check Render logs for errors
```

---

## 🎯 YOUR NEXT STEPS

**Right now:**

1. ⏱️ **Get credentials** (3 min)
   - MongoDB Atlas URL
   - Telegram Bot Token

2. 📤 **Push to GitHub** (2 min)
   - Run: `./push-to-github.sh`

3. 🚀 **Deploy** (10 min)
   - Backend: Render
   - Frontend: Vercel
   - Bot: Render Worker

4. ✅ **Test** (2 min)
   - Website works
   - Bot responds
   - Admin login

5. 🎉 **Share** (∞ impact)
   - Give URL to students
   - Share bot link
   - Start helping!

---

## 🌟 YOU'RE READY!

**Everything is prepared and waiting for you!**

All you need:
- [ ] 3 minutes to get credentials
- [ ] 2 minutes to push to GitHub  
- [ ] 10 minutes to deploy
- [ ] 2 minutes to test

**Total: 17 minutes to change the world! 🚀**

---

**Start with Step 1: Get your credentials now!**

Visit: https://mongodb.com/cloud/atlas/register

**Good luck! Your students are waiting! 🎓**
