from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from ..database import get_database
from ..auth import verify_password, get_password_hash, create_access_token
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/auth", tags=["auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    is_admin: bool
    username: str

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    db = get_database()
    
    # Check if it's the default admin
    admin_username = os.getenv("ADMIN_USERNAME", "nk28")
    admin_password = os.getenv("ADMIN_PASSWORD", "nom")
    
    if request.username == admin_username and request.password == admin_password:
        access_token = create_access_token(
            data={"sub": request.username, "is_admin": True},
            expires_delta=timedelta(days=30)
        )
        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
            is_admin=True,
            username=request.username
        )
    
    # Check database for other users
    user = await db.users.find_one({"username": request.username})
    if not user or not verify_password(request.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(
        data={"sub": user["username"], "is_admin": user.get("is_admin", False)},
        expires_delta=timedelta(days=30)
    )
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        is_admin=user.get("is_admin", False),
        username=user["username"]
    )

@router.post("/register")
async def register(request: LoginRequest):
    db = get_database()
    
    # Check if user already exists
    existing_user = await db.users.find_one({"username": request.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Create new user
    user = {
        "username": request.username,
        "password_hash": get_password_hash(request.password),
        "is_admin": False
    }
    await db.users.insert_one(user)
    
    return {"message": "User registered successfully"}
