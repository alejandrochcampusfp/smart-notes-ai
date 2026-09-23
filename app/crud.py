from sqlalchemy.orm import Session
from app.models import NoteModel
from app.schemas import NoteCreate

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    # Consulta segura y parametrizada ordenada de más reciente a más antigua
    return db.query(NoteModel).order_by(NoteModel.created_at.desc()).offset(skip).limit(limit).all()

def create_note(db: Session, note: NoteCreate, ai_summary: str = None):
    db_note = NoteModel(
        title=note.title,
        content=note.content,
        ai_summary=ai_summary
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = db.query(NoteModel).filter(NoteModel.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
        return True
    return False