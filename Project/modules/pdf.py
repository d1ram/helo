import os
import tkinter as tk
from tkinter import messagebox

class PDFview:
    def __init__(self):
        self.frames = []        # Список для хранения созданных фреймов
        self.pdf_files = []     # Список для хранения путей к PDF файлам
        self.current_pdf = None # Текущий PDF файл

    def load_pdfs(self, folder_path):
        """Загружает PDF файлы из указанной папки"""
        if os.path.exists(folder_path):
            self.pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
            messagebox.showinfo("Info", f"Loaded {len(self.pdf_files)} PDF files.")
        else:
            messagebox.showinfo("Info", "No folder with that name")

    def make_solid_frame(self, csf, rsf):
        """
        Создаёт единый фрейм, если существуют фреймы csf (center side frame) и rsf (right side frame),
        иначе выводит сообщение об ошибке
        """
        crsf = None
        if csf and rsf:
            csf.destroy()
            rsf.destroy()

            crsf = tk.Frame(bg='red') # Создаем новый фрейм
            self.frames.clear()       # Очищаем текущие фреймы
            self.frames.append(crsf)  # Добавляем новый фрейм в список
            return crsf
        else:
            messagebox.showinfo("Info", "Sorry, but already have one frame")

    def create_two_frames(self, crsf):
        """
        Создаёт два фрейма (csf и rsf), если сейчас нет фреймов или есть только один.
        """
        
        if len(self.frames) == 1:
            self.frames.clear()   # Очищаем текущие фреймы
            crsf.destroy()        # Удаляем текущий центральный фрейм

            csf = tk.Frame(bg='red')   # Создаем новый центральный фрейм
            rsf = tk.Frame(bg='purple') # Создаем новый правый фрейм
            self.frames.extend([csf, rsf])  # Добавляем оба фрейма в список

            return self.frames

        elif len(self.frames) == 0:
            csf = tk.Frame(bg='red')
            rsf = tk.Frame(bg='purple')
            self.frames.extend([csf, rsf])

            return self.frames
        else:
            messagebox.showinfo("Info", "Sorry, already have two frames")
