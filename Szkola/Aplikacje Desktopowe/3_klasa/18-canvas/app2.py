import tkinter as tk
from tkinter import colorchooser

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y, shape_id
    if mode.get() == "Pędzel":
        canvas.create_line(event.x - pen_size/2, event.y - pen_size/2, event.x + pen_size/2, event.y + pen_size/2, fill=pen_color)
    else:
        #Usuwamy poprzedni kształt tymczasowy
        if shape_id:
            canvas.delete(shape_id)
        if mode.get() == "Linia":
            shape_id = canvas.create_line(last_x, last_y, event.x, event.y, fill=pen_color, width=pen_size)
        elif mode.get() == "Prostokąt":
            shape_id = canvas.create_rectangle(last_x, last_y, event.x, event.y, outline=pen_color, width=pen_size)
        elif mode.get() == "Elipsa":
            shape_id = canvas.create_oval(last_x, last_y, event.x, event.y, outline=pen_color, width=pen_size)

def finalize_shape(event):
    '''Zatwierdza rysowanie kształtu po puszczeniu myszki'''
    global shape_id
    shape_id = None


def change_color():
    global pen_color
    color = colorchooser.askcolor()[1]
    if color:
        pen_color = color

def change_size(value):
    global pen_size
    pen_size = int(value)

root = tk.Tk()
root.title("Prosty Rysownik")
root.geometry("800x600")

pen_color = "black"
pen_size = 5
last_x, last_y = None, None
shape_id = None

toolbar = tk.Frame(root)
toolbar.pack(side='top', fill=tk.X)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

btn_color = tk.Button(toolbar, text="Wybierz kolor", command=change_color)
btn_color.pack(side=tk.LEFT, padx=5, pady=5)

btn_clear = tk.Button(toolbar, text="Wyczyść", command=lambda: canvas.delete("all"))
btn_clear.pack(side=tk.LEFT, padx=5, pady=5)

size_scale = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, label="Rozmiar pióra", command=change_size)
size_scale.set(pen_size)
size_scale.pack(side=tk.LEFT, padx=5, pady=5)

#tryb rysowania
mode = tk.StringVar(value="Pędzel")
modes = ["Pędzel", "Linia", "Prostokąt", "Elipsa"]
for m in modes:
    rb = tk.Radiobutton(toolbar, text=m, variable=mode, value=m).pack(side=tk.LEFT, padx=5, pady=5)

#Obsługa myszy
canvas.bind('<Button-1>', start_draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', finalize_shape)

root.mainloop() 