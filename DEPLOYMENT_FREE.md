# 🚀 One-Click Free Deployment Guide

Deploy your Mechanical Engineering Library to free hosting platforms in minutes!

## 🎯 Recommended Setup

**Best Free Combination:**
1. **Backend**: Render (Free tier)
2. **Frontend**: Vercel or Netlify (Free tier)
3. **Database**: MongoDB Atlas (Free tier)
4. **Bot**: Render Background Worker (Free tier)

**Total Cost: $0/month** ✅

---

## 📋 Prerequisites (Get These First)

### 1. MongoDB Atlas (Free Database)
```
1. Go to https://www.mongodb.com/cloud/atlas/register
2. Create free account
3. Create free cluster (M0 Sandbox - FREE FOREVER)
4. Create database user
5. Whitelist all IPs (0.0.0.0/0)
6. Get connection string:
   mongodb+srv://username:password@cluster.mongodb.net/mechanical_library
```

### 2. Telegram Bot Token
```
1. Open Telegram
2. Search for @BotFather
3. Send /newbot
4. Follow instructions
5. Copy the token (looks like: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz)
```

---

## 🚀 One-Click Deployments

### Option 1: Render (Recommended - All-in-One)

**Deploy Everything to Render (Backend + Bot)**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

**Steps:**
1. Click the button above
2. Connect your GitHub account
3. Fork this repository
4. Fill in environment variables:
   - `MONGODB_URL`: Your MongoDB Atlas connection string
   - `TELEGRAM_BOT_TOKEN`: Your bot token from @BotFather
   - `ADMIN_PASSWORD`: Change from default 'nom' to secure password
5. Click "Create Web Service"
6. Wait 5-10 minutes for deployment
7. Note your backend URL: `https://your-app.onrender.com`

**Deploy Frontend Separately:**
- Go to [Vercel](#option-2-vercel-frontend) or [Netlify](#option-3-netlify-frontend)

---

### Option 2: Vercel (Frontend)

**Deploy Frontend to Vercel**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/mechanical-library&project-name=mechanical-library&repository-name=mechanical-library)

**Steps:**
1. Click the button above
2. Connect GitHub and import repository
3. Set root directory to: `frontend`
4. Add environment variable:
   - `VITE_API_URL`: Your Render backend URL
5. Click "Deploy"
6. Get your frontend URL: `https://your-app.vercel.app`

**Update Backend:**
```bash
# On Render, add this environment variable:
FRONTEND_URL=https://your-app.vercel.app
```

---

### Option 3: Netlify (Frontend Alternative)

**Deploy Frontend to Netlify**

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/yourusername/mechanical-library)

**Steps:**
1. Click the button above
2. Connect GitHub
3. Set build settings:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `frontend/dist`
4. Add environment variable:
   - `VITE_API_URL`: Your backend URL
5. Click "Deploy site"

---

### Option 4: Railway (Backend + Bot + Frontend)

**Deploy Everything to Railway**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

**Steps:**
1. Click the button above
2. Connect GitHub
3. Add MongoDB plugin (free tier)
4. Set environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your bot token
   - `SECRET_KEY`: Generate random string
   - `ADMIN_PASSWORD`: Your secure password
5. Deploy!

**Configuration:**
```bash
# Railway automatically sets PORT
# Your services will be available at:
# Backend: https://your-app.up.railway.app
# Frontend: https://your-frontend.up.railway.app
```

---

### Option 5: Fly.io (Backend + Bot)

**Deploy to Fly.io**

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Deploy backend
cd backend
fly launch --name mechanical-library-api
fly secrets set MONGODB_URL="your_mongodb_url"
fly secrets set TELEGRAM_BOT_TOKEN="your_token"
fly secrets set SECRET_KEY="random_secret"
fly deploy

# Deploy bot (as separate app)
cd ../bot
fly launch --name mechanical-library-bot
fly secrets set TELEGRAM_BOT_TOKEN="your_token"
fly secrets set BACKEND_URL="https://mechanical-library-api.fly.dev"
fly deploy
```

**Free Tier:**
- 3 shared-cpu-1x VMs with 256MB RAM each
- 160GB outbound data transfer
- Perfect for this project!

---

### Option 6: Heroku (If You Have Credits)

**Deploy to Heroku**

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

**Steps:**
1. Click the button above
2. Fill in environment variables
3. Add MongoDB Atlas connection string
4. Deploy!

**Note:** Heroku deprecated free tier, but you may have credits or use eco dynos ($5/month)

---

## 🔧 Manual Deployment Steps

### Step 1: Setup MongoDB Atlas (FREE)

```bash
1. Create account at https://mongodb.com/cloud/atlas
2. Create free M0 cluster
3. Create database user
4. Set network access to 0.0.0.0/0
5. Get connection string
```

### Step 2: Deploy Backend to Render

```bash
1. Go to https://render.com
2. Create account
3. New > Web Service
4. Connect your GitHub repo
5. Settings:
   - Name: mechanical-library-api
   - Environment: Python 3
   - Build Command: cd backend && pip install -r requirements.txt
   - Start Command: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   - Plan: Free
6. Environment Variables:
   - MONGODB_URL=mongodb+srv://...
   - TELEGRAM_BOT_TOKEN=your_token
   - SECRET_KEY=random_secret_key_here
   - DATABASE_NAME=mechanical_library
   - ADMIN_USERNAME=nk28
   - ADMIN_PASSWORD=your_secure_password
7. Create Web Service
8. Note URL: https://mechanical-library-api.onrender.com
```

### Step 3: Deploy Bot to Render

```bash
1. Render Dashboard > New > Background Worker
2. Connect same repo
3. Settings:
   - Name: mechanical-library-bot
   - Environment: Python 3
   - Build Command: pip install -r bot/requirements.txt
   - Start Command: python bot/telegram_bot.py
4. Environment Variables:
   - TELEGRAM_BOT_TOKEN=your_token
   - BACKEND_URL=https://mechanical-library-api.onrender.com
   - ADMIN_USERNAME=nk28
   - ADMIN_PASSWORD=same_as_backend
5. Create Background Worker
```

### Step 4: Deploy Frontend to Vercel

```bash
1. Go to https://vercel.com
2. Import Git Repository
3. Root Directory: frontend
4. Framework Preset: Vite
5. Environment Variables:
   - VITE_API_URL=https://mechanical-library-api.onrender.com
6. Deploy
7. Note URL: https://your-app.vercel.app
```

### Step 5: Update Backend URLs

```bash
# Add to Render backend environment variables:
FRONTEND_URL=https://your-app.vercel.app
BACKEND_URL=https://mechanical-library-api.onrender.com
```

---

## 🎉 You're Live!

Your platform is now deployed!

**URLs:**
- **Website**: https://your-app.vercel.app
- **API**: https://mechanical-library-api.onrender.com
- **API Docs**: https://mechanical-library-api.onrender.com/docs
- **Bot**: Search your bot on Telegram

**Login:**
- Username: nk28
- Password: (what you set)

---

## 📊 Free Tier Limits

### Render (Free)
- ✅ 750 hours/month
- ✅ Automatic deploys from Git
- ✅ Free SSL
- ⚠️ Sleeps after 15 min inactivity
- ⚠️ Takes ~30 sec to wake up

### Vercel/Netlify (Free)
- ✅ 100GB bandwidth/month
- ✅ Unlimited sites
- ✅ Automatic HTTPS
- ✅ CDN included
- ✅ Instant global deployment

### MongoDB Atlas (Free)
- ✅ 512MB storage
- ✅ Shared cluster
- ✅ No credit card required
- ✅ Perfect for learning projects

### Railway (Free Trial)
- ✅ $5 free credit/month
- ✅ All services in one place
- ⚠️ May require credit card verification

### Fly.io (Free)
- ✅ 3 VMs with 256MB RAM
- ✅ 160GB transfer/month
- ✅ Great performance
- ⚠️ Requires credit card (not charged)

---

## 🔄 Keep Your App Awake

**Problem:** Free tier apps sleep after inactivity

**Solutions:**

### 1. UptimeRobot (Free)
```
1. Sign up at https://uptimerobot.com
2. Add New Monitor
3. Monitor Type: HTTP(s)
4. URL: https://your-app.onrender.com/health
5. Interval: 5 minutes
6. Keeps your app awake 24/7!
```

### 2. Cron-job.org (Free)
```
1. Go to https://cron-job.org
2. Create free account
3. Create new cron job
4. URL: https://your-app.onrender.com/health
5. Interval: Every 5 minutes
```

---

## 🔐 Security Checklist

After deployment:

- [ ] Change admin password from 'nom' to secure password
- [ ] Keep bot token secret
- [ ] Keep MongoDB credentials secure
- [ ] Enable 2FA on hosting platforms
- [ ] Whitelist MongoDB IPs if needed
- [ ] Review CORS settings
- [ ] Check environment variables
- [ ] Setup backup strategy

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Render logs
1. Go to Render dashboard
2. Click your service
3. View logs
4. Common issues:
   - Missing environment variables
   - MongoDB connection failed
   - Invalid bot token
```

### Frontend can't connect to backend
```bash
# Check VITE_API_URL
1. Vercel dashboard > Settings > Environment Variables
2. Make sure VITE_API_URL points to your Render backend
3. Redeploy frontend after changing
```

### Bot not responding
```bash
# Check bot logs on Render
1. Background Worker > Logs
2. Verify TELEGRAM_BOT_TOKEN is correct
3. Make sure BACKEND_URL is set
4. Check bot is running (not crashed)
```

### MongoDB connection failed
```bash
# Check connection string
1. MongoDB Atlas dashboard
2. Database > Connect
3. Copy connection string
4. Replace <password> with actual password
5. Update MONGODB_URL in Render
```

---

## 📈 Upgrade Options

When your app grows:

**Render:**
- Starter: $7/month (no sleep)
- Standard: $25/month (better performance)

**Vercel:**
- Pro: $20/month (more bandwidth)

**MongoDB Atlas:**
- M10: $0.08/hour (dedicated cluster)

---

## 🎓 Post-Deployment

1. **Test Everything:**
   - Visit your website
   - Login as admin
   - Create a subject
   - Upload a file
   - Test the bot
   - Check file downloads

2. **Share Your Platform:**
   - Share website URL with students
   - Share Telegram bot link
   - Post on social media

3. **Monitor:**
   - Setup UptimeRobot
   - Check logs regularly
   - Monitor MongoDB usage

---

## 💡 Tips

1. **Use Environment Variables:** Never commit secrets to Git
2. **Regular Backups:** Export MongoDB data regularly
3. **Monitor Limits:** Keep eye on free tier limits
4. **Update Dependencies:** Keep packages updated
5. **SSL Certificates:** All platforms provide free HTTPS

---

## 🆘 Need Help?

**Platform Support:**
- Render: https://render.com/docs
- Vercel: https://vercel.com/docs
- Netlify: https://docs.netlify.com
- Railway: https://docs.railway.app
- MongoDB Atlas: https://docs.atlas.mongodb.com

**Common Issues:**
- Check platform status pages
- Review deployment logs
- Verify environment variables
- Test MongoDB connection
- Confirm bot token is valid

---

## ✅ Deployment Complete!

You now have a production-ready mechanical engineering platform running on free hosting! 🎉

**Cost: $0/month**
**Performance: Great for learning projects**
**Scalability: Easy to upgrade when needed**

**Start helping students learn today!** 🎓
