import tkinter as tk
from time import strftime
import locale

# Устанавливаем локаль для русского языка
locale.setlocale(locale.LC_TIME, 'russian')

# Функция для обновления времени
def time():
    string = strftime('%H:%M:%S\n%A, %B %d, %Y')  # Формат времени и даты
    label.config(text=string)  # Обновляем текст на метке
    label.after(1000, time)  # Обновляем каждую секунду

# Создание основного окна
root = tk.Tk()
root.title("Часы и дата")

# Устанавливаем размер окна
root.geometry('300x300')

# Устанавливаем стиль окна (чтобы оно было квадратным)
root.resizable(False, False)

# Создание метки для отображения времени и даты
label = tk.Label(root, font=('calibri', 16, 'bold'), background='black', foreground='white', padx=20, pady=20)
label.pack(expand=True)

# Запуск функции для отображения времени
time()

# Запуск главного цикла
root.mainloop()