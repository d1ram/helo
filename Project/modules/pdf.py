import os
import tkinter as tk
from tkinter import messagebox
import fitz
from PIL import Image, ImageTk

class PDFview:
    def __init__(self):
        self.frames = []        # Список для хранения созданных фреймов
        self.pdf_files = []     # Список для хранения путей к PDF файлам
        self.current_pdf = None # Текущий PDF файл
        self.cf = None          # Frame для размещения элементов
        self.canvas = None
        self.buttons = []       # Список кнопок для отображения PDF
        self.current_page = 0   # Индекс текущей страницы
        self.buttons_per_page = 4  # Количество кнопок на одной странице
        self.scrollbar = None

    def load_pdfs(self, folder_path, cf_frame):
        self.cf = cf_frame
        if os.path.exists(folder_path):
            self.pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
            messagebox.showinfo("Info", f"Loaded {len(self.pdf_files)} PDF files.")
            self.show_page(self.current_page)
        else:
            messagebox.showinfo("Info", "No folder with that name")

    def create_canvas(self, frame):
        self.canvas = tk.Canvas(frame, bg="red")
        self.canvas.grid(row=0, column=1, columnspan=3, sticky="nsew")  

        self.scrollbar = tk.Scrollbar(frame, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=4, sticky="ns") 

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def open_pdf(self, index):
        for button in self.buttons:
            button.destroy() 
        self.buttons = []  

        self.create_canvas(self.cf)

        self.current_pdf = fitz.open(self.pdf_files[index])
        self.show_all_pages() 

        back_button = tk.Button(self.cf, text="Back to Files", command=self.back_to_files)
        back_button.grid(row=0, column=0, sticky="w")
        self.buttons.append(back_button) 

    def show_all_pages(self):
        if self.current_pdf:
            self.canvas.delete("all")
            total_height = 0  
            images = []
            try:
                for page_number in range(len(self.current_pdf)):
                    page = self.current_pdf[page_number]
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    images.append(img)
                    total_height += img.height

                final_image = Image.new("RGB", (images[0].width, total_height))
                y_offset = 0
                for img in images:
                    final_image.paste(img, (0, y_offset))
                    y_offset += img.height

                img_tk = ImageTk.PhotoImage(final_image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
                self.canvas.image = img_tk 

                self.canvas.config(scrollregion=self.canvas.bbox("all"))
            except Exception as e:
                messagebox.showerror("Error", "Failed to display the PDF pages.")

    def show_page(self, page):
        # Удаляем все старые кнопки перед созданием новых
        for button in self.buttons:
            button.destroy()
        self.buttons = []

        
        # Определяем начальный и конечный индексы для кнопок на текущей странице
        start = page * self.buttons_per_page
        end = min(start + self.buttons_per_page, len(self.pdf_files))

        # Создаем кнопки для текущей страницы
        for i in range(start, end):
            pdf = self.pdf_files[i]
            button = tk.Button(self.cf, text=f"Open {os.path.basename(pdf)}",
                               command=lambda idx=i: self.open_pdf(idx),
                               width=20, height=7)
            button.grid(row=2, column=i - start)
            self.buttons.append(button)

        # Кнопки "Назад" и "Вперед" для переключения страниц
        if page > 0:
            prev_button = tk.Button(self.cf, text="Назад", command=self.prev_page)
            prev_button.grid(row=3, column=0, sticky="w")
            self.buttons.append(prev_button)

        if end < len(self.pdf_files):
            next_button = tk.Button(self.cf, text="Вперед", command=self.next_page)
            next_button.grid(row=3, column=3, sticky="e")
            self.buttons.append(next_button)

    def next_page(self):
        # Переход на следующую страницу, если есть больше кнопок
        if (self.current_page + 1) * self.buttons_per_page < len(self.pdf_files):
            self.current_page += 1
            self.show_page(self.current_page)

    def prev_page(self):
        # Переход на предыдущую страницу, если она существует
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)

    def back_to_files(self):
        self.canvas.destroy()
        self.scrol
        self.canvas = None

        self.scrollbar.destroy()
        self.scrollbar = None
        self.show_page(self.cf)