import tkinter as tk 
from tkinter import ttk
from modules import settings
from modules.pdf import PDFview
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Основные настройки проекта<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
root = tk.Tk()
root.title("College OC")
root.state("zoomed")
root.attributes('-fullscreen', True)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PDF<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
pdf_view = PDFview()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Бинды клавиш<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
root.bind('<F11>', lambda event: settings.toggle_fullscreen(root, event))
root.bind('<F12>', lambda event: settings.exit(root, event))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Настройка параметров колонок и строчек<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
settings.make_row_column(root)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Верхний блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
up_frame = tk.Frame(bg='black')
up_frame.grid(column=1, row=1, columnspan=4, stick="wens")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Левый блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
left_side_frame = tk.Frame(bg='blue')
left_side_frame.grid(column=1, row=3, stick="wens")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Центральный блок и Правый блок <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
frames = pdf_view.create_two_frames(None)

central_frame = frames[0]
central_frame.grid(column=2, row=3, stick="wens")

right_side_frame = frames[1]
right_side_frame.grid(column=3, row=3, stick="wens")

central_frame = pdf_view.make_solid_frame(central_frame, right_side_frame)
central_frame.grid(column=2, row=3, columnspan=2 , stick="wens")

# frames = pdf_view.create_two_frames(central_frame)

# central_frame = frames[0]
# central_frame.grid(column=2, row=3, stick="wens")

# right_side_frame = frames[1]
# right_side_frame.grid(column=3, row=3, stick="wens")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Нижний блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
bottom_frame = tk.Frame(bg='black')
bottom_frame.grid(column=1, row=5, stick="wens", columnspan=4)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Конец программы<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
root.mainloop()













# central_right_side_frame = None
# frames = pdf.create_two_frames(central_right_side_frame)

# central_frame = frames[0]
# central_frame.grid(column=2, row=3, stick="wens")

# right_side_frame = frames[1]
# right_side_frame.grid(column=3, row=3, stick="wens")

# central_right_side_frame = pdf.make_solid_frame(central_frame, right_side_frame)
# central_right_side_frame.grid(column=2, row=3, columnspan=2 , stick="wens") 
