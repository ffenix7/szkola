import tkinter as tk

def show_entry():
    user_input = entry.get()
    if user_input.strip() == "":
        result.config(text="Pole nie może być puste!")
    else:
        result.config(text=f"Wpisane: {user_input}")

root = tk.Tk()

root.title("Przykład Entry")

prompt_label = tk.Label(root, text="Wpisz coś:", font=("Arial", 14))
prompt_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

button = tk.Button(root, text="Pokaż wpisane", font=("Arial", 14), command = show_entry)
button.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 14))
result.pack(pady=10)

root.mainloop()