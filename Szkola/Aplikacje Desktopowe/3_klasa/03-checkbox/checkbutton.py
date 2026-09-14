import tkinter as tk

def pokaz():
    result = ""
    if var1.get():
        result += "Programowanie\n"
    if var2.get():
        result += "Gry komputerowe\n"
    if var3.get():
        result += "Sport\n"
    if result.strip() == "":
        result_label.config(text="Twoje zainteresowania: Brak ")
    else:
        result_label.config(text="Twoje zainteresowania:\n" + result)

root = tk.Tk()

root.title("Przykład checkbutton")
root.geometry("500x250")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

cb1 = tk.Checkbutton(root,text="Opcja 1", variable=var1)
cb2 = tk.Checkbutton(root,text="Opcja 2", variable=var2)
cb3 = tk.Checkbutton(root,text="Opcja 3", variable=var3)

cb1.pack(anchor="w")
cb2.pack(anchor="w")
cb3.pack(anchor="w")

result_label = tk.Label(root, text="Twoje zainteresowania:", font=("Arial", 14), justify="left")

button = tk.Button(root, text="Pokaż wybór", command=pokaz, font=("Arial", 14))

button.pack(pady=10)
result_label.pack(pady=10)

root.mainloop()