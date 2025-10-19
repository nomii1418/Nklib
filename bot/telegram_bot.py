import asyncio
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes
)
import httpx
from dotenv import load_dotenv
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "nk28")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "nom")

# Conversation states
(ADMIN_LOGIN, ADMIN_MENU, ADD_SUBJECT, ADD_TOPIC, ADD_VIDEO, 
 ADD_FILE, ADD_QUIZ, ADD_TIP, EDIT_MENU, DELETE_MENU,
 UPLOAD_FILE_SUBJECT, UPLOAD_FILE_TOPIC, UPLOAD_FILE_TITLE,
 UPLOAD_FILE_DESC, UPLOAD_FILE_WAIT) = range(15)

# Store admin token and user sessions
admin_tokens = {}
user_sessions = {}

async def get_admin_token(telegram_id: str) -> str:
    """Get or create admin token for telegram user"""
    if telegram_id in admin_tokens:
        return admin_tokens[telegram_id]
    
    # Login to get token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/api/auth/login",
            json={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
        )
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            admin_tokens[telegram_id] = token
            return token
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command - show main menu"""
    keyboard = [
        [InlineKeyboardButton("📚 Browse Subjects", callback_data="browse_subjects")],
        [InlineKeyboardButton("🔍 Search Content", callback_data="search")],
        [InlineKeyboardButton("🤖 AI Assistant", callback_data="ai_assist")],
        [InlineKeyboardButton("👨‍💼 Admin Panel", callback_data="admin_login")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎓 Welcome to Mechanical Engineering Library!\n\n"
        "Access free learning resources including:\n"
        "• Video tutorials\n"
        "• Study materials\n"
        "• Practice quizzes\n"
        "• Tips & tricks\n\n"
        "Choose an option below:",
        reply_markup=reply_markup
    )

async def admin_login_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start admin login process"""
    query = update.callback_query
    await query.answer()
    
    telegram_id = str(query.from_user.id)
    
    # Auto-login for admin
    token = await get_admin_token(telegram_id)
    if token:
        await show_admin_menu(query, context)
    else:
        await query.edit_message_text("❌ Admin login failed. Please try again.")

async def show_admin_menu(query, context: ContextTypes.DEFAULT_TYPE):
    """Show admin control panel"""
    keyboard = [
        [InlineKeyboardButton("➕ Add Subject", callback_data="admin_add_subject")],
        [InlineKeyboardButton("➕ Add Topic", callback_data="admin_add_topic")],
        [InlineKeyboardButton("➕ Add Video", callback_data="admin_add_video")],
        [InlineKeyboardButton("📁 Upload File", callback_data="admin_upload_file")],
        [InlineKeyboardButton("➕ Add Quiz", callback_data="admin_add_quiz")],
        [InlineKeyboardButton("➕ Add Tip", callback_data="admin_add_tip")],
        [InlineKeyboardButton("✏️ Edit Content", callback_data="admin_edit")],
        [InlineKeyboardButton("🗑️ Delete Content", callback_data="admin_delete")],
        [InlineKeyboardButton("🔙 Back to Main", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "👨‍💼 Admin Control Panel\n\n"
        "Manage all platform content:",
        reply_markup=reply_markup
    )

async def browse_subjects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show all subjects"""
    query = update.callback_query
    await query.answer()
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/subjects")
        if response.status_code == 200:
            subjects = response.json()
            
            if not subjects:
                await query.edit_message_text(
                    "📚 No subjects available yet.\n\n"
                    "Admin can add subjects using the admin panel.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔙 Back", callback_data="back_to_main")
                    ]])
                )
                return
            
            keyboard = []
            for subject in subjects:
                keyboard.append([
                    InlineKeyboardButton(
                        f"📖 {subject['name']}", 
                        callback_data=f"subject_{subject['_id']}"
                    )
                ])
            keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="back_to_main")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                "📚 Select a Subject:\n\n"
                "Click on any subject to view its content.",
                reply_markup=reply_markup
            )

async def show_subject(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show subject details and content options"""
    query = update.callback_query
    await query.answer()
    
    subject_id = query.data.split("_")[1]
    
    async with httpx.AsyncClient() as client:
        # Get subject details
        response = await client.get(f"{BACKEND_URL}/api/subjects/{subject_id}")
        if response.status_code == 200:
            subject = response.json()
            
            # Get content counts
            content_response = await client.get(f"{BACKEND_URL}/api/subjects/{subject_id}/content")
            content = content_response.json()
            
            keyboard = [
                [InlineKeyboardButton(
                    f"📑 Topics ({len(content['topics'])})", 
                    callback_data=f"topics_{subject_id}"
                )],
                [InlineKeyboardButton(
                    f"🎥 Videos ({len(content['videos'])})", 
                    callback_data=f"videos_{subject_id}"
                )],
                [InlineKeyboardButton(
                    f"📁 Files ({len(content['files'])})", 
                    callback_data=f"files_{subject_id}"
                )],
                [InlineKeyboardButton(
                    f"📝 Quizzes ({len(content['quizzes'])})", 
                    callback_data=f"quizzes_{subject_id}"
                )],
                [InlineKeyboardButton(
                    f"💡 Tips ({len(content['tips'])})", 
                    callback_data=f"tips_{subject_id}"
                )],
                [InlineKeyboardButton("🔙 Back to Subjects", callback_data="browse_subjects")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                f"📖 {subject['name']}\n\n"
                f"{subject['description']}\n\n"
                "Choose content type:",
                reply_markup=reply_markup
            )

async def show_videos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show videos for a subject"""
    query = update.callback_query
    await query.answer()
    
    subject_id = query.data.split("_")[1]
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/videos?subject_id={subject_id}")
        if response.status_code == 200:
            videos = response.json()
            
            if not videos:
                await query.edit_message_text(
                    "🎥 No videos available for this subject yet.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔙 Back", callback_data=f"subject_{subject_id}")
                    ]])
                )
                return
            
            message = "🎥 Videos:\n\n"
            for idx, video in enumerate(videos[:10], 1):  # Show first 10
                message += f"{idx}. {video['title']}\n"
                message += f"   📝 {video['description'][:50]}...\n"
                message += f"   🔗 {video['url']}\n\n"
            
            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data=f"subject_{subject_id}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(message, reply_markup=reply_markup)

async def show_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show files for a subject"""
    query = update.callback_query
    await query.answer()
    
    subject_id = query.data.split("_")[1]
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/files?subject_id={subject_id}")
        if response.status_code == 200:
            files = response.json()
            
            if not files:
                await query.edit_message_text(
                    "📁 No files available for this subject yet.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔙 Back", callback_data=f"subject_{subject_id}")
                    ]])
                )
                return
            
            message = "📁 Study Materials:\n\n"
            for idx, file in enumerate(files[:10], 1):
                message += f"{idx}. {file['title']}\n"
                message += f"   📝 {file['description'][:50]}...\n"
                message += f"   📥 Download: {BACKEND_URL}{file['download_url']}\n"
                message += f"   Size: {file['file_size'] / 1024:.2f} KB\n\n"
            
            keyboard = [[InlineKeyboardButton("🔙 Back", callback_data=f"subject_{subject_id}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(message, reply_markup=reply_markup)

async def show_topics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show topics for a subject"""
    query = update.callback_query
    await query.answer()
    
    subject_id = query.data.split("_")[1]
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/subjects/{subject_id}/topics")
        if response.status_code == 200:
            topics = response.json()
            
            if not topics:
                await query.edit_message_text(
                    "📑 No topics available for this subject yet.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔙 Back", callback_data=f"subject_{subject_id}")
                    ]])
                )
                return
            
            keyboard = []
            for topic in topics:
                keyboard.append([
                    InlineKeyboardButton(
                        f"📖 {topic['name']}", 
                        callback_data=f"topic_{topic['_id']}"
                    )
                ])
            keyboard.append([InlineKeyboardButton("🔙 Back", callback_data=f"subject_{subject_id}")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                "📑 Select a Topic:",
                reply_markup=reply_markup
            )

async def show_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show topic details"""
    query = update.callback_query
    await query.answer()
    
    topic_id = query.data.split("_")[1]
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/topics/{topic_id}")
        topic = response.json()
        
        content_response = await client.get(f"{BACKEND_URL}/api/topics/{topic_id}/content")
        content = content_response.json()
        
        keyboard = [
            [InlineKeyboardButton(
                f"🎥 Videos ({len(content['videos'])})", 
                callback_data=f"topic_videos_{topic_id}"
            )],
            [InlineKeyboardButton(
                f"📁 Files ({len(content['files'])})", 
                callback_data=f"topic_files_{topic_id}"
            )],
            [InlineKeyboardButton(
                f"📝 Quizzes ({len(content['quizzes'])})", 
                callback_data=f"topic_quizzes_{topic_id}"
            )],
            [InlineKeyboardButton(
                f"💡 Tips ({len(content['tips'])})", 
                callback_data=f"topic_tips_{topic_id}"
            )],
            [InlineKeyboardButton("🔙 Back", callback_data=f"topics_{topic['subject_id']}")}
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"📖 {topic['name']}\n\n"
            f"{topic['description']}\n\n"
            "Choose content type:",
            reply_markup=reply_markup
        )

async def admin_upload_file_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start file upload process"""
    query = update.callback_query
    await query.answer()
    
    telegram_id = str(query.from_user.id)
    
    # Get subjects for selection
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/subjects")
        if response.status_code == 200:
            subjects = response.json()
            
            if not subjects:
                await query.edit_message_text(
                    "❌ Please create at least one subject first.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("🔙 Back", callback_data="admin_panel")
                    ]])
                )
                return
            
            user_sessions[telegram_id] = {"subjects": subjects}
            
            keyboard = []
            for subject in subjects:
                keyboard.append([
                    InlineKeyboardButton(
                        subject['name'], 
                        callback_data=f"upload_subject_{subject['_id']}"
                    )
                ])
            keyboard.append([InlineKeyboardButton("🔙 Cancel", callback_data="admin_panel")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                "📁 File Upload - Step 1/5\n\n"
                "Select subject for the file:",
                reply_markup=reply_markup
            )

async def admin_upload_subject_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle subject selection for file upload"""
    query = update.callback_query
    await query.answer()
    
    telegram_id = str(query.from_user.id)
    subject_id = query.data.split("_")[2]
    
    if telegram_id not in user_sessions:
        user_sessions[telegram_id] = {}
    
    user_sessions[telegram_id]["upload_subject_id"] = subject_id
    
    # Get topics for the subject
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/api/subjects/{subject_id}/topics")
        if response.status_code == 200:
            topics = response.json()
            
            keyboard = [[InlineKeyboardButton("No Topic (General)", callback_data="upload_topic_none")]]
            for topic in topics:
                keyboard.append([
                    InlineKeyboardButton(
                        topic['name'], 
                        callback_data=f"upload_topic_{topic['_id']}"
                    )
                ])
            keyboard.append([InlineKeyboardButton("🔙 Cancel", callback_data="admin_panel")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(
                "📁 File Upload - Step 2/5\n\n"
                "Select topic (or choose 'No Topic'):",
                reply_markup=reply_markup
            )

async def admin_upload_topic_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle topic selection for file upload"""
    query = update.callback_query
    await query.answer()
    
    telegram_id = str(query.from_user.id)
    
    if "none" in query.data:
        user_sessions[telegram_id]["upload_topic_id"] = None
    else:
        topic_id = query.data.split("_")[2]
        user_sessions[telegram_id]["upload_topic_id"] = topic_id
    
    await query.edit_message_text(
        "📁 File Upload - Step 3/5\n\n"
        "Please enter the file title:"
    )
    
    user_sessions[telegram_id]["awaiting"] = "file_title"

async def admin_upload_title_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle file title input"""
    telegram_id = str(update.message.from_user.id)
    
    if telegram_id in user_sessions and user_sessions[telegram_id].get("awaiting") == "file_title":
        user_sessions[telegram_id]["upload_title"] = update.message.text
        user_sessions[telegram_id]["awaiting"] = "file_description"
        
        await update.message.reply_text(
            "📁 File Upload - Step 4/5\n\n"
            "Please enter the file description:"
        )

async def admin_upload_description_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle file description input"""
    telegram_id = str(update.message.from_user.id)
    
    if telegram_id in user_sessions and user_sessions[telegram_id].get("awaiting") == "file_description":
        user_sessions[telegram_id]["upload_description"] = update.message.text
        user_sessions[telegram_id]["awaiting"] = "file_upload"
        
        await update.message.reply_text(
            "📁 File Upload - Step 5/5\n\n"
            "Now send the file you want to upload."
        )

async def admin_file_received(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle file upload"""
    telegram_id = str(update.message.from_user.id)
    
    if telegram_id not in user_sessions or user_sessions[telegram_id].get("awaiting") != "file_upload":
        return
    
    # Show upload in progress
    progress_msg = await update.message.reply_text("⏳ Uploading file... 0%")
    
    try:
        # Get file from Telegram
        file = await update.message.document.get_file()
        
        await progress_msg.edit_text("⏳ Downloading from Telegram... 25%")
        
        # Download file
        file_path = f"/tmp/{update.message.document.file_name}"
        await file.download_to_drive(file_path)
        
        await progress_msg.edit_text("⏳ Uploading to server... 50%")
        
        # Get admin token
        token = await get_admin_token(telegram_id)
        
        # Upload to backend
        session = user_sessions[telegram_id]
        
        with open(file_path, 'rb') as f:
            files = {'file': (update.message.document.file_name, f, update.message.document.mime_type)}
            data = {
                'subject_id': session['upload_subject_id'],
                'topic_id': session.get('upload_topic_id', ''),
                'title': session['upload_title'],
                'description': session['upload_description'],
                'order': 0
            }
            
            async with httpx.AsyncClient(timeout=300.0) as client:
                await progress_msg.edit_text("⏳ Processing... 75%")
                
                response = await client.post(
                    f"{BACKEND_URL}/api/admin/files",
                    files=files,
                    data=data,
                    headers={"Authorization": f"Bearer {token}"}
                )
                
                await progress_msg.edit_text("⏳ Finalizing... 90%")
                
                if response.status_code == 200:
                    result = response.json()
                    download_url = f"{BACKEND_URL}{result['download_url']}"
                    
                    await progress_msg.edit_text(
                        "✅ File uploaded successfully!\n\n"
                        f"📁 {result['title']}\n"
                        f"📥 Download: {download_url}\n"
                        f"📊 Size: {result['file_size'] / 1024:.2f} KB"
                    )
                else:
                    await progress_msg.edit_text("❌ Upload failed. Please try again.")
        
        # Clean up
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Clear session
        user_sessions[telegram_id] = {}
        
    except Exception as e:
        await progress_msg.edit_text(f"❌ Error: {str(e)}")
        user_sessions[telegram_id] = {}

async def ai_assistant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """AI Assistant for queries"""
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        "🤖 AI Assistant\n\n"
        "Ask me anything about mechanical engineering!\n\n"
        "Simply type your question and I'll help you.",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🔙 Back", callback_data="back_to_main")
        ]])
    )

async def handle_ai_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle AI queries"""
    user_message = update.message.text
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BACKEND_URL}/api/ai/chat",
            json={"messages": [{"role": "user", "content": user_message}]}
        )
        
        if response.status_code == 200:
            data = response.json()
            await update.message.reply_text(f"🤖 {data['message']}")
        else:
            await update.message.reply_text("❌ AI service temporarily unavailable.")

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all callback queries"""
    query = update.callback_query
    
    if query.data == "back_to_main":
        await query.answer()
        keyboard = [
            [InlineKeyboardButton("📚 Browse Subjects", callback_data="browse_subjects")],
            [InlineKeyboardButton("🔍 Search Content", callback_data="search")],
            [InlineKeyboardButton("🤖 AI Assistant", callback_data="ai_assist")],
            [InlineKeyboardButton("👨‍💼 Admin Panel", callback_data="admin_login")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🎓 Main Menu\n\nChoose an option:",
            reply_markup=reply_markup
        )
    elif query.data == "browse_subjects":
        await browse_subjects(update, context)
    elif query.data.startswith("subject_"):
        await show_subject(update, context)
    elif query.data.startswith("videos_"):
        await show_videos(update, context)
    elif query.data.startswith("files_"):
        await show_files(update, context)
    elif query.data.startswith("topics_"):
        await show_topics(update, context)
    elif query.data.startswith("topic_") and not query.data.startswith("topic_videos") and not query.data.startswith("topic_files"):
        await show_topic(update, context)
    elif query.data == "admin_login" or query.data == "admin_panel":
        await admin_login_start(update, context)
    elif query.data == "admin_upload_file":
        await admin_upload_file_start(update, context)
    elif query.data.startswith("upload_subject_"):
        await admin_upload_subject_selected(update, context)
    elif query.data.startswith("upload_topic_"):
        await admin_upload_topic_selected(update, context)
    elif query.data == "ai_assist":
        await ai_assistant(update, context)

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages"""
    telegram_id = str(update.message.from_user.id)
    
    # Check if awaiting input for file upload
    if telegram_id in user_sessions:
        if user_sessions[telegram_id].get("awaiting") == "file_title":
            await admin_upload_title_received(update, context)
            return
        elif user_sessions[telegram_id].get("awaiting") == "file_description":
            await admin_upload_description_received(update, context)
            return
    
    # Otherwise treat as AI query
    await handle_ai_query(update, context)

async def document_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle document uploads"""
    await admin_file_received(update, context)

def main():
    """Start the bot"""
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not set in .env file")
        return
    
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(callback_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    application.add_handler(MessageHandler(filters.Document.ALL, document_handler))
    
    print("Bot started successfully!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
