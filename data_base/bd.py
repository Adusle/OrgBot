import sqlite3

def create_table():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_id INTEGER UNIQUE,
            username TEXT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


def add_user(user_id, username):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    cursor.close()
    conn.close()

def get_users_id(user_id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE user_id = ?', (user_id,))
    users = cursor.fetchone()
    cursor.close()
    conn.close()
    return users

def get_username_id(user_id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE user_id = ?', (user_id,))
    users = cursor.fetchone()
    cursor.close()
    conn.close()
    return users

