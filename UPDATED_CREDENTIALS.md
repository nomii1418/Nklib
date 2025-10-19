# 🔑 Updated Credentials Guide

## ✅ All Credentials You Need

### 1️⃣ MongoDB Atlas (FREE - 2 min)
```
URL: https://mongodb.com/cloud/atlas/register
Get: mongodb+srv://admin:PASSWORD@cluster.mongodb.net/mechanical_library
```

### 2️⃣ Telegram Bot Token (FREE - 1 min)
```
Open Telegram → @BotFather → /newbot
Get: 7364728191:AAGvH5xKz...
```

### 3️⃣ Cloudinary Credentials (FREE - 2 min) ⭐ NEW!
```
URL: https://cloudinary.com/users/register/free
Get 3 values:
  - Cloud Name: your-cloud-name
  - API Key: 123456789012345
  - API Secret: abcdefghijklmnopqrstuvwxyz
```

### 4️⃣ Admin Configuration
```
Website Login:
  Username: nk28
  Password: nom (CHANGE THIS!)

Bot Admin:
  Telegram ID: 6056498996 (YOUR ID)
  Access: Automatic (no login needed)
```

---

## 📋 Complete Environment Variables

### For Render Backend:

```env
# Required
MONGODB_URL=mongodb+srv://admin:PASSWORD@cluster.mongodb.net/mechanical_library
TELEGRAM_BOT_TOKEN=your_bot_token_here
SECRET_KEY=(click Generate in Render)
DATABASE_NAME=mechanical_library

# Admin
ADMIN_USERNAME=nk28
ADMIN_PASSWORD=your_secure_password
ADMIN_TELEGRAM_ID=6056498996

# Cloudinary (NEW!)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# URLs (add after deployment)
FRONTEND_URL=https://nklib.vercel.app
BACKEND_URL=https://nklib-api.onrender.com
```

### For Render Bot Worker:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
BACKEND_URL=https://nklib-api.onrender.com
ADMIN_USERNAME=nk28
ADMIN_PASSWORD=(same as backend)
ADMIN_TELEGRAM_ID=6056498996
```

### For Vercel Frontend:

```env
VITE_API_URL=https://nklib-api.onrender.com
```

---

## 🚀 Setup Order

**1. Get Cloudinary Credentials (2 min)** ⭐ NEW!
```
→ https://cloudinary.com/users/register/free
→ Sign up (no credit card)
→ Go to Dashboard
→ Copy: Cloud Name, API Key, API Secret
```
📖 **Detailed guide:** `CLOUDINARY_SETUP.md`

**2. Get MongoDB & Telegram (3 min)**
```
→ MongoDB Atlas (as before)
→ Telegram Bot Token (as before)
```
📖 **Detailed guide:** `YOUR_CREDENTIALS.md`

**3. Deploy with All Credentials (10 min)**
```
→ Add all variables to Render
→ Deploy backend + bot
→ Deploy frontend to Vercel
```
📖 **Detailed guide:** `RENDER_FIX.md`

---

## 🔐 Security Checklist

**✅ DO:**
- Store credentials in environment variables
- Use .env file locally (not committed to git)
- Change admin password from "nom"
- Keep Cloudinary API secret private

**❌ DON'T:**
- Commit credentials to git
- Share credentials publicly
- Use default password in production
- Share bot token

---

## 📊 What Changed

**NEW - Cloudinary Integration:**
```
✅ Files now stored on Cloudinary (not local disk)
✅ 25GB free storage
✅ 25GB free bandwidth
✅ CDN delivery worldwide
✅ Files persist forever (no ephemeral storage issues)
✅ Works perfectly with Render free tier!
```

**NEW - Admin Telegram ID:**
```
✅ Only YOUR Telegram ID (6056498996) can access admin panel
✅ Bot checks ID before showing admin controls
✅ Other users see "Unauthorized" message
✅ Secure bot administration
```

**Updated:**
```
✅ render.yaml - Added Cloudinary vars + Telegram ID
✅ render-simple.yaml - Added Cloudinary vars + Telegram ID
✅ Backend code - Integrated Cloudinary
✅ Bot code - Added Telegram ID check
```

---

## 🎯 Quick Reference

**Your Configuration:**
```
Admin Username: nk28
Admin Password: nom (CHANGE!)
Admin Telegram ID: 6056498996
Bot Admin: Only your Telegram account
File Storage: Cloudinary (25GB free)
Database: MongoDB Atlas (512MB free)
```

**What You Need:**
1. MongoDB URL ✅
2. Telegram Bot Token ✅
3. Cloudinary Cloud Name ✅
4. Cloudinary API Key ✅
5. Cloudinary API Secret ✅

---

## 📚 Detailed Guides

**Cloudinary Setup:**
→ `CLOUDINARY_SETUP.md` - Step-by-step Cloudinary

**Admin Configuration:**
→ `ADMIN_TELEGRAM_ID.md` - Your Telegram ID setup

**All Credentials:**
→ `YOUR_CREDENTIALS.md` - MongoDB + Telegram

**Deployment:**
→ `RENDER_FIX.md` - Complete deployment guide

---

## ✅ Checklist

Before deploying:
- [ ] MongoDB Atlas URL
- [ ] Telegram Bot Token
- [ ] Cloudinary Cloud Name
- [ ] Cloudinary API Key
- [ ] Cloudinary API Secret
- [ ] Changed admin password
- [ ] Your Telegram ID: 6056498996

After deploying:
- [ ] Backend URL saved
- [ ] Frontend URL saved
- [ ] All env vars set on Render
- [ ] Test file upload
- [ ] Test bot admin access
- [ ] Files upload to Cloudinary
- [ ] Everything works!

---

## 🎉 You're Ready!

**With Cloudinary:**
- ✅ Files persist forever
- ✅ 25GB free storage
- ✅ Fast CDN delivery
- ✅ No Render storage issues

**With Telegram ID Security:**
- ✅ Only you can access admin
- ✅ Bot is secure
- ✅ Others can browse content
- ✅ Full control for you

**Deploy now with confidence!** 🚀

---

*Setup time: 7 minutes*
*Monthly cost: $0*
*Storage: 25GB (Cloudinary) + 512MB (MongoDB)*
*Admin: Your Telegram only*
*All features: Working ✅*
