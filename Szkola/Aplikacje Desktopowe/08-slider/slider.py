import tkinter as tk

def update(event):
    label.config(text=f"Wartość slidera: {slider.get()}")

root = tk.Tk()
root.title("Przykład slidera(scale)")
root.geometry("300x200")

label = tk.Label(root, text="Wartość slidera:")
label.pack(pady=10)

#slider

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update)
slider.pack(pady=10)

root.mainloop()