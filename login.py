import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

def login():
    username = entry_user.get()
    password = entry_pass.get()   
    if username:
        root.withdraw()  
        python_executable = r"C:\Path\To\Python\python.exe"
        subprocess.Popen(["python", "main.py"])  # Open main.py
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Crepto User Login")
root.geometry("800x500")
root.configure(bg="#2C3E50")  # Dark background for contrast

# Load background image with PIL
bg_image_path = os.path.join("assets", "background.jpg")
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((800, 500))  
bg_image = ImageTk.PhotoImage(bg_image)

# Set background image using a label
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a stylish login frame
frame = tk.Frame(root, bg="white", padx=40, pady=30, relief="ridge", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(frame, text="Login", font=("Helvetica", 18, "bold"), bg="white", fg="#2C3E50")
title_label.pack(pady=10)

# Username field
tk.Label(frame, text="Username", font=("Helvetica", 12), bg="white").pack(anchor="w", pady=(10, 0))
entry_user = tk.Entry(frame, font=("Helvetica", 12), bg="#ECF0F1", fg="black", relief="flat", bd=5)
entry_user.pack(ipady=5, fill="x", padx=5)

# Password field
tk.Label(frame, text="Password", font=("Helvetica", 12), bg="white").pack(anchor="w", pady=(10, 0))
entry_pass = tk.Entry(frame, show="*", font=("Helvetica", 12), bg="#ECF0F1", fg="black", relief="flat", bd=5)
entry_pass.pack(ipady=5, fill="x", padx=5)

# Stylish Login Button
def on_hover(event):
    login_button.config(bg="#16A085")  # Darker shade on hover

def on_leave(event):
    login_button.config(bg="#1ABC9C")  # Original color

login_button = tk.Button(frame, text="Login", font=("Helvetica", 12, "bold"), bg="#1ABC9C", fg="white",
                         relief="flat", command=login, cursor="hand2")
login_button.pack(pady=15, ipadx=20, ipady=5, fill="x")

login_button.bind("<Enter>", on_hover)
login_button.bind("<Leave>", on_leave)

# Start the GUI main loop
root.mainloop()
