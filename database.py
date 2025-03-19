
import sqlite3

def connect_db():
    """Connect to SQLite database (creates file if it doesn’t exist)."""
    return sqlite3.connect("grocery_db.sqlite")

# Test connection
if __name__ == "__main__":
    conn = connect_db()
    print("Database connected successfully!")
    conn.close()


conn = sqlite3.connect("grocery_db.sqlite")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS grocery_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
""")

conn.commit()
conn.close()
print("Table created successfully!")
