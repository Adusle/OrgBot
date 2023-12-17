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
    cursor.execute('UPDATE event SET username = ? WHERE id = ?',(username, id,))
    conn.commit()
    cursor.close()
    conn.close()

def remove_performance(id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM event WHERE id = ?',(id,))
    conn.commit()
    cursor.close()
    conn.close()

def print_list():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, event_name, username FROM event')
    all_rows = cursor.fetchall()
    
    """
    while row is not None:
        print(" ".join([str(c) for c in row]))
        l = [str(c) for c in row]
        print(*l)
        row = cursor.fetchone()
        """
    cursor.close()
    conn.close()
    return all_rows