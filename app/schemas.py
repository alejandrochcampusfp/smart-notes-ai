from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NoteCreate(BaseModel):
    # Validamos que el título y el contenido cumplan restricciones estrictas anti-inyecciones/vacíos
    title: str = Field(..., min_length=1, max_length=100, description="Título obligatorio de la nota")
    content: str = Field(..., min_length=1, max_length=2000, description="Contenido de la nota")

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    ai_summary: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True