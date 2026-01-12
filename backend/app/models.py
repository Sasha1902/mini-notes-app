from dataclasses import dataclass
import uuid

@dataclass
class Note:
    id: str
    title: str
    content: str

    @staticmethod
    def new(title: str, content: str) -> "Note":
        return Note(id=str(uuid.uuid4()), title=title, content=content)
