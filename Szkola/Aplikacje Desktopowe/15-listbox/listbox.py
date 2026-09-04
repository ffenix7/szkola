import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

def show_selection():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Selection", "No languages selected.")
        return
    selected_languages = [listbox.get(i) for i in selected]
    messagebox.showinfo("Selected Languages", ", ".join(selected_languages))
    return

tk.Label(root, text="Select your favorite programming languages:").pack(pady=10)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
for lang in languages:
    listbox.insert(tk.END, lang)
listbox.pack(pady=10)

tk.Button(root, text="Show Selection", command=show_selection).pack(pady=10)

root.mainloop()