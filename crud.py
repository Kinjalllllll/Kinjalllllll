from database import connect_db
import mysql.connector

def add_item(name, price, quantity):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Change to your MySQL username
        password="",  # Change to your MySQL password
        database="1grocery_db"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO `1grocery_items`(`id`, `name`, `price`, `quantity`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]'")
    conn.commit()
    #conn.close()

def update_item(item_id, name, price, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE `1grocery_items` SET `id`='[value-1]',`name`='[value-2]',`price`='[value-3]',`quantity`='[value-4]' WHERE 1")
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `1grocery_items` WHERE 0 id=%s", (item_id,))
    conn.commit()
    conn.close()

def view_items():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `1grocery_items` WHERE 1")
    items = cursor.fetchall()
    conn.close()
    return items
