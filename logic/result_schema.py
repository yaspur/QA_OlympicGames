from pydantic import BaseModel

class LLMResponse(BaseModel):
    resultado: str

class Data(BaseModel):
    
    process: LLMResponse
    query: str