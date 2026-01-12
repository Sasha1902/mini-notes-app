export interface Note { 
  id: string;
  title: string;
  content: string;
}

const API_URL = import.meta.env.VITE_API_URL as string;

export async function fetchNotes(): Promise<Note[]> {
  const res = await fetch(`${API_URL}/notes`);
  return res.json();
}

export async function createNote(title: string, content: string): Promise<Note> {
  const res = await fetch(`${API_URL}/notes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, content }),
  });
  return res.json();
}

export async function deleteNote(id: string): Promise<void> {
  await fetch(`${API_URL}/notes/${id}`, { method: "DELETE" });
}
