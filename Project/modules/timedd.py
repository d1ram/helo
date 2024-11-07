import tkinter as tk
from time import strftime
# Функция для обновления времени
def time(label):
    string = strftime('%H:%M:%S\n%A, %B %d, %Y')  # Формат времени и даты
    label.config(text=string)  # Обновляем текст на метке
    label.after(1000, time)  # Обновляем каждую секунду