import sqlite3
import os

ROOT = os.path.dirname(os.path.relpath(__file__))

def get_user(hash_id):
    conn = sqlite3.connect(os.path.join(ROOT, 'timesheet.db'))
    curr = conn.cursor()
    curr.execute('SELECT username FROM users WHERE id=?', (hash_id,))
    retrieved_user = curr.fetchall()
    return retrieved_user

def create_post(name, content):
    conn = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    curr = conn.cursor()
    curr.execute('INSERT INTO posts (name, content) values(?, ?)', (name, content))
    conn.commit()
    conn.close()

def get_posts():
    conn = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    curr = conn.cursor()
    curr.execute('SELECT * FROM posts')
    posts = curr.fetchall()
    return posts

def create_subject(id, owner, dateCreated, parent=None):
    conn = sqlite3.connect(os.path.join(ROOT, 'timesheet.db'))
    curr = conn.cursor()
    curr.execute(
        'INSERT INTO subjects (id, owner, parent, dateCreated) values(?, ?, ?, ?)', 
        (id, owner, parent, dateCreated))
    conn.commit()
    conn.close()

def create_session(id, owner, subject, dateCreated, startTime, endTime):
    conn = sqlite3.connect(os.path.join(ROOT, 'timesheet.db'))
    curr = conn.cursor()
    curr.execute(
        'INSERT INTO subjects (id, owner, subject, dateCreated, startTime, endTime) values(?, ?, ?, ?, ?, ?)', 
        (id, owner, subject, dateCreated, startTime, endTime))
    conn.commit()
    conn.close()

