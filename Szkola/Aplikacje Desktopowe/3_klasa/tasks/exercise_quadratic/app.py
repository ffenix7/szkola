import tkinter as tk
import math
from tkinter import messagebox

def calculate_roots():
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for A, B, and C.")
        return
    if a == 0:
        messagebox.showerror("Input Error", "Coefficient A cannot be zero.")
        return
    
    delta = b**2 - (4*a*c)
    
    if delta < 0:
        result.config(text="No real roots.")
        return
    
    elif delta == 0:
        x = -b / (2*a)
        result.config(text=f"One real root: x = {x:.2f}")
        return
    
    else:
        x_1 = (-b - math.sqrt(delta)) / (2*a)
        x_2 = (-b + math.sqrt(delta)) / (2*a)
        result.config(text=f"Two real roots: x1 = {x_1:.2f}, x2 = {x_2:.2f}")

root = tk.Tk()
root.title("Quadratic Equation Solver")
root.geometry("300x400")
root.configure(bg="darkblue")

label_0 = tk.Label(root, text="Calculate Roots of Quadratic Equation", bg="darkblue", fg="white", font=("Helvetica", 12))
label_0.pack(pady=10)

frame_1 = tk.Frame(root, bg="darkblue")
frame_1.pack(pady=20)

label_a = tk.Label(frame_1, text="A:", bg="darkblue", fg="white")
entry_a = tk.Entry(frame_1)
label_a.pack(pady=5, padx=5, anchor='w', side='left')
entry_a.pack(pady=5, anchor='w')

frame_2 = tk.Frame(root, bg="darkblue")
frame_2.pack(pady=20)

label_b = tk.Label(frame_2, text="B:", bg="darkblue", fg="white")
entry_b = tk.Entry(frame_2)
label_b.pack(pady=5, padx=5, anchor='w', side='left')
entry_b.pack(pady=5, anchor='w')

frame_3 = tk.Frame(root, bg="darkblue")
frame_3.pack(pady=20)

label_c = tk.Label(frame_3, text="C:", bg="darkblue", fg="white")
entry_c = tk.Entry(frame_3)
label_c.pack(pady=5, padx=5, anchor='w', side='left')
entry_c.pack(pady=5, anchor='w')

frame_4 = tk.Frame(root, bg="darkblue")
frame_4.pack(pady=20)
frame_5 = tk.Frame(frame_4, bg="darkblue", highlightbackground="black", highlightthickness=2)
frame_5.pack()

button = tk.Button(frame_5, text="Calculate Roots", command=calculate_roots, bg="blue", fg="white", width=30, height=3)
button.pack()

result = tk.Label(frame_4, text="", bg="darkblue", fg="white", font=("Helvetica", 12))
result.pack(pady=5)

root.mainloop()