import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change to your MySQL username
        password="",  # Change to your MySQL password
        database="1grocery_db"
    )

