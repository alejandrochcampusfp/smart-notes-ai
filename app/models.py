from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class NoteModel(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    ai_summary = Column(Text, nullable=True) # Campo para guardar el resumen generado por IA
    created_at = Column(DateTime, default=datetime.utcnow)