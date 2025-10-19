from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "mechanical_library")

client = None
database = None

async def connect_to_mongo():
    global client, database
    client = AsyncIOMotorClient(MONGODB_URL)
    database = client[DATABASE_NAME]
    
    # Create indexes
    await database.subjects.create_index([("order", ASCENDING)])
    await database.topics.create_index([("subject_id", ASCENDING), ("order", ASCENDING)])
    await database.videos.create_index([("subject_id", ASCENDING), ("topic_id", ASCENDING)])
    await database.files.create_index([("subject_id", ASCENDING), ("topic_id", ASCENDING)])
    await database.quizzes.create_index([("subject_id", ASCENDING), ("topic_id", ASCENDING)])
    await database.tips.create_index([("subject_id", ASCENDING), ("topic_id", ASCENDING)])
    await database.users.create_index([("username", ASCENDING)], unique=True)
    
    print("Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Closed MongoDB connection")

def get_database():
    return database
