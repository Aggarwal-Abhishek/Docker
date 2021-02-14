import uuid

from ORM import Note
import DatabaseHandler as db

from fastapi import FastAPI

app = FastAPI()

db.CreateTable()
db_cols = [
    'note_id', 'title', 'date', 
    'text', 'username', 'color'
]

@app.get('/')
def Home():
    return "Service is Running..."

@app.get('/notes/{user_name}')
def Notes(user_name: str):
    notes = db.GetNotes(user_name)
    ret = [
        {x:y for (x,y) in zip(db_cols, row)}
        for row in notes
    ]
    return ret

@app.get('/note_id/{note_id}')
def GetNote(note_id: str):
    note = db.GetNoteByID(note_id)
    ret = {x:y for (x,y) in zip(db_cols, note)}
    return ret

@app.post('/add_note')
def AddNote(note: Note):
    note.note_id = str(uuid.uuid4())
    db.AddNote(note)
    return note

@app.get('/delete/{note_id}')
def DeleteNote(note_id: str):
    db.DeleteNote(note_id)
    return 'Deleted '+note_id

@app.post('/update_note')
def UpdateNote(note: Note):
    db.UpdateNote(note)
    return note
