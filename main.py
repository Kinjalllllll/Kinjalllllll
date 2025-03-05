from tkinter import *
from tkinter import ttk, messagebox
from crud import add_item, update_item, delete_item, view_items
from billing import generate_bill
import mysql.connector
#from tkinter import Tk, Label

def refresh_items():
    for row in tree.get_children():
        tree.delete(row)
    for item in view_items():
        tree.insert("", "end", values=item)
        
    
root = Tk()
root.geometry("800x500")
heading = Label(root, text="CREPTO", font=("Arial", 20, "bold"))
heading.grid(row=0, column=0, pady=20, columnspan=4)  # Add some space


heading = Label(root, text="Welcome to My CREPTO", font=("Arial", 20, "bold"))
heading.grid(row=0, column=0, pady=20, columnspan=4)  # Add some space


def add_item_ui():
    name, price, quantity = entry_name.get(), entry_price.get(), entry_quantity.get()
   
    #add_item(name, price, quantity)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Change to your MySQL username
        password="",  # Change to your MySQL password
        database="1grocery_db"
    )
    print("Connection Created!")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO `1grocery_items`(`id`, `name`, `price`, `quantity`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]'")
    conn.commit()
    print("Query Committed!")

    root.update()
    if cursor.rowcount > 0:
        print("Record Inserted!")
    else:
        print("Record Cannot Be Inserted!")
    #conn.close()
    refresh_items()



def delete_item_ui():
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item, "values")[0]
        delete_item(item_id)
        refresh_items()

    else:
        messagebox.showerror("Error", "Select an item to delete")

def bill_ui():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item, "values")
        item_name, price, quantity = item[1], float(item[2]), int(item[3])
        total_price = generate_bill(item_name, price, quantity)
        messagebox.showinfo("Bill", f"Total Price: ${total_price}")
    else:
        messagebox.showerror("Error", "Select an item for billing")

# Input Fields
Label(root, text="Name").grid(row=1, column=0)
entry_name = Entry(root)
entry_name.grid(row=1, column=1)

Label(root, text="Price").grid(row=2, column=0)
entry_price = Entry(root)
entry_price.grid(row=2, column=1)

Label(root, text="Quantity").grid(row=3, column=0)
entry_quantity = Entry(root)
entry_quantity.grid(row=3, column=1)

Button(root, text="Add Item", command=add_item_ui).grid(row=4, column=1)
Button(root, text="Delete Item", command=delete_item_ui).grid(row=4, column=2)
Button(root, text="Generate Bill", command=bill_ui).grid(row=4, column=3)

# Grocery Items Table
columns = ("ID", "Name", "Price", "Quantity")
#columns = ("ID", "Name", "Price", "Quantity")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=4)


root.mainloop()

refresh_items()

# root.mainloop()