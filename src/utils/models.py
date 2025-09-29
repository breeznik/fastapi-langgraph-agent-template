"""
Pydantic models for API request and response schemas.
"""
from pydantic import BaseModel
from typing import Optional, Any, Dict

class ChatRequest(BaseModel):
    message: str
    checkpoint_id: Optional[str] = None

class ChatResponse(BaseModel):
    content: dict
    checkpoint_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    state: Optional[Dict[str, Any]] = None
    status: str 
    
class ErrorResponse(BaseModel):
    error: str
    type: str
    message: str
    context: Optional[Dict[str, Any]] = None
    request_id: Optional[str] = None

class UpdateModelRequest(BaseModel):
    ai_model: str

class UpdateModelResponse(BaseModel):
    message: str
    ai_model: str
    status: str
