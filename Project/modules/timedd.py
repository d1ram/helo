import tkinter as tk
from time import strftime
import locale


# Устанавливаем локаль для русского языка
locale.setlocale(locale.LC_TIME, 'russian')
root = tk.Tk()
# Функция для обновления времени
def time(label):
    string = strftime('%H:%M:%S\n%A, %B %d, %Y')  # Формат времени и даты
    label.config(text=string)  # Обновляем текст на метке
    label.after(1000, time)  # Обновляем каждую секунду

# Создание основного окна
def start_clock():
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
    time(label)
    root.mainloop()

    # Запуск главного цикла
root.mainloop()