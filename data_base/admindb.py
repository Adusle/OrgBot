import sqlite3

def create_admin_table():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY,
            user_id INTEGER UNIQUE,
            username TEXT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


def check_admin(user_id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM admins WHERE user_id = ?', (user_id,))
    users = cursor.fetchone()
    cursor.close()
    conn.close()
    return users

def add_admin(user_id, username):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO admins (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    cursor.close()
    conn.close()
