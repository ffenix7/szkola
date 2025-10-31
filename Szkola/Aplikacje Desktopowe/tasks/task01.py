import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def show_summary():
    cena = 0
    imie = entry_1.get()

    if imie.strip() == "":
        messagebox.showerror("Błąd", "Proszę podać imię!")
        return

    rozmiar = combo_1.get()

    if rozmiar == "":
        messagebox.showerror("Błąd", "Proszę wybrać rozmiar pizzy!")
        return

    ciasto = ciasto_var.get()

    dodatki = []
    if var1.get():
        dodatki.append("Ser")
        cena += 3
    if var2.get():
        dodatki.append("Pieczarki")
        cena += 4
    if var3.get():
        dodatki.append("Szynka")
        cena += 4
    if var4.get():
        dodatki.append("Oliwki")
        cena += 2

    if rozmiar == "Mała":
        cena += 15

    elif rozmiar == "Średnia":
        cena += 20

    elif rozmiar == "Duża":
        cena += 25

    ostrosc = scale_1.get()

    messagebox.showinfo("Podsumowanie", message=f"Twoje zamówienie:\n\nImię: {imie}\nRozmiar pizzy: {rozmiar}\nRodzaj ciasta: {ciasto}\nDodatki: {', '.join(dodatki) if dodatki else 'Brak'}\nOstrość sosu: {ostrosc}\n\nCena: {cena}zł")

def clear_all():
    entry_1.delete(0, tk.END)
    
    combo_1.set('')

    ciasto_var.set("Cienkie")

    scale_1.set(0)

    var1.set(False)
    var2.set(False)
    var3.set(False)
    var4.set(False)

root = tk.Tk()
root.title("Kreator pizzy")
root.geometry("500x800")

label_1 = tk.Label(root, text="Podaj swoje imię:")
label_1.pack(pady=10)
entry_1 = tk.Entry(root, width=50)
entry_1.pack(pady=10)

label_2 = tk.Label(root, text="Wybierz rozmiar pizzy:")
label_2.pack(pady=10)
combo_1 = ttk.Combobox(root, values=["Mała", "Średnia", "Duża"], state="readonly")
combo_1.pack(pady=10)

ciasto_var = tk.StringVar()
ciasto_var.set("Cienkie")

label_3 = tk.Label(root, text="Wybierz rodzaj ciasta:")
label_3.pack(pady=10)
radio_1 = tk.Radiobutton(root, text="Cienkie", variable=ciasto_var, value="Cienkie")
radio_1.pack(pady=10)
radio_2 = tk.Radiobutton(root, text="Grube", variable=ciasto_var, value="Grube")
radio_2.pack(pady=10)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()

label_4 = tk.Label(root, text="Wybierz dodatki:")
label_4.pack(pady=10)
check_1 = tk.Checkbutton(root, text="Ser - 3zł", variable=var1)
check_1.pack(pady=10)
check_2 = tk.Checkbutton(root, text="Pieczarki - 4zł", variable=var2)
check_2.pack(pady=10)
check_3 = tk.Checkbutton(root, text="Szynka - 5zł", variable=var3)
check_3.pack(pady=10)
check_4 = tk.Checkbutton(root, text="Oliwki - 4zł", variable = var4)
check_4.pack(pady=10)

label_5 = tk.Label(root, text="Wybierz ostrość sosu:")
label_5.pack(pady=10)
scale_1 = tk.Scale(root, from_=0, to=10, tickinterval=1, orient="horizontal", length=150)
scale_1.pack(pady=10)

button_1 = tk.Button(root, text="Podsumowanie", command=show_summary)
button_1.pack(pady=10)

button_2 = tk.Button(root, text="Wyczyść", command=clear_all)
button_2.pack(pady=10)

root.mainloop()