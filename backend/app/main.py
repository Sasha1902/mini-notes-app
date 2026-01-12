from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.db import SessionLocal, NoteModel
import uuid

app = FastAPI()

# CORS
origins = ["http://localhost:5173", "http://localhost:5174"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Healthcheck
@app.get("/health")
def health():
    return {"status": "ok", "db": "connected"}

# Dependency
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        

# CRUD Endpoints
@app.post("/notes")
def create_note(payload: dict, session: Session = Depends(get_session)):
    if "title" not in payload or "content" not in payload:
        raise HTTPException(status_code=400, detail="Missing title or content")
    note = NoteModel(id=str(uuid.uuid4()), title=payload["title"], content=payload["content"])
    session.add(note)
    session.commit()
    session.refresh(note)
    return {"id": note.id, "title": note.title, "content": note.content}

@app.get("/notes")
def read_notes(session: Session = Depends(get_session)):
    notes = session.query(NoteModel).all()
    return [{"id": n.id, "title": n.title, "content": n.content} for n in notes]

@app.get("/notes/{note_id}")
def read_note(note_id: str, session: Session = Depends(get_session)):
    note = session.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note.id, "title": note.title, "content": note.content}

@app.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: str, session: Session = Depends(get_session)):
    note = session.query(NoteModel).filter(NoteModel.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    return {"status": "deleted"}
