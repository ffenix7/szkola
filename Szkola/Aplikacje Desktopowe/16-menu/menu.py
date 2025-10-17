import tkinter as tk
from tkinter import ttk, messagebox

def new_file():
    messagebox.showinfo("Info", "Tworzenie nowego pliku")

def save_file():
    messagebox.showinfo("Info", "Zapisywanie pliku")

def open_file():
    messagebox.showinfo("Info", "Otwieranie pliku")

def about():
    messagebox.showinfo("O programie", "To jest przykładowa aplikacja z menu.")



root = tk.Tk()
root.title("Menu Example")
root.geometry("300x200")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label="Nowy")
menu_bar.add_command(label="Otwórz")
file_menu.add_command(label="Zapisz")
file_menu.add_separator()
file_menu.add_command(label="Zamknij", command=root.quit)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="O programie", command=about)

root.mainloop()