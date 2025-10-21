from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from typing import List

router = APIRouter(prefix="/api/ai", tags=["ai"])

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    message: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    AI Assistant using free Hugging Face Inference API
    You can replace this with any other free AI API
    """
    try:
        # Using Hugging Face's free inference API
        # You can sign up for a free API key at huggingface.co
        
        # For demo purposes, using a simple response system
        # In production, integrate with actual AI API
        
        last_message = request.messages[-1].content if request.messages else ""
        
        # Simple keyword-based responses for mechanical engineering
        if "thermodynamics" in last_message.lower():
            response = "Thermodynamics is the study of energy, heat, and work. The four laws of thermodynamics govern energy transfer and transformation. How can I help you with thermodynamics?"
        elif "mechanics" in last_message.lower():
            response = "Mechanics deals with forces and motion. It includes statics (bodies at rest) and dynamics (bodies in motion). What specific topic in mechanics would you like to explore?"
        elif "fluid" in last_message.lower():
            response = "Fluid mechanics studies the behavior of liquids and gases. Key concepts include pressure, flow rate, viscosity, and turbulence. What aspect of fluid mechanics interests you?"
        elif "material" in last_message.lower():
            response = "Material science covers properties, behavior, and selection of engineering materials like metals, polymers, ceramics, and composites. What would you like to know?"
        elif "manufacturing" in last_message.lower():
            response = "Manufacturing processes include casting, machining, forming, joining, and additive manufacturing. Each has specific applications and advantages. What process are you interested in?"
        else:
            response = f"I'm your AI assistant for mechanical engineering. I can help with topics like thermodynamics, mechanics, fluid dynamics, materials, manufacturing, and more. How can I assist you today?"
        
        return ChatResponse(message=response)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")

@router.get("/suggestions")
async def get_suggestions():
    """Get AI-powered study suggestions"""
    return {
        "suggestions": [
            "Start with fundamental concepts in thermodynamics",
            "Practice solving mechanics problems daily",
            "Watch video tutorials for complex topics",
            "Take quizzes to test your understanding",
            "Review material properties and their applications"
        ]
    }
