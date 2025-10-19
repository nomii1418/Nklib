# 🚀 Quick Deploy - Choose Your Platform

## ⚡ Fastest: One-Click Deploy

### 🟢 Option 1: Render (Recommended)
**Deploy backend + bot in one click!**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/nomii1418/Nklib)

**What you need:**
- MongoDB Atlas URL (free at mongodb.com/cloud/atlas)
- Telegram Bot Token (free from @BotFather)

**Steps:**
1. Click button above
2. Fill in 2 values: MongoDB URL & Bot Token
3. Wait 5 minutes
4. Done! Your API is live 🎉

---

### 🔷 Option 2: Railway
**Deploy everything including database!**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/mechanical-library)

**Steps:**
1. Click button
2. Connect GitHub
3. Add Bot Token
4. Deploy!

**Railway provides:**
- Free MongoDB instance
- Backend + Bot automatically configured
- $5 free credit/month

---

### ▲ Option 3: Vercel (Frontend Only)
**Deploy your website frontend!**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/nomii1418/Nklib&project-name=mechanical-library)

**Use with:** Render backend or Railway

---

### 🌐 Option 4: Netlify (Frontend Only)
**Alternative frontend deployment!**

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/nomii1418/Nklib)

---

## 🎯 Recommended Combinations

### Best Free Setup:
```
✅ Frontend: Vercel or Netlify (FREE)
✅ Backend: Render (FREE)
✅ Bot: Render Background Worker (FREE)
✅ Database: MongoDB Atlas (FREE)

Total: $0/month
```

### Easiest Setup:
```
✅ Everything: Railway (FREE trial, then $5/month)
   - Includes MongoDB
   - One platform for everything
   - Automatic configuration
```

---

## 📋 Pre-Deployment Checklist

### 1. Get MongoDB Atlas (2 minutes)
```
1. Go to: https://mongodb.com/cloud/atlas/register
2. Create free account
3. Create cluster (M0 FREE)
4. Create user & get connection string
   Example: mongodb+srv://user:pass@cluster.mongodb.net/mechanical_library
```

### 2. Get Telegram Bot Token (1 minute)
```
1. Open Telegram
2. Search: @BotFather
3. Send: /newbot
4. Follow steps
5. Copy token (looks like: 123456:ABCdef...)
```

### 3. Choose Platform (above)

---

## 🚀 Step-by-Step: Render + Vercel (Most Popular)

### A. Deploy Backend to Render (5 minutes)

```bash
1. Go to: https://render.com/deploy

2. Connect GitHub account

3. Fork this repository to your GitHub

4. Click "Deploy to Render" button above

5. Fill in environment variables:
   - MONGODB_URL: mongodb+srv://user:pass@cluster.mongodb.net/mechanical_library
   - TELEGRAM_BOT_TOKEN: your_bot_token_here
   - SECRET_KEY: (auto-generated)
   - ADMIN_PASSWORD: change_from_nom_to_secure_password

6. Click "Create Web Service"

7. Wait 5-10 minutes for deployment

8. Copy your backend URL:
   https://your-app.onrender.com
```

### B. Deploy Frontend to Vercel (2 minutes)

```bash
1. Click "Deploy with Vercel" button above

2. Import repository

3. Configure:
   - Root Directory: frontend
   - Framework: Vite
   
4. Add Environment Variable:
   - Name: VITE_API_URL
   - Value: https://your-app.onrender.com (from step A)

5. Click "Deploy"

6. Get your website URL:
   https://your-app.vercel.app
```

### C. Update Backend (1 minute)

```bash
1. Go back to Render dashboard

2. Your service > Environment

3. Add variable:
   - FRONTEND_URL: https://your-app.vercel.app

4. Save (will auto-redeploy)
```

### D. Start Bot Worker (3 minutes)

```bash
1. Render dashboard > New > Background Worker

2. Connect same repository

3. Settings:
   - Build: pip install -r bot/requirements.txt
   - Start: python bot/telegram_bot.py

4. Environment Variables:
   - TELEGRAM_BOT_TOKEN: same_as_backend
   - BACKEND_URL: https://your-app.onrender.com
   - ADMIN_USERNAME: nk28
   - ADMIN_PASSWORD: same_as_backend

5. Create Worker
```

---

## ✅ You're Live!

**Your platform is deployed! 🎉**

### Access Your Platform:

**Website:**
```
🌐 https://your-app.vercel.app
```

**API:**
```
🔧 https://your-app.onrender.com
📚 https://your-app.onrender.com/docs
```

**Telegram Bot:**
```
🤖 Search your bot on Telegram
```

**Admin Login:**
```
👤 Username: nk28
🔑 Password: (what you set)
```

---

## 🎨 Customize Your Deployment

### Change Admin Credentials:
```bash
Render Dashboard > Environment Variables:
- ADMIN_USERNAME: your_username
- ADMIN_PASSWORD: your_password
```

### Add Custom Domain (Free):
```bash
Vercel: Settings > Domains > Add
Render: Settings > Custom Domain
```

### Setup Auto-Deploy:
```bash
✅ Already configured!
Push to main branch = auto deploy
```

---

## 🔄 Keep App Awake (Prevent Sleep)

Free tier apps sleep after 15 minutes of inactivity.

### Quick Fix: UptimeRobot (Free)

```bash
1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Add New Monitor:
   - Type: HTTP(s)
   - URL: https://your-app.onrender.com/health
   - Interval: 5 minutes
4. Save

Now your app stays awake 24/7! ✅
```

---

## 📊 Your Free Resources

**Render (Free):**
- ✅ 750 hours/month
- ✅ Free SSL
- ✅ Auto deploys
- ⚠️ Sleeps after 15 min (fix with UptimeRobot)

**Vercel (Free):**
- ✅ 100GB bandwidth
- ✅ Unlimited sites
- ✅ Global CDN
- ✅ Instant deploys

**MongoDB Atlas (Free):**
- ✅ 512MB storage
- ✅ Good for thousands of documents
- ✅ No credit card needed

**Total Cost: $0** ✅

---

## 🐛 Troubleshooting

### Backend not working?
```bash
1. Check Render logs: Dashboard > Logs
2. Verify MongoDB URL is correct
3. Check all environment variables are set
4. Make sure bot token is valid
```

### Frontend can't connect?
```bash
1. Verify VITE_API_URL in Vercel settings
2. Should be: https://your-app.onrender.com
3. Redeploy frontend after changing
```

### Bot not responding?
```bash
1. Check Render Background Worker logs
2. Verify TELEGRAM_BOT_TOKEN
3. Make sure worker is running (not stopped)
4. Test bot token with @BotFather
```

### MongoDB connection error?
```bash
1. Atlas dashboard > Network Access
2. Add IP: 0.0.0.0/0 (allow all)
3. Database Access > Check user exists
4. Connection string format:
   mongodb+srv://user:pass@cluster.mongodb.net/dbname
```

---

## 🎓 What's Next?

1. **Test Your Deployment:**
   - Visit your website
   - Login as admin (nk28 / your_password)
   - Create a subject
   - Upload a file
   - Test Telegram bot

2. **Add Content:**
   - Create subjects for your curriculum
   - Upload study materials
   - Add video tutorials
   - Create quizzes

3. **Share:**
   - Share website URL with students
   - Share Telegram bot link
   - Post on social media

4. **Monitor:**
   - Setup UptimeRobot
   - Check Render logs occasionally
   - Monitor MongoDB storage

---

## 💰 When to Upgrade?

**Stay Free When:**
- < 100 active users
- < 512MB data
- Can handle 30s wake time

**Upgrade When:**
- Need instant response (no sleep)
- > 512MB data storage
- High traffic (>100 concurrent users)

**Upgrade Costs:**
- Render Starter: $7/month (no sleep)
- MongoDB M10: ~$10/month (more storage)
- Vercel Pro: $20/month (more bandwidth)

---

## 🌟 Success Stories

**Your platform will have:**
- ✅ Professional website
- ✅ Powerful Telegram bot
- ✅ Admin controls everywhere
- ✅ File uploads with progress
- ✅ AI assistant
- ✅ Full sync
- ✅ Free for students

**All running on free hosting!** 🎉

---

## 📞 Need Help?

**Quick Links:**
- [Full Deployment Guide](DEPLOYMENT_FREE.md)
- [Render Docs](https://render.com/docs)
- [Vercel Docs](https://vercel.com/docs)
- [MongoDB Atlas Docs](https://docs.atlas.mongodb.com)

**Common Issues:**
- Backend: Check Render logs
- Frontend: Check browser console
- Bot: Check Render worker logs
- Database: Check MongoDB Atlas network access

---

## 🎉 You're Ready to Deploy!

**Choose your platform above and click the deploy button!**

**Deployment time: 10-15 minutes**
**Cost: $0**
**Difficulty: Easy**

**Start helping students learn today!** 🎓

---

*Last Updated: October 2024*
*Platform: Render + Vercel + MongoDB Atlas*
*Status: ✅ Production Ready*
