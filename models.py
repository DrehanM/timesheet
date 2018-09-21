import sqlite3
import os
import re

ROOT = os.path.dirname(os.path.relpath(__file__))

def get_user(user_id):
    conn = sqlite3.connect(os.path.join(ROOT, 'timesheet.db'))
    curr = conn.cursor()
    curr.execute('SELECT * FROM users WHERE id=?', (user_id,))
    retrieved_user = curr.fetchall()
    return retrieved_user

def get_username(username):
    conn = sqlite3.connect(os.path.join(ROOT, 'timesheet.db'))
    curr = conn.cursor()
    curr.execute('SELECT username FROM users WHERE username=?', (username,))
    retrieved_username = curr.fetchall()
    return retrieved_username

#Must check for existing username
def register_user(user_id, username, dateCreated=0):
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return 1, "Invalid username."
    if get_username(username):
        return 1, "That username already exists."
    conn = sqlite3.connect(os.path.join(ROOT, 'timesheet.db'))
    curr = conn.cursor()
    curr.execute(
        'INSERT INTO users (id, username, dateCreated, numSessions) VALUES (?, ?, ?, ?)',
        (user_id, username, dateCreated, 0))
    conn.commit()
    conn.close()

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

