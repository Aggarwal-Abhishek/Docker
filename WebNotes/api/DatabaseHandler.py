import os, time
import psycopg2

def GetNotes(username):
    qry = f'''SELECT * from notes WHERE username='{username}';'''
    cursor.execute(qry)
    return cursor.fetchall()

def GetNoteByID(note_id):
    qry = f'''SELECT * from notes WHERE note_id='{note_id}';'''
    cursor.execute(qry)
    return cursor.fetchone()

def AddNote(note):
    qry = f'''\
    INSERT INTO notes(note_id, title, date, text, username, color)
    VALUES(%s, %s, %s, %s, %s, %s);'''

    values = (note.note_id, note.title, note.date, 
        note.text, note.username, note.color)
    
    cursor.execute(qry, values)
    conn.commit()    

def DeleteNote(note_id):
    qry = f'''DELETE FROM notes WHERE note_id='{note_id}';'''
    cursor.execute(qry)
    conn.commit()

def UpdateNote(note):
    DeleteNote(note.note_id)
    AddNote(note)

def CreateTable():
    cursor.execute(''' CREATE TABLE IF NOT EXISTS notes(
        note_id varchar(64) NOT NULL PRIMARY KEY,
        title varchar(128) NOT NULL,
        date varchar(64) NOT NULL,
        text varchar(1024) NOT NULL,
        username varchar(128) NOT NULL,
        color varchar(8) NOT NULL
    ); ''')
    
    conn.commit()

while True:
    try:
        conn = psycopg2.connect(
            host = os.environ['DB_HOST'],
            database = os.environ['DB_NAME'],
            user = os.environ['DB_USERNAME'],
            password = os.environ['DB_PASSWORD']
        )
        cursor = conn.cursor()
        print("Database Connected Successifully :-)")
        break
        
    except Exception as error:
        print("Connecting to database failed...Trying Again...")
        print("Error:", error)
        time.sleep(2)
        
