import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

PASSWORD = ''

def generate_password(verbose=True):
    length = int(entry_chars.get())
    use_uppercase = check_upper_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    characters = "abcdefghijklmnopqrstuvwxyz"
    if use_uppercase:
        characters += " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        characters += "0123456789"
    if use_special:
        characters += "!@#$%^&*()"
    passwd = ''.join(random.choice(characters) for _ in range(length))
    if verbose:
        messagebox.showinfo("Wygenerowane hasło", f"Twoje hasło: {passwd}")
    global PASSWORD
    PASSWORD = passwd
    return passwd

def accept():
    name = entry_name.get()
    surname = entry_surname.get()
    position = position_var.get()
    
    if not name or not surname or not position:
        messagebox.showerror("Błąd", "Proszę wypełnić wszystkie pola.")
        return
    
    if (not PASSWORD):
        messagebox.showerror("Błąd", "Proszę wygenerować hasło.")
        return
    messagebox.showinfo("Informacje o pracowniku", f"Imię: {name}\nNazwisko: {surname}\nStanowisko: {position}\nHasło: {PASSWORD}")

root = tk.Tk()
root.title("Dodaj pracownika")
root.geometry("550x350")
root.configure(bg="#B0C4DE")

main_frame = tk.Frame(root, bg="#B0C4DE")
main_frame.pack(pady=20, padx=10, fill="both", expand=True)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

frame_1 = tk.LabelFrame(main_frame, borderwidth=2, relief="groove", text="Dane pracownika", bg="#B0C4DE", padx=10)
frame_1.grid_columnconfigure(0, weight=0)
frame_1.grid_columnconfigure(1, weight=1)

label_name = tk.Label(frame_1, text="Imię:", bg="#B0C4DE")
label_name.grid(row=0, column=0, pady=5, sticky='w')
entry_name = tk.Entry(frame_1, width=30)
entry_name.grid(row=0, column=1, pady=5, sticky='e')

label_surname = tk.Label(frame_1, text="Nazwisko:", bg="#B0C4DE")
label_surname.grid(row=1, column=0, pady=5, sticky='w')
entry_surname = tk.Entry(frame_1, width=30)
entry_surname.grid(row=1, column=1, pady=5, sticky='e')

label_position = tk.Label(frame_1, text="Stanowisko:", bg="#B0C4DE")
label_position.grid(row=2, column=0, pady=5, sticky='w')
position_var = tk.StringVar()
position_combobox = ttk.Combobox(frame_1, textvariable=position_var, values=("Kierownik", "Starszy programista", "Młodszy programista", "Tester"), width=27)
position_combobox.grid(row=2, column=1, pady=5, sticky='e')

frame_1.grid_columnconfigure(1, weight=1)
frame_1.grid(row=0, column=0, sticky='nsew', padx=10, pady=0)

frame_2 = tk.LabelFrame(main_frame, borderwidth=2, relief="groove", text="Generowanie hasła", bg="#B0C4DE", padx=10)
frame_2.grid_columnconfigure(0, weight=0)
frame_2.grid_columnconfigure(1, weight=1)
label_chars = tk.Label(frame_2, text="Ile znaków:", bg="#B0C4DE")
label_chars.grid(row=0, column=0, pady=5, sticky='w')
entry_chars = tk.Entry(frame_2, width=8)
entry_chars.grid(row=0, column=1, pady=5)

check_upper_var = tk.BooleanVar(value=True)
check_uppercase = tk.Checkbutton(frame_2, text="Wielkie litery", variable=check_upper_var, bg="#B0C4DE")
check_uppercase.grid(row=1, column=0, pady=5, sticky='w')

numbers_var = tk.BooleanVar()
check_numbers = tk.Checkbutton(frame_2, text="Cyfry", variable=numbers_var, bg="#B0C4DE")
check_numbers.grid(row=2, column=0, pady=5, sticky='w')

special_var = tk.BooleanVar()
check_special = tk.Checkbutton(frame_2, text="Znaki specjalne", variable=special_var, bg="#B0C4DE")
check_special.grid(row=3, column=0, pady=5, sticky='w')

generate_button = tk.Button(frame_2, text="Generuj hasło", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky='ew')
generate_button.configure(bg="#4682B4", fg="white")

# place frame_2 in right column and allow it to expand
frame_2.grid(row=0, column=1, sticky='nsew', padx=10, pady=0)

confirm_button = tk.Button(root, text="Zatwierdź", command=accept, width=40)
confirm_button.pack(pady=20)
confirm_button.configure(bg="#4682B4", fg="white")

root.mainloop()