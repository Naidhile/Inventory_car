import sqlite3

def setup_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create ProductMaster table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProductMaster (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        category TEXT,
        cost REAL
    )
    ''')

    # Create SalesTracker table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SalesTracker (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        category TEXT,
        sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES ProductMaster (product_id)
    )
    ''')

    # Create Users table with mobile_no
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT CHECK(role IN ('admin', 'user')),
        mobile_no TEXT
    )
    ''')

    # Example users
    cursor.execute('INSERT OR IGNORE INTO Users (username, password, role, mobile_no) VALUES (?, ?, ?, ?)', ('admin', 'adminpass', 'admin', '1234567890'))
    cursor.execute('INSERT OR IGNORE INTO Users (username, password, role, mobile_no) VALUES (?, ?, ?, ?)', ('user1', 'userpass', 'user', '0987654321'))

    conn.commit()
    conn.close()
