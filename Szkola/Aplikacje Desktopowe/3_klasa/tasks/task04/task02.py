import tkinter as tk

window = tk.Tk()
window.title("Rysowanie")
window.geometry("600x480")

current_color = ["#2c3e50"]
current_size = [3]
last_pos = [None]

def start_draw(event):
    last_pos[0] = (event.x, event.y)

def draw(event):
    if last_pos[0]:
        x0, y0 = last_pos[0]
        canvas.create_line(
            x0, y0, event.x, event.y,
            fill=current_color[0],
            width=current_size[0],
            capstyle="round",
            smooth=True
        )
        last_pos[0] = (event.x, event.y)

def stop_draw(event):
    last_pos[0] = None

def set_color(color):
    current_color[0] = color

toolbar = tk.Frame(window, bg="gray", pady=5)
toolbar.pack(fill="x")

for color in ["#2c3e50", "#e74c3c", "#3498db", "#27ae60",
              "#f39c12", "#9b59b6", "#ffffff"]:
    tk.Button(
        toolbar, bg=color, width=3,
        relief="raised", borderwidth=2,
        command=lambda c=color: set_color(c)
    ).pack(side="left", padx=3)

tk.Label(toolbar, text="Grubość:", bg="#ecf0f1").pack(side="left", padx=5)
size_scale = tk.Scale(toolbar, from_=1, to=20, orient="horizontal",length=120, showvalue=True,command=lambda v: current_size.__setitem__(0, int(v)))
size_scale.set(3)
size_scale.pack(side="left")

tk.Button(toolbar, text="Wyczyść", command=lambda: canvas.delete("all")).pack(side="right", padx=5)

canvas = tk.Canvas(window, bg="white", cursor="crosshair")
canvas.pack(fill="both", expand=True)

canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

window.mainloop()
