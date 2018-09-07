import sqlite3
import os

ROOT = os.path.dirname(os.path.relpath(__file__))

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