from pydantic import BaseModel , Field

class sample_schema(BaseModel):
    message:str = Field(...,description="AI message to human")
    