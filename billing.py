from database import connect_db

def generate_bill(item_name, price, quantity):
    total_price = price * quantity
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bills (item_name, price, quantity, total_price) VALUES (?, ?, ?, ?)", (item_name, price, quantity, total_price))

    conn.commit()
    conn.close()
    return total_price

import sqlite3

conn = sqlite3.connect("grocery_db.sqlite")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        total_price REAL NOT NULL
    )
""")

conn.commit()
conn.close()

print("Table 'bills' created successfully!")
