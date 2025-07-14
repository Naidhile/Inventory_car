import sqlite3

def update_database_schema():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    # Add the mobile_no column to the Users table
    cursor.execute('ALTER TABLE Users ADD COLUMN mobile_no TEXT')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_database_schema()
