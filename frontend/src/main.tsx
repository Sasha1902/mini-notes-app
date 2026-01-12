import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";
import { fetchNotes, createNote, deleteNote, Note } from "./api";

const App = () => {
  const [notes, setNotes] = useState<Note[]>([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const loadNotes = async () => {
    const data = await fetchNotes();
    setNotes(data);
  };

  const handleAdd = async () => {
    if (!title || !content) return;
    const newNote = await createNote(title, content);
    setNotes((prev) => [...prev, newNote]);
    setTitle("");
    setContent("");
  };

  const handleDelete = async (id: string) => {
    await deleteNote(id);
    setNotes((prev) => prev.filter((n) => n.id !== id));
  };

  useEffect(() => { loadNotes(); }, []);

  return (
    <div style={{ padding: 32 }}>
      <h1>Mini Notes App 111</h1>

      <div style={{ marginBottom: 16 }}>
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ marginRight: 8 }}
        />
        <input
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          style={{ marginRight: 8 }}
        />
        <button onClick={handleAdd}>Add Note</button>
      </div>

      <ul>
        {notes.map((note) => (
          <li key={note.id}>
            <strong>{note.title}</strong>: {note.content}{" "}
            <button onClick={() => handleDelete(note.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")!).render(<App />);
