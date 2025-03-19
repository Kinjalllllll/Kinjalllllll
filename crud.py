from database import connect_db
import sqlite3
def add_item(name, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grocery_items (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))

    conn.commit()
    conn.close()


def update_item(item_id, name, price, quantity):
    """Update an existing item in the grocery_items table."""
    conn = sqlite3.connect("grocery_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE grocery_items 
        SET name = ?, price = ?, quantity = ? 
        WHERE id = ?
    """, (name, price, quantity, item_id))

    conn.commit()
    conn.close()

    print(f"Item {item_id} updated successfully!")



def delete_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM grocery_items WHERE id = ?", (item_id,))

    conn.commit()
    conn.close()

def view_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `grocery_items`")
    items = cursor.fetchall()
    conn.close()
    return items


