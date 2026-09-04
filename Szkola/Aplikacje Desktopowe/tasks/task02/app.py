import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

def clear_name(name):
    return ''.join(char for char in name if char.isalnum() or char.isspace()).strip()

def calculate_price_thread():
    progres_bar['value'] = 0
    
    if not clear_name(entry.get()):
        messagebox.showerror("Błąd", "Proszę podać imię zamawiającego.")
        return

    result_text = ''
    name = clear_name(entry.get())
    dish = dish_var.get()
    quantity = scale_quant.get()
    sides_selected = [side for side, var in sides_var.items() if var.get()]
    drink = drink_var.get()
    price = 0

    price += dishes[dish]
    progres_bar['value'] += 25
    result_text = f"Zamówienie dla {name}:\nDanie główne: {dish}\n"
    update_text(result_text)
    time.sleep(0.5)

    for side in sides_selected:
        price += sides[side]
    progres_bar['value'] += 25
    result_text += f"Dodatki: {', '.join(sides_selected) if sides_selected else 'Brak'}\n"
    update_text(result_text)
    time.sleep(0.5)

    if drink == "Sok(8zł)":
        price += 8
    elif drink == "Cola(12zł)":
        price += 12
    progres_bar['value'] += 25
    result_text += f"Napój: {drink}\n"
    update_text(result_text)
    time.sleep(0.5)

    total_price = price * quantity
    progres_bar['value'] += 25
    result_text += f"Ilość porcji: {quantity}\nCałkowity koszt: {total_price}zł"
    update_text(result_text)

def update_text(text):
    text_result.config(state='normal')
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, text)
    text_result.config(state='disabled')

def calculate_price():
    threading.Thread(target=calculate_price_thread, daemon=True).start()

def new_order():
    entry.delete(0, tk.END)
    dish_var.set("Spaghetti Bolognese(30zł)")
    for var in sides_var.values():
        var.set(False)
    drink_var.set("Woda")
    scale_quant.set(1)
    porc_label.config(text="1 porcja")
    progres_bar['value'] = 0
    update_text("")

def update_portions(val):
    val_int = int(float(val))
    porc_label.config(text=f"{val_int} porcj{'e' if 5 > val_int > 1 else('i' if val_int == 5 else 'a')}")

root = tk.Tk()
root.title("Kalkulator zamówień obiadu")
root.geometry("400x850")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Nowe zamówienie", command=new_order)
file_menu.add_command(label="Wyjście", command=root.quit)

tk.Label(root, text="Kalkulator zamówień obiadu").pack(pady=10)
tk.Label(root, text="Imię zamawiającego:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Label(root, text="Wybierz danie główne:").pack(pady=5)
dish_var = tk.StringVar(value="Spaghetti Bolognese(30zł)")
dishes = {"Pierogi(25zł)": 25, 'Spaghetti Bolognese(30zł)': 30, 'Sałatka Cezar(20zł)': 20, 'Zupa Pomidorowa(15zł)': 15}
combo_dish = ttk.Combobox(root, textvariable=dish_var, values=list(dishes.keys()), state="readonly")
combo_dish.pack(pady=5)

tk.Label(root, text="Wybierz dodatki:").pack(pady=5)
sides_var = {}
sides = {"Chleb(5zł)": 5, 'Surówka(10zł)': 10, 'Deser(15zł)': 15}
for side in sides.keys():
    var = tk.BooleanVar()
    tk.Checkbutton(root, text=side, variable=var).pack(pady=2)
    sides_var[side] = var

tk.Label(root, text="Wybierz napój:").pack(pady=5)
drink_var = tk.StringVar(value="Woda")
tk.Radiobutton(root, text="Woda(+0zł)", variable=drink_var, value="Woda").pack()
tk.Radiobutton(root, text="Sok(+8zł)", variable=drink_var, value="Sok(8zł)").pack()
tk.Radiobutton(root, text="Cola(+12zł)", variable=drink_var, value="Cola(12zł)").pack()

tk.Label(root, text="Ilość porcji:").pack()
scale_quant = tk.Scale(root, from_=1, to=5, orient='horizontal', length=200, command=update_portions)
scale_quant.pack()
porc_label = tk.Label(root, text="1 porcja")
porc_label.pack(pady=5)

tk.Button(root, text="Oblicz koszt zamówienia", command=calculate_price).pack(pady=10)

progres_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progres_bar.pack(pady=10)

text_result = tk.Text(root, height=12, width=40, state='disabled')
text_result.pack(pady=10)

root.mainloop()