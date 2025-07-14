import sqlite3

def view_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ProductMaster')
    products = cursor.fetchall()
    conn.close()
    return products

def buy_product(product_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ProductMaster WHERE product_id = ?', (product_id,))
    product = cursor.fetchone()
    if product:
        category = product[2]
        cursor.execute('''
        INSERT INTO SalesTracker (product_id, category)
        VALUES (?, ?)
        ''', (product_id, category))
        conn.commit()
    else:
        print("No such product exists.")
    conn.close()

def get_top_trending_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT product_id, COUNT(*) as count 
    FROM SalesTracker 
    GROUP BY product_id 
    ORDER BY count DESC 
    LIMIT 3
    ''')
    top_products = cursor.fetchall()
    conn.close()
    return top_products
