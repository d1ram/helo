import tkinter as tk
from tkinter import messagebox
import fitz  # PyMuPDF
from PIL import Image, ImageTk
import os
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> В DEF LOAD_PDFS В FOLDER_PATH СОЗДАЙ ЛЮБУЮ ПАПКУ И ЗАКАЧАЙ ТУДА ПДФОК, ИНАЧЕ У ТЕБЯ ОНИ НЕ ЗАГРУЗЯТСЯ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class PDFViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Viewer")
        self.master.state("zoomed")

        self.pdf_files = []  # Список для хранения загруженных PDF-файлов
        self.current_pdf = None  # Выбранный PDF-файл
        self.canvas = None  # Инициализация атрибута для канваса

        self.load_pdfs()  # Загружаем PDF-файлы
        self.create_pdf_buttons()  # Создаем кнопки для PDF-файлов

        self.back_button = tk.Button(master, text="Go back", command=self.go_back)
        self.back_button.pack(side="bottom")

        # Создаем область для отображения PDF
        self.pdf_area = tk.Frame(master, width=1000, height=500)  # Задаем фиксированные размеры области
        self.pdf_area.pack(fill=tk.BOTH, expand=True)


    def load_pdfs(self):
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>СЮДА<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        folder_path = r"C:\Users\User\Desktop\vanya\PDF"  # Укажите свой путь
        if os.path.exists(folder_path):
            self.pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
            messagebox.showinfo("Info", f"Loaded {len(self.pdf_files)} PDF files.")
        else:
            messagebox.showwarning("Warning", "Folder does not exist.")

    def create_canvas(self):
        self.canvas = tk.Canvas(self.pdf_area, bg="white")  # Создаем канвас внутри pdf_area
        self.canvas.pack(fill=tk.BOTH, expand=True,)

        scrollbar = tk.Scrollbar(self.pdf_area, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=scrollbar.set)
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)  # Привязываем прокрутку колесом

    def create_pdf_buttons(self):
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.buttons = []  # Список для хранения кнопок
        for index, pdf in enumerate(self.pdf_files):
            button = tk.Button(self.button_frame, text=f"Open {os.path.basename(pdf)}",
                               command=lambda idx=index: self.open_pdf(idx),
                               width=20, height=7)
            button.pack(side=tk.LEFT, padx=5, pady=5)
            self.buttons.append(button)

    def open_pdf(self, index):
        self.create_canvas()  # Создаем канвас при открытии PDF
        for button in self.buttons:
            button.pack_forget()  # Убираем кнопки с экрана

        self.current_pdf = fitz.open(self.pdf_files[index])
        self.show_all_pages()

    def show_all_pages(self):
        if self.current_pdf:
            self.canvas.delete("all")  # Очищаем холст
            total_height = 0  # Общая высота для создания одного длинного изображения
            images = []

            try:
                for page_number in range(len(self.current_pdf)):
                    page = self.current_pdf[page_number]
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    images.append(img)
                    total_height += img.height

                # Создаем одно длинное изображение
                final_image = Image.new("RGB", (images[0].width, total_height))
                y_offset = 0
                for img in images:
                    final_image.paste(img, (0, y_offset))
                    y_offset += img.height

                img_tk = ImageTk.PhotoImage(final_image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
                self.canvas.image = img_tk  # Сохраняем ссылку на изображение

                # Устанавливаем область прокрутки
                self.canvas.config(scrollregion=self.canvas.bbox("all"))
            except Exception as e:
                messagebox.showerror("Error", "Failed to display the PDF pages.")

    def on_mouse_wheel(self, event):
        # Прокручиваем канвас
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def go_back(self):
        if self.canvas:
            self.canvas.pack_forget()  # Удаляем канвас
            self.canvas = None  # Освобождаем ссылку на канвас

        # Показываем кнопки выбора файлов снова
        for button in self.buttons:
            button.pack(side=tk.LEFT, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    viewer = PDFViewer(root)
    root.mainloop()
