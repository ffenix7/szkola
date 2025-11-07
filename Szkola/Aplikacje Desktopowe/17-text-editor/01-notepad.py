import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Pliki tekstowe', '*.txt'), ('Wszystkie pliki', '*.*')])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
    if not file_path:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano pliku.")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Pliki tekstowe', '*.txt'), ('Wszystkie pliki', '*.*')])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
    if not file_path:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano pliku do zapisu.")

root = tk.Tk()
root.title("Prosty Edytor Tekstu")
root.geometry("600x400")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Nowy", command=new_file)
file_menu.add_command(label="Otwórz", command=open_file)
file_menu.add_command(label="Zapisz", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Zamknij", command=root.quit)

text_area = tk.Text(root, wrap='word')
scrollbar = tk.Scrollbar(root, command=text_area.yview)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill="y")

root.mainloop()
