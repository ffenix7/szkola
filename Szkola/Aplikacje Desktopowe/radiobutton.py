import tkinter as tk

def show_selection():
    label.config(text=fuel_var.get())

root = tk.Tk()
root.title("Radiobutton")
root.geometry("300x200")

fuel_var = tk.StringVar()

rb1 = tk.Radiobutton(root, text="Benzyna", variable=fuel_var, value="Benzyna")
rb1.pack(anchor='w')

rb2 = tk.Radiobutton(root, text="Diesel", variable=fuel_var, value="Diesel")
rb2.pack(anchor='w')

rb3 = tk.Radiobutton(root, text="LPG", variable=fuel_var, value="LPG")
rb3.pack(anchor='w')

button = tk.Button(root, text="Wybierz", command=show_selection)
button.pack(pady=10)

label = tk.Label(root, text="")
label.pack()

root.mainloop()