import tkinter as tk
from tkinter import ttk

def show_result():
    result.config(text="Wybrano: " + entry.get() + " " + subcategory_combo.get() + "\n")
    result.config(text=result.cget("text") + "Dodatki: ")
    if var_one.get():
        result.config(text=result.cget("text") + "Klimatyzacja,")
    if var_two.get():
        result.config(text=result.cget("text") + "Nawigacja GPS,")
    if var_three.get():
        result.config(text=result.cget("text") + "Skórzana tapicerka")

categories = [
    "Toyota",
    "Honda",
    "Ford"
]

bodies = [
    "Sedan",
    "SUV",
    "Hatchback"
]

root = tk.Tk()
root.title("Zależny comboboxy")
root.geometry("200x800")

tk.Label(root, text="Wybierz kategorię:").pack(pady=10)

result = tk.Label(root, text='')
result.pack(pady=10)

label_one = tk.Label(root, text="Wybierz markę samochodu:")
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

#drugie combo - podkategorie

label_two = tk.Label(root, text="Wybierz rodzaj nadwozia:")
label_two.pack(pady=10)
subcategory_combo = ttk.Combobox(root, values=list(bodies), state='readonly')
subcategory_combo.pack(pady=10)

#check button

var_one = tk.BooleanVar()
var_two = tk.BooleanVar()
var_three = tk.BooleanVar()

check_button_one = tk.Checkbutton(root, text="Klimatyzacja", variable=var_one)
check_button_two = tk.Checkbutton(root, text="Nawigacja GPS", variable=var_two)
check_button_three = tk.Checkbutton(root, text="Skórzana tapicerka", variable=var_three)

check_button_one.pack(anchor='w')
check_button_two.pack(anchor='w')
check_button_three.pack(anchor='w')


button = tk.Button(root, text="Pokaż wynik", command=show_result)
button.pack(pady=10)

root.mainloop()