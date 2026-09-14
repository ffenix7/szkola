# Zadanie 3 — Animacja: odbijające się kule
# Imię i nazwisko: Filip Gębala
# Data: 26.03.2026

import tkinter as tk
import random

COLORS = ["#e74c3c", "#3498db", "#27ae60", "#f39c12",
          "#9b59b6", "#1abc9c", "#e67e22", "#f1c40f"]

WIDTH, HEIGHT = 500, 400
NUM_BALLS = 10

def create_window():
    window = tk.Tk()
    window.title("Odbijające się kule")
    window.geometry(f"{WIDTH}x{HEIGHT+60}")
    window.resizable(False, False)

    # TODO: Canvas WIDTH x HEIGHT z ciemnym tłem (#1a1a2e)
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="#1a1a2e")

    # każda z losowym kolorem, prędkością (dx, dy) i promieniem (10-25)
    balls = []
    running = []
    for i in range(NUM_BALLS):
        x = random.randint(1, 500)
        y = random.randint(1, 300)
        r = random.randint(10,25)
        ball = canvas.create_oval(x, y, r, r, fill="#e74c3c", outline="")
        balls.append(ball)
        running.append(False)

    # TODO: Animacja — kule odbijają się od ścian
    # window.after(16, animate)

    # TODO: Przycisk "Start/Stop"

    # TODO: Kliknięcie w kulę zmienia jej kolor na losowy
    # hint: canvas.find_closest(event.x, event.y)

    # TODO: Label z liczbą kul i FPS (aktualizowany co sekundę)

    return window

if __name__ == "__main__":
    window = create_window()
    window.mainloop()