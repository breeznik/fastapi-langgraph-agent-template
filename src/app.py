from fastapi import FastAPI
from contextlib import asynccontextmanager
import sys
from fastapi.responses import FileResponse
# from src.mcp.mcp_client import init_tool_service
from fastapi.middleware.cors import CORSMiddleware
from src.utils import models , util
from src.controller.chat import Chat
import asyncio

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    # await init_tool_service()
    yield
    
# fast interface
app = FastAPI(lifespan=lifespan)


#cores
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-Type"],
)

@app.get("/")
async def root():
    return {"message": "The server is up and running"}

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("assets/favicon.ico")

@app.post("/api/chat", response_model=models.ChatResponse)
async def chat_endpoint(request: models.ChatRequest):
    try:
        controller = Chat(
            message=request.message,
            checkpoint_id=request.checkpoint_id,
        )
        content = await asyncio.wait_for(controller.run(), timeout=30)
        print("printing content" , content)
        data = util.reply_extractor(content)
        return models.ChatResponse(
            content=data,
            checkpoint_id=request.checkpoint_id,
            metadata=content,
            status="complete"
        )
        
    except asyncio.TimeoutError:
        print("Request timed out")
        return models.ChatResponse(
            content={"message": "Request timed out. Please try again.", "data": {}},
            checkpoint_id=request.checkpoint_id,
            metadata={},
            status="timeout"
        )
    except Exception as error:
        print(f"Error in chat endpoint: {error}")
        return models.ChatResponse(
            content={"message": "An error occurred while processing your request.", "data": {}},
            checkpoint_id=request.checkpoint_id,
            metadata={"error": str(error)},
            status="error"
        )
