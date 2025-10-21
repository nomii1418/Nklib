from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import os

from .database import connect_to_mongo, close_mongo_connection
from .routes import admin, public, auth, ai

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()

app = FastAPI(
    title="Mechanical Engineering Library API",
    description="API for mechanical engineering learning platform",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount uploads directory
os.makedirs("/workspace/uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="/workspace/uploads"), name="uploads")

# Include routers
app.include_router(auth.router)
app.include_router(public.router)
app.include_router(admin.router)
app.include_router(ai.router)

@app.get("/")
async def root():
    return {
        "message": "Mechanical Engineering Library API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}
