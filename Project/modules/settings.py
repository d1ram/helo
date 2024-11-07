import tkinter as tk

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Бинды<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def toggle_fullscreen(root ,event = None) :
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)

def exit(root ,event = None):
    root.quit()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Rows n Columns<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def make_row_column(root) :
    #rows
    root.grid_rowconfigure(0, minsize=20)
    root.grid_rowconfigure(1, minsize=80)
    root.grid_rowconfigure(2, minsize=20)
    root.grid_rowconfigure(3, minsize=760)
    root.grid_rowconfigure(4, minsize=20)
    root.grid_rowconfigure(5, minsize=160)
    root.grid_rowconfigure(6, minsize=20)
    #columns
    root.grid_columnconfigure(0, minsize=20)
    root.grid_columnconfigure(1, minsize=500)
    root.grid_columnconfigure(2, minsize=1150)
    root.grid_columnconfigure(3, minsize=200)
    root.grid_columnconfigure(4, minsize=20)
    #central_frame

def central_frame(central_frame):
    #row
    central_frame.grid_rowconfigure(0, weight=1, minsize = 152)
    central_frame.grid_rowconfigure(1, weight=1, minsize = 152)
    central_frame.grid_rowconfigure(2, weight=1, minsize = 152)
    central_frame.grid_rowconfigure(3, weight=1, minsize = 152)
    central_frame.grid_rowconfigure(4, weight=1, minsize = 152)
    central_frame.grid_rowconfigure(4, weight=1, minsize = 152)
    #column
    central_frame.grid_columnconfigure(0, weight=1, minsize=191)
    central_frame.grid_columnconfigure(1, weight=1, minsize=255)
    central_frame.grid_columnconfigure(2, weight=1, minsize=256)
    central_frame.grid_columnconfigure(3, weight=1, minsize=255)
    central_frame.grid_columnconfigure(4, weight=1, minsize=191)