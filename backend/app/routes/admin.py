from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from typing import List, Optional
from ..database import get_database
from ..auth import get_admin_user
from ..models import Subject, Topic, Video, File as FileModel, Quiz, Tip
from bson import ObjectId
from datetime import datetime
import aiofiles
import os
import shutil

router = APIRouter(prefix="/api/admin", tags=["admin"])

# Subjects
@router.post("/subjects")
async def create_subject(
    name: str = Form(...),
    description: str = Form(...),
    icon: Optional[str] = Form(None),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    subject = {
        "name": name,
        "description": description,
        "icon": icon,
        "order": order,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await db.subjects.insert_one(subject)
    subject["_id"] = str(result.inserted_id)
    return subject

@router.put("/subjects/{subject_id}")
async def update_subject(
    subject_id: str,
    name: str = Form(...),
    description: str = Form(...),
    icon: Optional[str] = Form(None),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    update_data = {
        "name": name,
        "description": description,
        "icon": icon,
        "order": order,
        "updated_at": datetime.utcnow()
    }
    result = await db.subjects.update_one(
        {"_id": ObjectId(subject_id)},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"message": "Subject updated successfully"}

@router.delete("/subjects/{subject_id}")
async def delete_subject(
    subject_id: str,
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    
    # Delete all related content
    await db.topics.delete_many({"subject_id": subject_id})
    await db.videos.delete_many({"subject_id": subject_id})
    await db.files.delete_many({"subject_id": subject_id})
    await db.quizzes.delete_many({"subject_id": subject_id})
    await db.tips.delete_many({"subject_id": subject_id})
    
    result = await db.subjects.delete_one({"_id": ObjectId(subject_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"message": "Subject and related content deleted successfully"}

# Topics
@router.post("/topics")
async def create_topic(
    subject_id: str = Form(...),
    name: str = Form(...),
    description: str = Form(...),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    topic = {
        "subject_id": subject_id,
        "name": name,
        "description": description,
        "order": order,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await db.topics.insert_one(topic)
    topic["_id"] = str(result.inserted_id)
    return topic

@router.put("/topics/{topic_id}")
async def update_topic(
    topic_id: str,
    subject_id: str = Form(...),
    name: str = Form(...),
    description: str = Form(...),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    update_data = {
        "subject_id": subject_id,
        "name": name,
        "description": description,
        "order": order,
        "updated_at": datetime.utcnow()
    }
    result = await db.topics.update_one(
        {"_id": ObjectId(topic_id)},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {"message": "Topic updated successfully"}

@router.delete("/topics/{topic_id}")
async def delete_topic(
    topic_id: str,
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    
    # Delete all related content
    await db.videos.delete_many({"topic_id": topic_id})
    await db.files.delete_many({"topic_id": topic_id})
    await db.quizzes.delete_many({"topic_id": topic_id})
    await db.tips.delete_many({"topic_id": topic_id})
    
    result = await db.topics.delete_one({"_id": ObjectId(topic_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {"message": "Topic and related content deleted successfully"}

# Videos
@router.post("/videos")
async def create_video(
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    description: str = Form(...),
    url: str = Form(...),
    thumbnail: Optional[str] = Form(None),
    duration: Optional[str] = Form(None),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    video = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "description": description,
        "url": url,
        "thumbnail": thumbnail,
        "duration": duration,
        "order": order,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await db.videos.insert_one(video)
    video["_id"] = str(result.inserted_id)
    return video

@router.put("/videos/{video_id}")
async def update_video(
    video_id: str,
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    description: str = Form(...),
    url: str = Form(...),
    thumbnail: Optional[str] = Form(None),
    duration: Optional[str] = Form(None),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    update_data = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "description": description,
        "url": url,
        "thumbnail": thumbnail,
        "duration": duration,
        "order": order,
        "updated_at": datetime.utcnow()
    }
    result = await db.videos.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Video not found")
    return {"message": "Video updated successfully"}

@router.delete("/videos/{video_id}")
async def delete_video(
    video_id: str,
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    result = await db.videos.delete_one({"_id": ObjectId(video_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Video not found")
    return {"message": "Video deleted successfully"}

# Files
@router.post("/files")
async def create_file(
    file: UploadFile = File(...),
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    description: str = Form(...),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    from ..cloudinary_config import upload_file_to_cloudinary
    
    db = get_database()
    
    # Read file content
    content = await file.read()
    file_size = len(content)
    
    # Upload to Cloudinary
    try:
        cloudinary_result = await upload_file_to_cloudinary(
            content,
            file.filename,
            folder=f"mechanical_library/{subject_id}"
        )
        
        file_doc = {
            "subject_id": subject_id,
            "topic_id": topic_id,
            "title": title,
            "description": description,
            "filename": file.filename,
            "cloudinary_url": cloudinary_result["url"],
            "cloudinary_public_id": cloudinary_result["public_id"],
            "file_type": file.content_type,
            "file_size": file_size,
            "download_url": cloudinary_result["url"],
            "order": order,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = await db.files.insert_one(file_doc)
        file_doc["_id"] = str(result.inserted_id)
        return file_doc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@router.put("/files/{file_id}")
async def update_file(
    file_id: str,
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    description: str = Form(...),
    order: int = Form(0),
    file: Optional[UploadFile] = File(None),
    current_user: dict = Depends(get_admin_user)
):
    from ..cloudinary_config import upload_file_to_cloudinary, delete_file_from_cloudinary
    
    db = get_database()
    
    update_data = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "description": description,
        "order": order,
        "updated_at": datetime.utcnow()
    }
    
    if file:
        # Delete old file from Cloudinary
        old_file = await db.files.find_one({"_id": ObjectId(file_id)})
        if old_file and old_file.get("cloudinary_public_id"):
            try:
                await delete_file_from_cloudinary(old_file["cloudinary_public_id"])
            except:
                pass  # Continue even if deletion fails
        
        # Upload new file to Cloudinary
        content = await file.read()
        cloudinary_result = await upload_file_to_cloudinary(
            content,
            file.filename,
            folder=f"mechanical_library/{subject_id}"
        )
        
        update_data.update({
            "filename": file.filename,
            "cloudinary_url": cloudinary_result["url"],
            "cloudinary_public_id": cloudinary_result["public_id"],
            "file_type": file.content_type,
            "file_size": len(content),
            "download_url": cloudinary_result["url"]
        })
    
    result = await db.files.update_one(
        {"_id": ObjectId(file_id)},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File updated successfully"}

@router.delete("/files/{file_id}")
async def delete_file(
    file_id: str,
    current_user: dict = Depends(get_admin_user)
):
    from ..cloudinary_config import delete_file_from_cloudinary
    
    db = get_database()
    file_doc = await db.files.find_one({"_id": ObjectId(file_id)})
    if not file_doc:
        raise HTTPException(status_code=404, detail="File not found")
    
    # Delete file from Cloudinary
    if file_doc.get("cloudinary_public_id"):
        try:
            await delete_file_from_cloudinary(file_doc["cloudinary_public_id"])
        except Exception as e:
            print(f"Failed to delete from Cloudinary: {e}")
            # Continue deletion from database even if Cloudinary fails
    
    await db.files.delete_one({"_id": ObjectId(file_id)})
    return {"message": "File deleted successfully"}

# Quizzes
@router.post("/quizzes")
async def create_quiz(
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    description: str = Form(...),
    questions: str = Form(...),  # JSON string
    duration: Optional[int] = Form(None),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    import json
    db = get_database()
    
    quiz = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "description": description,
        "questions": json.loads(questions),
        "duration": duration,
        "order": order,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await db.quizzes.insert_one(quiz)
    quiz["_id"] = str(result.inserted_id)
    return quiz

@router.put("/quizzes/{quiz_id}")
async def update_quiz(
    quiz_id: str,
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    description: str = Form(...),
    questions: str = Form(...),
    duration: Optional[int] = Form(None),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    import json
    db = get_database()
    
    update_data = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "description": description,
        "questions": json.loads(questions),
        "duration": duration,
        "order": order,
        "updated_at": datetime.utcnow()
    }
    result = await db.quizzes.update_one(
        {"_id": ObjectId(quiz_id)},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return {"message": "Quiz updated successfully"}

@router.delete("/quizzes/{quiz_id}")
async def delete_quiz(
    quiz_id: str,
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    result = await db.quizzes.delete_one({"_id": ObjectId(quiz_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return {"message": "Quiz deleted successfully"}

# Tips
@router.post("/tips")
async def create_tip(
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    content: str = Form(...),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    tip = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "content": content,
        "order": order,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    result = await db.tips.insert_one(tip)
    tip["_id"] = str(result.inserted_id)
    return tip

@router.put("/tips/{tip_id}")
async def update_tip(
    tip_id: str,
    subject_id: str = Form(...),
    topic_id: Optional[str] = Form(None),
    title: str = Form(...),
    content: str = Form(...),
    order: int = Form(0),
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    update_data = {
        "subject_id": subject_id,
        "topic_id": topic_id,
        "title": title,
        "content": content,
        "order": order,
        "updated_at": datetime.utcnow()
    }
    result = await db.tips.update_one(
        {"_id": ObjectId(tip_id)},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Tip not found")
    return {"message": "Tip updated successfully"}

@router.delete("/tips/{tip_id}")
async def delete_tip(
    tip_id: str,
    current_user: dict = Depends(get_admin_user)
):
    db = get_database()
    result = await db.tips.delete_one({"_id": ObjectId(tip_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tip not found")
    return {"message": "Tip deleted successfully"}
