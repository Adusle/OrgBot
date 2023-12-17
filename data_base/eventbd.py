import sqlite3


def create_event_table():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS event (
                id INTEGER PRIMARY KEY,
                event_name TEXT,
                user_id TEXT,
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


def add_user_id(id, user_id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE event SET user_id = ? WHERE id = ?', (user_id, id,))
    conn.commit()
    cursor.close()
    conn.close()


def remove_performance(id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM event WHERE id = ?', (id,))
    conn.commit()
    cursor.close()
    conn.close()


def print_list():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, event_name, username FROM event')
    all_rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_rows

def add_username(user_id):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    s = ''
    for i in row:
        s = s+i
    print(s)
    cursor.execute('UPDATE event SET username = ? WHERE user_id = ?', (s, user_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_performance_username_id():
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()

    cursor.execute('SELECT username, user_id FROM event')
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

def replace(num1, num2):
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    names = ["event_name", "user_id", "username"]
    for i in names:
        s1 = ''
        s2 = ''
        cursor.execute(f'SELECT {i} FROM event WHERE id = ?', (num1,))
        row1 = cursor.fetchone()
        cursor.execute(f'SELECT {i} FROM event WHERE id = ?', (num2,))
        row2 = cursor.fetchone()
        for n in row1:
            s1 = s1+n
        for n in row2:
            s2 = s2+n
        cursor.execute(f'UPDATE event SET {i} = ? WHERE id = ?', (s2, num1,))
        cursor.execute(f'UPDATE event SET {i} = ? WHERE id = ?', (s1, num2,))
    conn.commit()
    cursor.close()
    conn.close()

