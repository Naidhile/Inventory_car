import sqlite3

def create_user(username, password, role):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Users (username, password, role)
    VALUES (?, ?, ?)
    ''', (username, password, role))

    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT role FROM Users WHERE username = ? AND password = ?
    ''', (username, password))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]  # Return the role of the user (either 'admin' or 'user')
    else:
        return None  # Invalid credentials
