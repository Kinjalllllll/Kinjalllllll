from database import connect_db

def generate_bill(item_name, price, quantity):
    total_price = price * quantity
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bills (item_name, price, quantity, total_price) VALUES (%s, %s, %s, %s)",
                   (item_name, price, quantity, total_price))
    conn.commit()
    conn.close()
    return total_price
