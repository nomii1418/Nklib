from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta
from typing import Optional
import os
import hashlib
import secrets
import hmac
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production-minimum-32-characters-long")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60  # 30 days

security = HTTPBearer()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password using PBKDF2-SHA256 (pure Python, no Rust/C dependencies)
    This is secure, fast, and works on any platform including Render free tier
    """
    try:
        # Extract salt and hash from stored password
        parts = hashed_password.split('$')
        if len(parts) != 2:
            return False
        salt, stored_hash = parts
        
        # Hash the plain password with the same salt
        computed_hash = hashlib.pbkdf2_hmac(
            'sha256',
            plain_password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # 100k iterations (secure and fast)
        ).hex()
        
        # Use constant-time comparison to prevent timing attacks
        return hmac.compare_digest(computed_hash, stored_hash)
    except Exception:
        return False

def get_password_hash(password: str) -> str:
    """
    Hash password using PBKDF2-SHA256 (pure Python, no Rust/C dependencies)
    NIST-approved, industry standard, same security as bcrypt
    """
    # Generate a cryptographically secure random salt
    salt = secrets.token_hex(16)  # 32 character hex string
    
    # Hash the password with PBKDF2-HMAC-SHA256
    pwd_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000  # 100,000 iterations (NIST recommends 10k minimum, we use 10x)
    ).hex()
    
    # Return salt and hash combined (format: salt$hash)
    return f"{salt}${pwd_hash}"

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token using PyJWT (pure Python)"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token and return user info"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return {"username": username, "is_admin": payload.get("is_admin", False)}
    except jwt.InvalidTokenError:
        raise credentials_exception
    except Exception:
        raise credentials_exception

async def get_admin_user(current_user: dict = Depends(get_current_user)):
    """Check if current user is admin"""
    if not current_user.get("is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user
