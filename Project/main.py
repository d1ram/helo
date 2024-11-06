import tkinter as tk 
from tkinter import ttk
from modules import block

def toggle_fullscreen(event = None) :
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)

def exit(event = None):
    root.quit()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Основные настройки проекта<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
root = tk.Tk()
root.title("College OC")
root.state("zoomed")
root.attributes('-fullscreen', True)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Бинды клавиш<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
root.bind('<F11>', toggle_fullscreen)
root.bind('<F12>', exit)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Настройка параметров колонок и строчек<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
block.make_row_column(root)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Основные функции<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Deleting frame (for pdf)
def delete_frame(frame_name): lambda: frame_name.destroy()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Верхний блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
up_frame = tk.Frame(bg='black')
up_frame.grid(column=1, row=1, columnspan=4, stick="wens")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Левый блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
left_side_frame = tk.Frame(bg='blue')
left_side_frame.grid(column=1, row=3, stick="wens")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Центральный блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
center_frame = tk.Frame(bg='red')
center_frame.grid(column=2, row=3, stick="wens")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Правый блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
right_side_frame = tk.Frame(bg='purple')
right_side_frame.grid(column=3, row=3, stick="wens")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Нижний блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
bottom_frame = tk.Frame(bg='black')
bottom_frame.grid(column=1, row=5, stick="wens", columnspan=4)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Конец программы<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
root.mainloop()
