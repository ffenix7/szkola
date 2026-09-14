# Zadanie 1 — Galeria kształtów
# Imię i nazwisko: Filip Gębala
# Data: 20.03.2026

import tkinter as tk
import random


COLORS = ["#e74c3c", "#3498db", "#27ae60", "#f39c12",
          "#9b59b6", "#1abc9c", "#e67e22", "#2c3e50"]

def create_window():
    num_elems = 0
    def draw_line():
        nonlocal num_elems
        x = random.randint(1, 500)
        y = random.randint(1, 300)
        delta_x = abs(x - random.randint(1, 500))
        delta_y = abs(y - random.randint(1, 300))
        canvas.create_line(x, y, delta_x, delta_y, fill=random.choice(COLORS), width=2)
        num_elems += 1
        label.config(text=num_elems)

    def draw_rectangle():
        nonlocal num_elems
        x = random.randint(1, 500)
        y = random.randint(1, 300)
        delta_x = abs(x - random.randint(1, 500))
        delta_y = abs(y - random.randint(1, 300))
        canvas.create_rectangle(x, y, delta_x, delta_y, fill=random.choice(COLORS), width=2)
        num_elems += 1
        label.config(text=num_elems)

    def draw_circle():
        nonlocal num_elems
        x = random.randint(1, 500)
        y = random.randint(1, 300)
        delta_x = abs(x - random.randint(1, 500))
        delta_y = abs(y - random.randint(1, 300))
        canvas.create_oval(x, y, delta_x, delta_y, fill=random.choice(COLORS), width=2)
        num_elems += 1
        label.config(text=num_elems)

    def draw_poly():
        nonlocal num_elems
        points = []
        for i in range(10):
            if i%2:
                points.append(random.randint(0, 300))
            else:
                points.append(random.randint(0, 500))
        canvas.create_polygon(points, fill=random.choice(COLORS), width=2)
        num_elems += 1
        label.config(text=num_elems)

    def clear_canvas():
        canvas.delete("all")
        nonlocal num_elems
        num_elems = 0
        label.config(text=num_elems)

    window = tk.Tk()
    window.title("Galeria kształtów")
    window.geometry("820x630")
    window.resizable(False, False)

    line_button = tk.Button(window, text="Linia", command=draw_line)
    line_button.pack(pady=10)

    square_button = tk.Button(window, text="Prostokąt", command=draw_rectangle)
    square_button.pack(pady=10)

    circle_button = tk.Button(window, text="Owal", command=draw_circle)
    circle_button.pack(pady=10)

    poly_button = tk.Button(window, text="Wielokąt", command=draw_poly)
    poly_button.pack(pady=10)

    clear_button = tk.Button(window, text="Wyczyść", command= clear_canvas)
    clear_button.pack(pady=10)

    def on_right_click(event):
        item = canvas.find_closest(event.x, event.y)
        if item:
            canvas.delete(item)
            nonlocal num_elems
            num_elems -= 1
            label.config(text=num_elems)


    canvas = tk.Canvas(window,width=500, height=300, bg="white")
    canvas.pack()
    canvas.bind("<Button-3>", on_right_click)

    label = tk.Label(window, text="0")
    label.pack(pady=20)

    return window

if __name__ == "__main__":
    window = create_window()
    window.mainloop()