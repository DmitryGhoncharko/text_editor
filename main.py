


import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert("1.0", file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))


root = tk.Tk()
root.title("Текстовый редактор")


menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)


text = tk.Text(root)
text.pack(expand=True, fill="both")


root.mainloop()
