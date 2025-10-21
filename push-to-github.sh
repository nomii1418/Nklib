#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║        Push to GitHub: nomii1418/Nklib                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Set repository URL
REPO_URL="https://github.com/nomii1418/Nklib.git"

echo "📦 Preparing to push to: $REPO_URL"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "🔧 Initializing git..."
    git init
fi

# Configure git user (you may need to change these)
echo "👤 Configuring git user..."
git config user.name "nomii1418"
git config user.email "your-email@example.com"

# Add remote
echo "🔗 Setting up remote..."
git remote remove origin 2>/dev/null
git remote add origin $REPO_URL

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
if [ -z "$CURRENT_BRANCH" ]; then
    CURRENT_BRANCH="main"
    echo "📌 Creating main branch..."
    git checkout -b main
fi

echo "📍 Current branch: $CURRENT_BRANCH"
echo ""

# Add all files
echo "📁 Adding all files..."
git add .

# Show status
echo ""
echo "📊 Files to be committed:"
git status --short

echo ""
echo "💬 Creating commit..."
git commit -m "Deploy Mechanical Engineering Library Platform

✨ Features:
- FastAPI backend with MongoDB
- React frontend with Shadcn UI
- Telegram bot with admin controls
- Real-time file uploads with progress
- AI assistant integration
- Complete CRUD operations
- One-click deployment configs

🚀 Ready for deployment to:
- Render (backend + bot)
- Vercel (frontend)
- Railway (all-in-one)
- And more!

📚 Includes 12 comprehensive guides
💰 Total cost: \$0/month
"

echo ""
echo "🚀 Pushing to GitHub..."
echo ""

# Push to GitHub
if git push -u origin $CURRENT_BRANCH; then
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    ✅ SUCCESS!                                ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "🎉 Files pushed to: https://github.com/nomii1418/Nklib"
    echo ""
    echo "📋 NEXT STEPS:"
    echo ""
    echo "1. Get credentials (3 minutes):"
    echo "   📖 Read: YOUR_CREDENTIALS.md"
    echo ""
    echo "2. Deploy (10 minutes):"
    echo "   📖 Read: DEPLOY_TO_YOUR_REPO.md"
    echo ""
    echo "3. Go live! 🚀"
    echo ""
else
    echo ""
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    ⚠️  PUSH FAILED                           ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "This might be because:"
    echo "1. You need to authenticate with GitHub"
    echo "2. The branch already exists with different history"
    echo ""
    echo "To fix:"
    echo ""
    echo "Option 1: Force push (if you own the repo)"
    echo "  git push -u origin $CURRENT_BRANCH --force"
    echo ""
    echo "Option 2: Pull first then push"
    echo "  git pull origin $CURRENT_BRANCH --allow-unrelated-histories"
    echo "  git push -u origin $CURRENT_BRANCH"
    echo ""
    echo "Option 3: Use GitHub Personal Access Token"
    echo "  Visit: https://github.com/settings/tokens"
    echo "  Create token with 'repo' permissions"
    echo "  Then: git push https://YOUR_TOKEN@github.com/nomii1418/Nklib.git"
    echo ""
fi
