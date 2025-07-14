import sqlite3
from database_setup import setup_database
from admin_functions import add_product, list_products, modify_product, view_sales_analysis
from user_functions import view_products, buy_product
from voice_command import voice_command, handle_voice_command

def setup_initial_admin():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    # Check if any admins exist
    cursor.execute('SELECT COUNT(*) FROM Users WHERE role = "admin"')
    if cursor.fetchone()[0] == 0:
        # Prompt to create admin
        print("No admin found. Please register the admin first.")
        username = input("Enter a new admin username: ")
        password = input("Enter a new admin password: ")
        try:
            cursor.execute('INSERT INTO Users (username, password, role) VALUES (?, ?, ?)', (username, password, 'admin'))
            conn.commit()
            print("Admin registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists. Please try a different username.")
    conn.close()

def get_user_role():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    print("Select role:")
    print("1. Admin")
    print("2. User")
    role_choice = input("Enter choice: ")
    role = None
    if role_choice == "1":
        role = 'admin'
    elif role_choice == "2":
        role = 'user'
    else:
        print("Invalid choice.")
        conn.close()
        return None

    print("1. Login")
    print("2. Register")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        cursor.execute('SELECT role FROM Users WHERE username = ? AND password = ?', (username, password))
        result = cursor.fetchone()
        conn.close()

        if result and result[0] == role:
            return result[0]  # returns 'admin' or 'user'
        else:
            print("Invalid username or password.")
            return None
    elif choice == "2":
        if role == 'admin':
            print("Admins are pre-registered. Please contact the system admin.")
            conn.close()
            return None

        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        mobile_no = input("Enter your mobile number: ")
        try:
            cursor.execute('INSERT INTO Users (username, password, role, mobile_no) VALUES (?, ?, ?, ?)', (username, password, role, mobile_no))
            conn.commit()
            print(f"User '{username}' registered successfully as {role}.")
        except sqlite3.IntegrityError:
            print("Username already exists. Please try a different username.")
        conn.close()
        return role
    else:
        print("Invalid choice.")
        conn.close()
        return None

def main():
    setup_database()
    setup_initial_admin()  # Ensure an admin is registered initially

    role = get_user_role()

    if role == "admin":
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. List Products")
            print("3. Modify Product")
            print("4. View Sales Analysis")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                product_id = int(input("Enter product ID: "))
                product_name = input("Enter product name: ")
                category = input("Enter category: ")
                cost = float(input("Enter cost: "))
                add_product(product_id, product_name, category, cost)
            elif choice == "2":
                products = list_products()
                for product in products:
                    print(product)
            elif choice == "3":
                product_id = int(input("Enter product ID to modify: "))
                new_name = input("Enter new name (leave blank to skip): ")
                new_category = input("Enter new category (leave blank to skip): ")
                new_cost = input("Enter new cost (leave blank to skip): ")
                modify_product(
                    product_id,
                    new_name if new_name else None,
                    new_category if new_category else None,
                    float(new_cost) if new_cost else None
                )
            elif choice == "4":
                analysis = view_sales_analysis()
                for category, count in analysis:
                    print(f"Category: {category}, Count: {count}")
            elif choice == "5":
                break
            else:
                print("Invalid choice")

    elif role == "user":
        while True:
            print("\nUser Menu:")
            print("1. List Products")
            print("2. Buy Product")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                products = view_products()
                for product in products:
                    print(product)
            elif choice == "2":
                product_id = int(input("Enter product ID to buy: "))
                buy_product(product_id)
            elif choice == "3":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()
