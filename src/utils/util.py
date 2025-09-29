from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

base_url:str = os.getenv("OPENROUTER_URL")
api_key:str = os.getenv("OPENROUTER_API_KEY")

def model_creator(model):
    localized_model = ChatOpenAI(model=model, api_key=api_key,base_url=base_url,temperature=0,max_retries=1,timeout=15)
    return localized_model

# it can be changed to reply with the last ai message
def reply_extractor(content):
    # Get messages list safely
    messages = content.get("messages", [])
    last_msg = messages[-1] if messages else None
    
    # Step 1: Check for interrupt
    interrupt = content.get("__interrupt__", [])
    if interrupt:
        reply = interrupt[0].value
    
    # Step 2: Fallback to last message content
    else:
        if messages and last_msg:
            if hasattr(last_msg, "content"):
                reply = last_msg.content
            elif isinstance(last_msg, dict):
                reply = last_msg.get("content", "No content found.")
            else:
                reply = str(last_msg)
        else:
            reply = "No messages found."
            
    data = {"message": reply, "data": {}}
    
    
    # Check if last_msg has 'client_events' attribute
    # if "client_events" in content:
    #     data["data"] = {**data["data"] , "cart": data.get("cart", {}) , "client_events": content["client_events"]}
    
    return data