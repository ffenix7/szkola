import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import colorchooser

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

def about():
    messagebox.showinfo("O programie", "Prosty Edytor Tekstu\nAutor: Filip Fenix Gębala")

def update_font(font_name):
    current_font = text_area.cget("font").split()
    font_size = current_font[1] if len(current_font) > 1 else 12
    text_area.config(font=(font_name, font_size))

def update_font_size(size):
    current_font = text_area.cget("font").split()
    font_name = current_font[0]
    text_area.config(font=(font_name, size))

def change_bg_color():
    color = colorchooser.askcolor(title ="Wybierz kolor tła")[1]
    if color[1]:
        text_area.config(bg=color)

def change_text_color():
    color = colorchooser.askcolor(title ="Wybierz kolor tekstu")[1]
    if color[1]:
        text_area.config(fg=color)

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

# Menu edycja
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edycja", menu=edit_menu)
edit_menu.add_command(label="Cofnij", command=lambda: text_area.event_generate("<<Undo>>"))
edit_menu.add_command(label="Ponów", command=lambda: text_area.event_generate("<<Redo>>"))
edit_menu.add_command(label="Wytnij", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Kopiuj", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Wklej", command=lambda: text_area.event_generate("<<Paste>>"))

#Menu format
format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Zmień kolor tła", command=change_bg_color)
format_menu.add_command(label="Zmień kolor tekstu", command=change_text_color)

#Menu pomoc
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Pomoc", menu=help_menu)
help_menu.add_command(label="O programie", command=about)

#Pasek narzędzi - czcionka
tool_bar = tk.Frame(root)
tool_bar.pack(side=tk.TOP, fill=tk.X)

#lista czcionek
available_fonts = ["Arial", "Courier New", "Times New Roman", "Verdana", "Helvetica"]
font_family = tk.StringVar(value=available_fonts[0])
font_menu = tk.OptionMenu(tool_bar, font_family, *available_fonts, command=update_font)
font_menu.pack(side=tk.LEFT)
for font in available_fonts:
    edit_menu.add_command(label=f"Ustaw czcionkę: {font}")

#Rozmiar czcionki
font_size = tk.IntVar(value=12)
size_menu = tk.OptionMenu(tool_bar, font_size, *[8, 10, 12, 14, 16, 18, 20, 24, 28, 32], command=update_font_size)
size_menu.pack(side=tk.LEFT)

text_area = tk.Text(root, wrap='word')
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


scrollbar = tk.Scrollbar(root, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

root.mainloop()
