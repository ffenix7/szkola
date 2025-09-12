import tkinter as tk
from tkinter import ttk

def show_selection(event):
    result.config(text=f"wybrano: {combo.get()}")

root = tk.Tk()
root.title("Pole combo")
root.geometry("300x200")

label = tk.Label(root, text="Wybierz język programowania:")
label.pack(pady=10)

#combobox

languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
combo = ttk.Combobox(root, values=languages, state="readonly")
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", show_selection)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()