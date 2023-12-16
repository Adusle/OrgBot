import sqlite3

def create_event_table():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS event (
                id INTEGER PRIMARY KEY,
                event_name TEXT,
                username TEXT
            )
        ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_performance(event_name):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO event (event_name) VALUES (?)', (event_name,))
    conn.commit()
    cursor.close()
    conn.close()

def add_username(id, username):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO event (username) VALUES (?) WHERE id = ?', (id, username))
    conn.commit()
    cursor.close()
    conn.close()

"""id ev us
1 df df
2 asd asd
3 xcv xcv"""