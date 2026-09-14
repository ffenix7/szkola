import tkinter as tk
from tkinter import ttk

def update_subcategories(event):
    selected_category = category_combo.get()
    subcategory_combo['values'] = categories.get(selected_category, [])
    subcategory_combo.set('')  

def update_result(event):
    result.config(text="Wybrano:" + subcategory_combo.get())

categories = {
    "Języki programowania": ["Python", "Java", "C++", "JavaScript", "Ruby"],
    "Frameworki": ["Django", "Flask", "React", "Angular", "Vue"],
    "Bazy danych": ["MySQL", "PostgreSQL", "SQLite", "MongoDB", "Redis"]
}

root = tk.Tk()
root.title("Zależny comboboxy")
root.geometry("300x200")

tk.Label(root, text="Wybierz kategorię:").pack(pady=10)

result = tk.Label(root, text='')
result.pack(pady=10)

category_combo = ttk.Combobox(root, values=list(categories.keys()), state='readonly')
category_combo.pack(pady=10)
category_combo.bind("<<ComboboxSelected>>", update_subcategories)

#drugie combo - podkategorie

subcategory_combo = ttk.Combobox(root, values=[], text="Wybierz podkategorię:", state='readonly')
subcategory_combo.pack(pady=10)
subcategory_combo.bind("<<ComboboxSelected>>", update_result)

root.mainloop()