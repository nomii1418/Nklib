# 🔑 Credentials Needed for Deployment

## ⚡ QUICK CHECKLIST

You need these 2 things (both FREE):

### 1️⃣ MongoDB Atlas Connection String
```
Where: https://mongodb.com/cloud/atlas
Time: 2 minutes
Cost: FREE
```

### 2️⃣ Telegram Bot Token
```
Where: @BotFather on Telegram
Time: 1 minute
Cost: FREE
```

---

## 📋 STEP-BY-STEP: Get MongoDB Atlas

1. **Sign Up**
   ```
   → Go to: https://mongodb.com/cloud/atlas/register
   → Click "Try Free"
   → Sign up with Google (fastest)
   ```

2. **Create Free Cluster**
   ```
   → Click "Build a Database"
   → Choose "M0 FREE" (forever free)
   → Provider: AWS
   → Region: Choose closest to you
   → Cluster Name: Leave default or "NkLib"
   → Click "Create"
   ```

3. **Create Database User**
   ```
   → Security > Database Access
   → Add New Database User
   → Username: admin
   → Password: (create strong password, SAVE IT!)
   → Database User Privileges: Read and write to any database
   → Add User
   ```

4. **Allow Network Access**
   ```
   → Security > Network Access
   → Add IP Address
   → Click "Allow Access from Anywhere"
   → IP Address: 0.0.0.0/0
   → Confirm
   ```

5. **Get Connection String**
   ```
   → Deployment > Database
   → Click "Connect" on your cluster
   → Choose "Connect your application"
   → Driver: Python, Version: 3.12 or later
   → Copy the connection string:
   
   mongodb+srv://admin:<password>@cluster0.xxxxx.mongodb.net/
   
   → Replace <password> with your actual password
   → Add database name at end: /mechanical_library
   
   Final URL should look like:
   mongodb+srv://admin:YourPassword123@cluster0.xxxxx.mongodb.net/mechanical_library
   ```

**SAVE THIS URL!** You'll need it for deployment.

---

## 🤖 STEP-BY-STEP: Get Telegram Bot Token

1. **Open Telegram**
   ```
   → Open Telegram app or web.telegram.org
   ```

2. **Find BotFather**
   ```
   → Search for: @BotFather
   → Start chat
   ```

3. **Create New Bot**
   ```
   → Send: /newbot
   → BotFather asks: "Alright, a new bot. How are we going to call it?"
   → Reply: Mechanical Library (or any name you want)
   
   → BotFather asks: "Now choose a username for your bot"
   → Reply: nklib_mechanical_bot (must end with _bot)
   ```

4. **Get Token**
   ```
   → BotFather gives you the token:
   "Use this token to access the HTTP API:
   7364728191:AAGvH5xKz8..."
   
   → Copy this entire token!
   ```

**SAVE THIS TOKEN!** You'll need it for deployment.

---

## ✅ CREDENTIALS CHECKLIST

Before deploying, make sure you have:

- [ ] MongoDB Connection String
  ```
  Example: mongodb+srv://admin:pass123@cluster0.xxxxx.mongodb.net/mechanical_library
  ```

- [ ] Telegram Bot Token
  ```
  Example: 7364728191:AAGvH5xKz8pQwE...
  ```

- [ ] Admin Password (choose secure one)
  ```
  Default: nom (CHANGE THIS!)
  New: YourSecurePassword123
  ```

---

## 🔒 SECURITY NOTES

**DO NOT share these publicly:**
- ❌ MongoDB connection string (contains password)
- ❌ Telegram bot token (anyone can control your bot)
- ❌ Admin password

**Keep them safe in:**
- ✅ Environment variables (on hosting platform)
- ✅ .env file (locally, NOT in git)
- ✅ Password manager

---

## 🚀 READY TO DEPLOY?

Once you have both credentials, you can deploy!

**Next step:** Choose deployment platform and follow guide.

---

## 💾 YOUR CREDENTIALS (Fill this in locally, don't commit!)

```env
# MongoDB Atlas
MONGODB_URL=mongodb+srv://admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/mechanical_library

# Telegram Bot
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Admin Password
ADMIN_PASSWORD=YOUR_SECURE_PASSWORD_HERE

# These are auto-generated or set by platform:
SECRET_KEY=will_be_generated
DATABASE_NAME=mechanical_library
ADMIN_USERNAME=nk28
FRONTEND_URL=will_be_set_after_frontend_deploy
BACKEND_URL=will_be_set_after_backend_deploy
```

---

## ❓ FAQ

**Q: Do I need a credit card?**
A: No! MongoDB Atlas and Telegram are completely free.

**Q: How long does this take?**
A: About 3 minutes total.

**Q: What if I forget my credentials?**
A: MongoDB: Reset in Atlas dashboard
   Telegram: Message @BotFather again

**Q: Can I change them later?**
A: Yes! Update them in your hosting platform's environment variables.

---

## 🎯 NEXT STEPS

1. ✅ Get MongoDB URL (above)
2. ✅ Get Telegram Token (above)
3. 🚀 Deploy using DEPLOY_NOW.md
4. 🎉 Your platform is LIVE!
