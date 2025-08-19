from fastapi import FastAPI, HTTPException
from typing import List
from models import Note, NoteCreate, NoteUpdate
from database import notes_db, get_next_id
from fastapi import Depends, Header

API_KEY = "xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")

@app.get("/notes", response_model=List[Note])
def get_notes(dep: str = Depends(verify_api_key)):
    return notes_db

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, dep: str = Depends(verify_api_key)):
    note = next((n for n in notes_db if n.id == note_id), None)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes", response_model=Note, status_code=201)
def create_note(note_data: NoteCreate, dep: str = Depends(verify_api_key)):
    new_note = Note(id=get_next_id(), **note_data.dict())
    notes_db.append(new_note)
    return new_note

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_data: NoteUpdate, dep: str = Depends(verify_api_key)):
    note = next((n for n in notes_db if n.id == note_id), None)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    if note_data.title is not None:
        note.title = note_data.title
    if note_data.content is not None:
        note.content = note_data.content

    return note

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, dep: str = Depends(verify_api_key)):
    global notes_db
    note = next((n for n in notes_db if n.id == note_id), None)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    notes_db = [n for n in notes_db if n.id != note_id]
    return
