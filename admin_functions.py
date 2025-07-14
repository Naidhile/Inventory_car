import sqlite3

def add_product(product_id, product_name, category, cost):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ProductMaster (product_id, product_name, category, cost)
    VALUES (?, ?, ?, ?)
    ''', (product_id, product_name, category, cost))
    conn.commit()
    conn.close()

def list_products():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ProductMaster')
    products = cursor.fetchall()
    conn.close()
    return products

def modify_product(product_id, new_name=None, new_category=None, new_cost=None):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    if new_name:
        cursor.execute('UPDATE ProductMaster SET product_name = ? WHERE product_id = ?', (new_name, product_id))
    if new_category:
        cursor.execute('UPDATE ProductMaster SET category = ? WHERE product_id = ?', (new_category, product_id))
    if new_cost:
        cursor.execute('UPDATE ProductMaster SET cost = ? WHERE product_id = ?', (new_cost, product_id))
    conn.commit()
    conn.close()

def view_sales_analysis():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, COUNT(*) as count FROM SalesTracker GROUP BY category')
    analysis = cursor.fetchall()
    conn.close()
    return analysis
