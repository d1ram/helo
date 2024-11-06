# helo
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()

# Set window size and title
root.geometry('420x180+820+450')
root.title("Sims Open")

# Load the background image
background_image = Image.open("C:\\Users\\bro\\Pictures\\sims.jpg")  # Update with your image path
background_image = background_image.resize((420, 180))  # Resize if necessary
bg_image = ImageTk.PhotoImage(background_image)

# Create a Label to hold the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)  # Make it cover the entire window

def open(dest):
    if dest == 1:
        os.startfile("A:\\The Sims 4\\Launcher.exe")
        root.destroy()
    elif dest == 2:
        os.startfile('C:\\Users\\bro\\Documents\\Electronic Arts\\The Sims 4\\Mods')
    elif dest == 3:
        os.startfile("A:\\The Sims 4")
    elif dest == 4:
        root.destroy()

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton',
                background='#43C6DB',
                foreground='#033E3E',
                font=('Helvetica', 12))

style.map('TButton',
          background=[('active', '#CFECEC')],
          foreground=[('pressed', '#B3D9D9')],
          relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

# Create the label without a background color
label = tk.Label(root, text="Sims 4",  fg='black', font=('Helvetica', 16))
label.grid(column=1, row=0, stick="wens")

ttk.Button(text="Open Sims4",
           command=lambda: open(1)).grid(column=0, row=1, padx=5, pady=5, stick="wens")
ttk.Button(text="Open Mods folder",
           command=lambda: open(2)).grid(column=1, row=1, padx=5, pady=5, stick="wens")
ttk.Button(text="Open Root folder",
           command=lambda: open(3)).grid(column=2, row=1, padx=5, pady=5, stick="wens")
ttk.Button(text="Exit",
           command=lambda: open(4)).grid(column=1, row=2, padx=5, pady=5, stick="wens")

root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)

root.mainloop()
