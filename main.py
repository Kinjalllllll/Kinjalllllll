
import tkinter as tk
from tkinter import ttk, messagebox
from crud import add_item, update_item, delete_item, view_items
from billing import generate_bill

# Create the main window
root = tk.Tk()
root.title("Crepto Grocery Store")
root.geometry("900x550")
root.configure(bg="#34495E")  # Dark background for contrast

# Create button frame
btn_frame = tk.Frame(root, bg="#34495E")
btn_frame.pack(pady=10)

# Button hover effects
def on_hover(event, btn):
    btn.config(bg="#1ABC9C")

def on_leave(event, btn):
    btn.config(bg="#16A085")  # Reset button color when mouse leaves

# Add alternate row colors for better visibility
style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 11))
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.map("Treeview", background=[("selected", "#1ABC9C")])
style.configure("Treeview", rowheight=25)

# Stylish frame for inputs
input_frame = tk.Frame(root, bg="#ECF0F1", padx=20, pady=20, relief="ridge", bd=3)
input_frame.pack(pady=15, padx=20, fill="x")

# Entry Fields with Labels
tk.Label(input_frame, text="Name", font=("Helvetica", 12), bg="#ECF0F1").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Price", font=("Helvetica", 12), bg="#ECF0F1").grid(row=1, column=0, padx=10, pady=5)
entry_price = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_price.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Quantity", font=("Helvetica", 12), bg="#ECF0F1").grid(row=2, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_quantity.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="ID", font=("Helvetica", 12), bg="#ECF0F1").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_id.grid(row=0, column=1, padx=10, pady=5)


# Function to move focus to the next entry
def move_focus(event, next_widget):
    next_widget.focus_set()

# Entry Fields with Labels
tk.Label(input_frame, text="Name", font=("Helvetica", 12), bg="#ECF0F1").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Price", font=("Helvetica", 12), bg="#ECF0F1").grid(row=1, column=0, padx=10, pady=5)
entry_price = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_price.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Quantity", font=("Helvetica", 12), bg="#ECF0F1").grid(row=2, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(input_frame, font=("Helvetica", 12), bg="white", relief="flat", bd=5)
entry_quantity.grid(row=2, column=1, padx=10, pady=5)

# Bind Enter key to move between fields
entry_name.bind("<Return>", lambda event: move_focus(event, entry_price))
entry_price.bind("<Return>", lambda event: move_focus(event, entry_quantity))
entry_quantity.bind("<Return>", lambda event: move_focus(event, entry_id))



# Create button frame
btn_frame = tk.Frame(root, bg="#34495E")
btn_frame.pack(pady=10)

# Create button frame
btn_frame = tk.Frame(root, bg="#34495E")
btn_frame.pack(pady=10)

# Table for Displaying Items
table_frame = tk.Frame(root, bg="#ECF0F1", relief="ridge", bd=3)
table_frame.pack(pady=10, padx=20, fill="both", expand=True)

columns = ("ID", "Name", "Price", "Quantity")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
tree.pack(fill="both", expand=True)

# Define column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

# Function to refresh items in the table
def refresh_items():
    for row in tree.get_children():
        tree.delete(row)
    for item in view_items():
        tree.insert("", "end", values=item)

# Function to add an item
from tkinter import messagebox

def add_item_ui():
    try:
        name = entry_name.get().strip()  
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
        if name and price > 0 and quantity >0:
             add_item(name, price, quantity)
             refresh_items()
        else:
            messagebox.showerror("Error", "Please enter valid item details")
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity")


# Function to delete an item
def delete_item_ui():
    selected = tree.selection()
    if selected:
        for item in selected:
            item_id = tree.item(item, "values")[0]
            delete_item(item_id)
        refresh_items()
    else:
        messagebox.showerror("Error", "Select an item to delete")
def update_item_ui():
    try:
        name = entry_name.get()
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
        if name and price > 0 and quantity > 0:
            update_item(name, price, quantity)
            refresh_items()
        else:
            messagebox.showerror("Error", "Please enter valid item details")
    except ValueError:
        messagebox.showerror("Error", "Invalid price or quantity")

def bill_ui():
    selected_items = tree.selection()  # Get all selected items in the treeview
    
    if not selected_items:
        messagebox.showerror("Error", "Select at least one item to generate a bill")
        return

    # Loop through all selected items and generate bills
    for item in selected_items:
        item_values = tree.item(item, "values")
        name = item_values[1]  # Item Name
        price = float(item_values[2])  # Item Price
        quantity = int(item_values[3])  # Item Quantity
        total_price = generate_bill(name, price, quantity)  # Call the billing logic

        # Create a bill pop-up for each selected item
        bill_window = tk.Toplevel(root)
        bill_window.title("Bill Receipt")
        bill_window.geometry("350x250")
        bill_window.configure(bg="#ECF0F1")

        tk.Label(bill_window, text="Crepto Grocery Store", font=("Helvetica", 14, "bold"), bg="#ECF0F1", fg="#2C3E50").pack(pady=10)
        tk.Label(bill_window, text=f"Item: {name}", font=("Helvetica", 12), bg="#ECF0F1").pack(pady=5)
        tk.Label(bill_window, text=f"Price: Rs{price:.2f}", font=("Helvetica", 12), bg="#ECF0F1").pack(pady=5)
        tk.Label(bill_window, text=f"Quantity: {quantity}", font=("Helvetica", 12), bg="#ECF0F1").pack(pady=5)
        tk.Label(bill_window, text=f"Total: Rs{total_price:.2f}", font=("Helvetica", 14, "bold"), fg="#E74C3C", bg="#ECF0F1").pack(pady=10)
        

        # Close button for each bill window
        close_btn = tk.Button(bill_window, text="Close", font=("Helvetica", 12, "bold"), bg="#1ABC9C", fg="white",
                              relief="flat", padx=20, pady=5, command=bill_window.destroy)
        close_btn.pack(pady=10)



# Button hover effects
def on_hover(event, btn):
    btn.config(bg="#1ABC9C")

def on_leave(event, btn):
    btn.config(bg="#16A085")



# Create Buttons Before mainloop()
buttons = [
    ("Add Item", add_item_ui),
    ("Delete Item", delete_item_ui),
    ("Generate Bill", bill_ui),
    ("Update Item", update_item_ui)
]
#  `buttons` in the loop (AFTER defining it)
for i, (text, command) in enumerate(buttons):
    btn = tk.Button(btn_frame, text=text, font=("Helvetica", 12, "bold"), bg="#16A085", fg="white",
                    relief="flat", command=command, padx=20, pady=5, width=15, cursor="hand2")
    btn.grid(row=0, column=i, padx=10)
    btn.bind("<Leave>", lambda event, b=btn: on_leave(event, b))


#btn_update = tk.Button(btn_frame, text="Update Item", font=("Helvetica", 12), bg="#1ABC9C", fg="white", 
                       #padx=10, pady=5, relief="flat", command=update_item_ui)
#btn_update.grid(row=0, column=2, padx=10)


# Load items initially
refresh_items()

# Start the main event loop
root.mainloop()



