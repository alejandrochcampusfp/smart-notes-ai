from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from app.database import engine, Base, get_db
from app.models import NoteModel
from app.schemas import NoteCreate, NoteResponse
from app.crud import get_notes, create_note, delete_note
from app.ai_service import generate_note_summary

# Creamos las tablas en SQLite automáticamente si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartNotes AI API",
    description="Microservicio seguro con FastAPI, SQLAlchemy y Groq IA para gestión de notas.",
    version="1.0.0"
)

# Montamos la carpeta estática para servir la interfaz visual
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", include_in_schema=False)
def serve_frontend():
    # Sirve automáticamente la interfaz visual en la ruta principal
    return FileResponse("app/static/index.html")

# Endpoints de la API con control estricto de métodos HTTP y códigos de estado
@app.get("/api/notes", response_model=List[NoteResponse], status_code=status.HTTP_200_OK)
def api_get_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_notes(db, skip=skip, limit=limit)

@app.post("/api/notes", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def api_create_note(note: NoteCreate, db: Session = Depends(get_db)):
    # Generamos el resumen inteligente mediante la IA de forma aislada
    summary = generate_note_summary(note.content)
    return create_note(db=db, note=note, ai_summary=summary)

@app.delete("/api/notes/{note_id}", status_code=status.HTTP_200_OK)
def api_delete_note(note_id: int, db: Session = Depends(get_db)):
    success = delete_note(db, note_id)
    if not success:
        # Manejo limpio de errores controlados para evitar filtraciones o caídas de servidor
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La nota solicitada no existe."
        )
    return {"message": "Nota eliminada correctamente"}