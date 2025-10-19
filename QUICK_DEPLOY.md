# ⚡ QUICK DEPLOY - You Have MongoDB!

## ✅ YOU HAVE (1/3)

**MongoDB URL:** ✅ Ready!
```
mongodb+srv://nk:nk1418$K@cluster0.ffrsd03.mongodb.net/mechanical_library?retryWrites=true&w=majority&appName=Cluster0
```

---

## ⏳ YOU NEED (2 more - 3 minutes)

### 1. Telegram Bot Token (1 minute)

```bash
Open Telegram → @BotFather → /newbot

Example result:
7364728191:AAGvH5xKz8pQwE_RtF2...
```

### 2. Cloudinary (2 minutes)

```bash
Sign up: https://cloudinary.com/users/register/free

Get 3 values from Dashboard:
- Cloud Name: xyz
- API Key: 123456789
- API Secret: abc...
```

---

## 🚀 DEPLOY (10 minutes)

### Step 1: Backend to Render (5 min)

1. **Go to:** https://dashboard.render.com
2. **New** → Web Service → Connect: **nomii1418/Nklib**
3. **Settings:**
   ```
   Name: nklib-api
   Build: cd backend && pip install -r requirements.txt
   Start: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Environment Variables (10):**
   ```
   MONGODB_URL
   mongodb+srv://nk:nk1418$K@cluster0.ffrsd03.mongodb.net/mechanical_library?retryWrites=true&w=majority&appName=Cluster0
   
   TELEGRAM_BOT_TOKEN
   (your bot token)
   
   SECRET_KEY
   (click Generate)
   
   DATABASE_NAME
   mechanical_library
   
   ADMIN_USERNAME
   nk28
   
   ADMIN_PASSWORD
   YourSecurePassword123
   
   ADMIN_TELEGRAM_ID
   6056498996
   
   CLOUDINARY_CLOUD_NAME
   (your cloud name)
   
   CLOUDINARY_API_KEY
   (your API key)
   
   CLOUDINARY_API_SECRET
   (your API secret)
   ```

5. **Deploy!** → Wait 5 minutes
6. **Save URL:** https://nklib-api.onrender.com

---

### Step 2: Bot to Render (2 min)

1. **New** → Background Worker
2. **Same repo**
3. **Settings:**
   ```
   Name: nklib-bot
   Build: pip install -r bot/requirements.txt
   Start: python bot/telegram_bot.py
   ```

4. **Environment Variables (5):**
   ```
   TELEGRAM_BOT_TOKEN = (same as backend)
   BACKEND_URL = https://nklib-api.onrender.com
   ADMIN_USERNAME = nk28
   ADMIN_PASSWORD = (same as backend)
   ADMIN_TELEGRAM_ID = 6056498996
   ```

5. **Deploy!**

---

### Step 3: Frontend to Vercel (2 min)

1. **Go to:** https://vercel.com
2. **Import:** nomii1418/Nklib
3. **Root Directory:** frontend
4. **Environment Variable:**
   ```
   VITE_API_URL = https://nklib-api.onrender.com
   ```
5. **Deploy!**
6. **Save URL:** https://nklib.vercel.app

---

### Step 4: Update URLs (1 min)

1. Render → nklib-api → Environment
2. Add:
   ```
   FRONTEND_URL = https://nklib.vercel.app
   BACKEND_URL = https://nklib-api.onrender.com
   ```
3. Save

---

## ✅ TEST

**Website:**
```
https://nklib.vercel.app
Login: nk28 / YourSecurePassword123
```

**API:**
```
https://nklib-api.onrender.com/health
Should return: {"status":"healthy"}
```

**Bot:**
```
@your_bot_username
/start
Click "Admin Panel" (only works for you!)
```

---

## 🎯 TIMELINE

- Get Bot Token: 1 min
- Get Cloudinary: 2 min
- Deploy Backend: 5 min
- Deploy Bot: 2 min
- Deploy Frontend: 2 min
- Update URLs: 1 min

**Total: 13 minutes** ⏱️

---

## 🎉 GO!

1. **Right now:** Get bot token (1 min)
2. **Then:** Get Cloudinary (2 min)
3. **Then:** Deploy! (10 min)
4. **Done:** Platform live! 🚀

**Start with @BotFather on Telegram!**

---

*MongoDB: ✅ Ready*
*Admin ID: ✅ Configured (6056498996)*
*Time remaining: 13 minutes*
*Cost: $0/month*
