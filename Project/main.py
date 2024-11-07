import tkinter as tk 
from tkinter import ttk
from modules import settings
from modules.pdf import PDFview
from modules import timedd
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Основные настройки проекта<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def main() :
    root = tk.Tk()
    root.title("College OC")
    root.state("zoomed")
    root.attributes('-fullscreen', True)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PDF<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    pdf_view = PDFview()
    folder_path = 'C:\\Users\\User\\Desktop\\vanya\\PDF'
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
    central_frame = tk.Frame(bg = 'red')
    central_frame.grid(column=2, row=3, stick="wens")
    settings.central_frame(central_frame)
    pdf_view.load_pdfs(folder_path, central_frame)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Нижний блок<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    bottom_frame = tk.Frame(bg='black')
    bottom_frame.grid(column=1, row=5, stick="wens", columnspan=4)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Конец программы<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    root.mainloop()
if __name__ == "__main__":
    main()