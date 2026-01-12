import os
from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Datenbank-URL sauber aus Env lesen
POSTGRES_URL = (
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:"
    f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(POSTGRES_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class NoteModel(Base):
    __tablename__ = "notes"
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)

# Tabellen erstellen (einmal beim Start)
Base.metadata.create_all(bind=engine)

# --- CRUD-Funktionen ---
def create_note(session: Session, id: str, title: str, content: str) -> NoteModel:
    note = NoteModel(id=id, title=title, content=content)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

def get_notes(session: Session):
    return session.query(NoteModel).all()

def get_note(session: Session, note_id: str):
    return session.query(NoteModel).filter(NoteModel.id == note_id).first()

def delete_note(session: Session, note_id: str) -> bool:
    note = get_note(session, note_id)
    if note:
        session.delete(note)
        session.commit()
        return True
    return False
