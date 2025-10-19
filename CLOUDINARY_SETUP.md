# ☁️ Cloudinary Setup Guide

## 🎯 Why Cloudinary?

**Benefits:**
- ✅ 25GB storage FREE
- ✅ 25GB bandwidth/month FREE
- ✅ CDN included (fast delivery worldwide)
- ✅ No credit card required
- ✅ Files persist forever (no ephemeral storage)
- ✅ Perfect for Render free tier!

---

## 📋 Setup Steps (3 minutes)

### Step 1: Sign Up for Cloudinary (1 min)

1. **Go to Cloudinary**
   ```
   https://cloudinary.com/users/register/free
   ```

2. **Sign Up**
   - Use Google/GitHub (fastest)
   - Or email signup
   - No credit card needed!

3. **Verify Email**
   - Check your inbox
   - Click verification link

---

### Step 2: Get Your Credentials (1 min)

1. **Go to Dashboard**
   ```
   https://console.cloudinary.com/console
   ```

2. **Find Your Credentials**
   - Top right: Account Details
   - You'll see:
     ```
     Cloud Name: your-cloud-name
     API Key: 123456789012345
     API Secret: abcdefghijklmnopqrstuvwxyz
     ```

3. **Copy These 3 Values**
   ```
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=123456789012345
   CLOUDINARY_API_SECRET=abcdefghijklmnopqrstuvwxyz
   ```

---

### Step 3: Add to Your Deployment (1 min)

**For Render:**

1. Go to your backend service settings
2. Environment > Add Environment Variable
3. Add these 3 variables:
   ```
   CLOUDINARY_CLOUD_NAME = your-cloud-name
   CLOUDINARY_API_KEY = 123456789012345
   CLOUDINARY_API_SECRET = abcdefghijklmnopqrstuvwxyz
   ```

**For Railway:**

1. Variables tab
2. Add the same 3 variables

**For Local Development:**

Add to `backend/.env`:
```env
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcdefghijklmnopqrstuvwxyz
```

---

## ✅ How It Works

**File Upload Process:**

1. User uploads file (website or bot)
2. Backend receives file
3. File is uploaded to Cloudinary
4. Cloudinary returns public URL
5. URL is saved in MongoDB
6. User can download from Cloudinary URL

**Benefits:**
- ✅ Files stored on Cloudinary CDN
- ✅ Fast access from anywhere
- ✅ Persistent (never deleted)
- ✅ No local storage needed
- ✅ Works perfectly with Render free tier!

---

## 📊 Free Tier Limits

**Cloudinary Free Plan:**
- Storage: 25GB
- Bandwidth: 25GB/month
- Transformations: 25 credits/month
- Users: Unlimited
- Files: Unlimited

**For Education Platform:**
- ✅ Perfect for hundreds of students
- ✅ Can store PDFs, images, videos
- ✅ More than enough for most use cases

**When to upgrade?**
- Only if you exceed 25GB storage
- Only if you exceed 25GB bandwidth/month
- Most education platforms never need to!

---

## 🔧 Features

**What's Integrated:**

1. **File Upload** ✅
   - Direct upload to Cloudinary
   - Progress tracking works
   - Returns permanent URL

2. **File Download** ✅
   - Direct from Cloudinary CDN
   - Fast worldwide delivery
   - Works in website and bot

3. **File Delete** ✅
   - Removes from Cloudinary
   - Frees up storage
   - Removes from database

4. **File Update** ✅
   - Deletes old version
   - Uploads new version
   - Updates database

---

## 📁 File Organization

**Cloudinary Folder Structure:**
```
mechanical_library/
├── subject_id_1/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
├── subject_id_2/
│   ├── file1.pdf
│   └── ...
└── ...
```

**Automatic Organization:**
- Files grouped by subject
- Easy to browse in Cloudinary dashboard
- Can manage manually if needed

---

## 🎨 Bonus Features

**Cloudinary Can Also:**

1. **Image Optimization**
   - Auto-resize images
   - Convert formats (WebP, etc.)
   - Compress for faster loading

2. **Video Hosting**
   - Upload video tutorials
   - Adaptive streaming
   - Thumbnails auto-generated

3. **Transformations**
   - Resize on-the-fly
   - Add watermarks
   - Image effects

**All included in free plan!**

---

## 🔒 Security

**Your Credentials:**
- ⚠️ Keep API Secret private!
- ✅ Store in environment variables only
- ❌ Never commit to git
- ❌ Never share publicly

**Access Control:**
- Files are public by default (for easy sharing)
- Can make private if needed
- Admin uploads only (controlled by your app)

---

## 📊 Monitor Usage

**Check Your Usage:**

1. Go to: https://console.cloudinary.com
2. Dashboard > Usage
3. See:
   - Storage used
   - Bandwidth used
   - Transformations used

**Set Up Alerts:**
- Settings > Notifications
- Get email at 80% usage
- Upgrade or cleanup before limit

---

## 🆘 Troubleshooting

### Upload Fails?

**Check:**
```bash
# Verify credentials in environment
echo $CLOUDINARY_CLOUD_NAME
echo $CLOUDINARY_API_KEY
echo $CLOUDINARY_API_SECRET

# Test connection
curl https://api.cloudinary.com/v1_1/YOUR_CLOUD_NAME/image/list
```

### Files Not Showing?

**Verify:**
1. Cloudinary dashboard > Media Library
2. Your files should be there
3. Check folder: mechanical_library
4. Copy URL and test in browser

### Slow Uploads?

**Solutions:**
- Cloudinary has global CDN (should be fast)
- Check your internet connection
- Try smaller files first
- Check Cloudinary status: status.cloudinary.com

---

## 💡 Tips

1. **Organize Folders**
   - Use subject names in folders
   - Makes management easier
   - Can browse in Cloudinary UI

2. **File Naming**
   - Use descriptive names
   - Avoid special characters
   - Makes searching easier

3. **Backup**
   - Cloudinary is reliable
   - But keep original files backup
   - Just in case!

4. **Monitor Usage**
   - Check dashboard monthly
   - Delete unused files
   - Stay within free tier

---

## ✅ Setup Complete!

**You now have:**
- ✅ Cloudinary account
- ✅ API credentials
- ✅ Integration configured
- ✅ 25GB free storage
- ✅ Persistent file storage
- ✅ CDN delivery

**Files will now:**
- Upload to Cloudinary ☁️
- Store permanently (not deleted on restart)
- Deliver fast via CDN
- Work perfectly with Render free tier!

---

## 📚 Resources

**Cloudinary Docs:**
- Getting Started: https://cloudinary.com/documentation
- Python SDK: https://cloudinary.com/documentation/python_integration
- Free Tier: https://cloudinary.com/pricing

**Support:**
- Email: support@cloudinary.com
- Community: https://community.cloudinary.com
- Status: https://status.cloudinary.com

---

## 🎉 Ready!

**Next steps:**
1. ✅ You have Cloudinary credentials
2. ✅ Add to Render environment variables
3. ✅ Redeploy backend
4. ✅ Upload a test file
5. ✅ Files persist forever!

**Your file storage problem is solved!** ☁️🚀

---

*Setup time: 3 minutes*
*Cost: $0/month*
*Storage: 25GB*
*Bandwidth: 25GB/month*
*Perfect for education!* ✅
