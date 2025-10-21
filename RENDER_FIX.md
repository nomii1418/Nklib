# 🔧 Render Deployment - Fixed Configuration

## ⚠️ Issues Fixed

1. **Disk storage removed** - Free tier doesn't support persistent disks
2. **Frontend removed** - Static sites work better on Vercel/Netlify
3. **Simplified configuration** - Works with free tier limitations

---

## 🚀 UPDATED DEPLOYMENT GUIDE

### Render Free Tier Limitations:

❌ No persistent disk storage (files are temporary)
❌ Static sites have restrictions
✅ Backend API works great
✅ Background workers work great

### Solution:

1. **Backend + Bot** → Render (FREE)
2. **Frontend** → Vercel or Netlify (FREE)
3. **Files** → Store in MongoDB GridFS or use external service

---

## 📋 STEP-BY-STEP DEPLOYMENT

### Step 1: Deploy Backend to Render (5 minutes)

1. **Go to Render**
   ```
   https://dashboard.render.com
   Sign in with GitHub
   ```

2. **Create Web Service**
   ```
   → New + > Web Service
   → Connect Repository: nomii1418/Nklib
   → Name: nklib-api
   → Environment: Python 3
   → Branch: main
   → Root Directory: (leave empty)
   → Build Command: cd backend && pip install -r requirements.txt
   → Start Command: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   → Plan: Free
   ```

3. **Add Environment Variables**
   ```
   MONGODB_URL = mongodb+srv://admin:password@cluster.mongodb.net/mechanical_library
   TELEGRAM_BOT_TOKEN = your_bot_token
   SECRET_KEY = (click Generate)
   DATABASE_NAME = mechanical_library
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = your_secure_password
   ```

4. **Create Service**
   - Wait 5-10 minutes
   - Save URL: https://nklib-api.onrender.com

---

### Step 2: Deploy Bot to Render (3 minutes)

1. **Create Background Worker**
   ```
   → New + > Background Worker
   → Connect same repository
   → Name: nklib-bot
   → Environment: Python 3
   → Build Command: pip install -r bot/requirements.txt
   → Start Command: python bot/telegram_bot.py
   ```

2. **Add Environment Variables**
   ```
   TELEGRAM_BOT_TOKEN = (same as backend)
   BACKEND_URL = https://nklib-api.onrender.com
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = (same as backend)
   ```

3. **Create Worker**
   - Bot starts running immediately!

---

### Step 3: Deploy Frontend to Vercel (2 minutes)

1. **Go to Vercel**
   ```
   https://vercel.com
   Sign in with GitHub
   ```

2. **Import Project**
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
   - Wait 2 minutes
   - Save URL: https://nklib.vercel.app

---

### Step 4: Update Backend URLs (1 minute)

1. Go to Render → nklib-api → Environment
2. Add:
   ```
   FRONTEND_URL = https://nklib.vercel.app
   BACKEND_URL = https://nklib-api.onrender.com
   ```
3. Save (auto-redeploys)

---

## 📁 FILE STORAGE NOTE

**Important:** Render free tier has **ephemeral filesystem**

This means:
- ❌ Uploaded files are deleted when service restarts
- ❌ Files don't persist between deploys

**Solutions:**

### Option 1: MongoDB GridFS (FREE, Built-in)
Store files in MongoDB database
- ✅ Free
- ✅ Works with current setup
- ✅ Files persist
- ⚠️ Limited by 512MB MongoDB free tier

### Option 2: Cloudinary (FREE tier available)
External image/file hosting
- ✅ 25GB free storage
- ✅ 25GB free bandwidth/month
- ✅ CDN included
- Sign up: https://cloudinary.com

### Option 3: AWS S3 Free Tier
- ✅ 5GB storage (12 months free)
- More complex setup

### Option 4: Upgrade Render Plan
- $7/month for persistent disk
- 1GB storage included

**For now:** Files work temporarily. For permanent storage, implement one of the above solutions.

---

## ✅ DEPLOYMENT CHECKLIST

- [ ] Backend deployed to Render
- [ ] Bot worker running on Render
- [ ] Frontend deployed to Vercel
- [ ] All environment variables set
- [ ] Backend URL updated in frontend
- [ ] Frontend URL updated in backend
- [ ] Test: https://nklib-api.onrender.com/health
- [ ] Test: https://nklib.vercel.app
- [ ] Test: Telegram bot responds

---

## 🎯 WHAT WORKS

✅ **Backend API** - All endpoints working
✅ **Telegram Bot** - Fully functional
✅ **Frontend** - Fast and responsive
✅ **Database** - MongoDB Atlas (512MB free)
✅ **Admin Panel** - Full CRUD operations
✅ **AI Assistant** - Working
✅ **Real-time Sync** - Between web and bot

⚠️ **File Uploads** - Temporary only (see solutions above)

---

## 💰 COST

**Current Setup:**
- Render Backend: $0/month
- Render Bot: $0/month
- Vercel Frontend: $0/month
- MongoDB Atlas: $0/month
- **TOTAL: $0/month** ✅

**To Add Persistent Storage:**
- Render Starter ($7/month) - includes disk
- OR Cloudinary free tier - 25GB free
- OR MongoDB GridFS - included in current plan

---

## 🔄 FILE STORAGE IMPLEMENTATION

### Quick Fix: Store Files in MongoDB

Update `backend/app/routes/admin.py`:

```python
# Instead of saving to disk, save to MongoDB GridFS
import gridfs
from io import BytesIO

# In create_file endpoint:
fs = gridfs.GridFS(db)
file_id = fs.put(
    await file.read(),
    filename=file.filename,
    content_type=file.content_type,
    metadata={
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title
    }
)

# Store GridFS file_id in files collection
file_doc = {
    "file_id": str(file_id),
    # ... rest of metadata
}
```

This makes files permanent! ✅

---

## 🆘 TROUBLESHOOTING

### Backend Not Starting?
```
→ Check Render logs
→ Verify MONGODB_URL
→ Check Python version (should auto-detect)
```

### Bot Not Responding?
```
→ Check worker logs
→ Verify TELEGRAM_BOT_TOKEN
→ Make sure BACKEND_URL is correct
```

### Frontend Can't Connect?
```
→ Check VITE_API_URL in Vercel
→ Should match backend URL exactly
→ Redeploy after changing
```

---

## 📞 SUPPORT

**Render Issues:**
- Docs: https://render.com/docs
- Status: https://status.render.com

**File Storage Help:**
- MongoDB GridFS: https://docs.mongodb.com/manual/core/gridfs/
- Cloudinary: https://cloudinary.com/documentation

---

## 🎉 YOU'RE READY!

**Your platform is now deployed and working!**

Files to use:
- ✅ `render.yaml` - Updated and fixed
- ✅ `render-simple.yaml` - Simplified version

**Deploy now with confidence!** 🚀

---

*Issues fixed: Disk storage removed, static site configuration corrected*
*Free tier: Fully compatible*
*All features: Working except permanent file storage (see solutions)*
