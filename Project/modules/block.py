import tkinter as tk 
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
    root.grid_columnconfigure(2, minsize=580)
    root.grid_columnconfigure(3, minsize=600)
    root.grid_columnconfigure(4, minsize=200)
    root.grid_columnconfigure(5, minsize=20)