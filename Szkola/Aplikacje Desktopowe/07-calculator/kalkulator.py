import tkinter as tk
from tkinter import messagebox, ttk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            res = num1 + num2
        elif operation == '-':
            res = num1 - num2
        elif operation == '*':
            res = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Błąd", "Nie można dzielić przez zero!")
                return
            res = num1 / num2

        result.config(text="Wynik: " + str(res))
    except ValueError as e:
        messagebox.showerror("Błąd", str(e))


root = tk.Tk()
root.title("Prosty Kalkulator")
root.geometry("300x300")

#wynik
result = tk.Label(root, text="Wynik: ", font=("Arial", 14))
result.pack(pady=5)

tk.Label(root, text="Liczba 1:").pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack(pady=5)

tk.Label(root, text="Liczba 2:").pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack(pady=5)

frame=tk.Frame(root)
frame.pack(pady=10)

btn_add = tk.Button(frame, text="+", font=("Arial", 14), width=5, command=lambda: calculate('+'))
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_sub = tk.Button(frame, text="-", font=("Arial", 14), width=5, command=lambda: calculate('-'))
btn_sub.grid(row=0, column=1, padx=5, pady=5)

btn_mul = tk.Button(frame, text="*", font=("Arial", 14), width=5, command=lambda: calculate('*'))
btn_mul.grid(row=0, column=2, padx=5, pady=5)

btn_div = tk.Button(frame, text="/", font=("Arial", 14), width=5, command=lambda: calculate('/'))
btn_div.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()