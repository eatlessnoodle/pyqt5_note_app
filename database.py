import sqlite3
from PyQt5.QtCore import Qt, QDate

conn = sqlite3.connect('learning_records.db')
c = conn.cursor()

def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, note_type TEXT, note_name TEXT, content TEXT, content_en TEXT)''')
    conn.commit()

def insert_record(note_type, note_name, content, content_en):
    current_date = QDate.currentDate().toString(Qt.ISODate)
    c.execute("INSERT INTO records (date, note_type, note_name, content, content_en) VALUES (?, ?, ?, ?, ?)", (current_date, note_type, note_name, content, content_en))
    conn.commit()

def get_all_records():
    c.execute("SELECT id, date, note_type, note_name FROM records")
    return c.fetchall()

def get_record_by_id(record_id):
    c.execute("SELECT content, content_en FROM records WHERE id = ?", (record_id,))
    return c.fetchone()

def delete_record(record_id):
    c.execute("DELETE FROM records WHERE id = ?", (record_id,))
    conn.commit()
