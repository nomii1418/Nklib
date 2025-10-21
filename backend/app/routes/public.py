from fastapi import APIRouter, HTTPException, Response
from typing import List, Optional
from ..database import get_database
from bson import ObjectId
import os

router = APIRouter(prefix="/api", tags=["public"])

# Get all subjects
@router.get("/subjects")
async def get_subjects():
    db = get_database()
    subjects = []
    async for subject in db.subjects.find().sort("order", 1):
        subject["_id"] = str(subject["_id"])
        subjects.append(subject)
    return subjects

# Get subject by ID
@router.get("/subjects/{subject_id}")
async def get_subject(subject_id: str):
    db = get_database()
    subject = await db.subjects.find_one({"_id": ObjectId(subject_id)})
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    subject["_id"] = str(subject["_id"])
    return subject

# Get topics by subject
@router.get("/subjects/{subject_id}/topics")
async def get_topics(subject_id: str):
    db = get_database()
    topics = []
    async for topic in db.topics.find({"subject_id": subject_id}).sort("order", 1):
        topic["_id"] = str(topic["_id"])
        topics.append(topic)
    return topics

# Get topic by ID
@router.get("/topics/{topic_id}")
async def get_topic(topic_id: str):
    db = get_database()
    topic = await db.topics.find_one({"_id": ObjectId(topic_id)})
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    topic["_id"] = str(topic["_id"])
    return topic

# Get videos
@router.get("/videos")
async def get_videos(subject_id: Optional[str] = None, topic_id: Optional[str] = None):
    db = get_database()
    query = {}
    if subject_id:
        query["subject_id"] = subject_id
    if topic_id:
        query["topic_id"] = topic_id
    
    videos = []
    async for video in db.videos.find(query).sort("order", 1):
        video["_id"] = str(video["_id"])
        videos.append(video)
    return videos

# Get video by ID
@router.get("/videos/{video_id}")
async def get_video(video_id: str):
    db = get_database()
    video = await db.videos.find_one({"_id": ObjectId(video_id)})
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    video["_id"] = str(video["_id"])
    return video

# Get files
@router.get("/files")
async def get_files(subject_id: Optional[str] = None, topic_id: Optional[str] = None):
    db = get_database()
    query = {}
    if subject_id:
        query["subject_id"] = subject_id
    if topic_id:
        query["topic_id"] = topic_id
    
    files = []
    async for file in db.files.find(query).sort("order", 1):
        file["_id"] = str(file["_id"])
        files.append(file)
    return files

# Get file by ID
@router.get("/files/{file_id}")
async def get_file(file_id: str):
    db = get_database()
    file = await db.files.find_one({"_id": ObjectId(file_id)})
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    file["_id"] = str(file["_id"])
    return file

# Download file
@router.get("/files/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join("/workspace/uploads", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open(file_path, "rb") as f:
        content = f.read()
    
    return Response(
        content=content,
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

# Get quizzes
@router.get("/quizzes")
async def get_quizzes(subject_id: Optional[str] = None, topic_id: Optional[str] = None):
    db = get_database()
    query = {}
    if subject_id:
        query["subject_id"] = subject_id
    if topic_id:
        query["topic_id"] = topic_id
    
    quizzes = []
    async for quiz in db.quizzes.find(query).sort("order", 1):
        quiz["_id"] = str(quiz["_id"])
        quizzes.append(quiz)
    return quizzes

# Get quiz by ID
@router.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id: str):
    db = get_database()
    quiz = await db.quizzes.find_one({"_id": ObjectId(quiz_id)})
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    quiz["_id"] = str(quiz["_id"])
    return quiz

# Get tips
@router.get("/tips")
async def get_tips(subject_id: Optional[str] = None, topic_id: Optional[str] = None):
    db = get_database()
    query = {}
    if subject_id:
        query["subject_id"] = subject_id
    if topic_id:
        query["topic_id"] = topic_id
    
    tips = []
    async for tip in db.tips.find(query).sort("order", 1):
        tip["_id"] = str(tip["_id"])
        tips.append(tip)
    return tips

# Get tip by ID
@router.get("/tips/{tip_id}")
async def get_tip(tip_id: str):
    db = get_database()
    tip = await db.tips.find_one({"_id": ObjectId(tip_id)})
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")
    tip["_id"] = str(tip["_id"])
    return tip

# Get all content for a subject
@router.get("/subjects/{subject_id}/content")
async def get_subject_content(subject_id: str):
    db = get_database()
    
    # Get topics
    topics = []
    async for topic in db.topics.find({"subject_id": subject_id}).sort("order", 1):
        topic["_id"] = str(topic["_id"])
        topics.append(topic)
    
    # Get videos
    videos = []
    async for video in db.videos.find({"subject_id": subject_id}).sort("order", 1):
        video["_id"] = str(video["_id"])
        videos.append(video)
    
    # Get files
    files = []
    async for file in db.files.find({"subject_id": subject_id}).sort("order", 1):
        file["_id"] = str(file["_id"])
        files.append(file)
    
    # Get quizzes
    quizzes = []
    async for quiz in db.quizzes.find({"subject_id": subject_id}).sort("order", 1):
        quiz["_id"] = str(quiz["_id"])
        quizzes.append(quiz)
    
    # Get tips
    tips = []
    async for tip in db.tips.find({"subject_id": subject_id}).sort("order", 1):
        tip["_id"] = str(tip["_id"])
        tips.append(tip)
    
    return {
        "topics": topics,
        "videos": videos,
        "files": files,
        "quizzes": quizzes,
        "tips": tips
    }

# Get all content for a topic
@router.get("/topics/{topic_id}/content")
async def get_topic_content(topic_id: str):
    db = get_database()
    
    # Get videos
    videos = []
    async for video in db.videos.find({"topic_id": topic_id}).sort("order", 1):
        video["_id"] = str(video["_id"])
        videos.append(video)
    
    # Get files
    files = []
    async for file in db.files.find({"topic_id": topic_id}).sort("order", 1):
        file["_id"] = str(file["_id"])
        files.append(file)
    
    # Get quizzes
    quizzes = []
    async for quiz in db.quizzes.find({"topic_id": topic_id}).sort("order", 1):
        quiz["_id"] = str(quiz["_id"])
        quizzes.append(quiz)
    
    # Get tips
    tips = []
    async for tip in db.tips.find({"topic_id": topic_id}).sort("order", 1):
        tip["_id"] = str(tip["_id"])
        tips.append(tip)
    
    return {
        "videos": videos,
        "files": files,
        "quizzes": quizzes,
        "tips": tips
    }
