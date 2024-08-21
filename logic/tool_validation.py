from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Literal

class ResponseValidation(BaseModel):
    """responder yes solo si la pregunta tiene que ver con los juegos olimpicos, responder no si la pregunta tiene que ver con otra cosa que no sean los juegos olimpicos"""
    
    resultado: Literal["yes", "no"] = Field(..., description="responder yes solo si la pregunta tiene que ver con los juegos olimpicos, responder no si la pregunta tiene que ver con otra cosa que no sean los juegos olimpicos")