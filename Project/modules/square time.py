import tkinter as tk
from datetime import datetime
import locale

# Устанавливаем локаль для русского языка
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

class SquareApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Square Example")
        self.master.state("zoomed")
        
        self.update_time()  # Начинаем обновление времени

        # self.create_rectangle(100, 300, 720, 920)
        # self.create_rectangle(100, 300, 620, 820)

    def update_time(self):
        # Получаем текущее время
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Обновляем текст внутри квадрата
        self.canvas.itemconfig(self.text_id, text=f"Время: {current_time}")
        
        # Запланировать следующее обновление через 1 секунду
        self.master.after(1000, self.update_time)
    def create_rectangle(self, x1, x2, y1, y2):
        self.canvas = tk.Canvas(self.master, width=1920, height=1080, bg="white")
        self.canvas.pack()
        
        # Задаем координаты для размещения квадрата
        self.x1, self.y1 = x1, y1  # Верхний левый угол
        self.x2, self.y2 = x2, y2  # Нижний правый угол
        
        # Создаем квадрат
        self.rectangle = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="Beige")

        # Создаем текст внутри квадрата
        self.text_id = self.canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, fill="white", font=("Arial", 16))

if __name__ == "__main__":
    root = tk.Tk()
    app = SquareApp(root)
    root.mainloop()
