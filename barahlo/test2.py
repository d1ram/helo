import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bg="blue")
frame.pack()

# Функция для удаления фрейма
def delete_frame():
    frame.destroy()

button = tk.Button(root, text="Удалить фрейм", command=delete_frame)
button.pack()

root.mainloop()