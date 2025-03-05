import tkinter as tk
from tkinter import messagebox
from database import connect_db

def login():
    username = entry_user.get()
    password = entry_pass.get()
   #  from customtkinter import*from PIL import image

   # imgtemp = CTkImage(light_image = Image.open("C:\kinjal\grocerystore"),size=(root.winfo_screenwidth(),root.winfo_screenheight()))
   # imgLabel = CTkLabel(root,image-imgtemp,text="Green Yellow Dynamic Photocentric Grocery Poster.jpg")
    #imgLabel.place(relx=0.5,rely=0.5,anchor="center")
    #image background
   

    from tkinter import Tk, Label, PhotoImage

    root = Tk()
    root.geometry("800x600") 

    bg_image = PhotoImage(file="Green Yellow Dynamic Photocentric Grocery Poster.jpg")
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    root.mainloop()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `user` WHERE username=admin AND password=admin", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        root.destroy()  # Close login window
        import main  # Open main window
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Create Tkinter Window
root = tk.Tk()
root.title("Crepto user Login")
root.geometry("800x500")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack()
root.mainloop()


