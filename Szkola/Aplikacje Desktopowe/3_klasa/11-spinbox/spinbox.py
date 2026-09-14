import tkinter as tk
from tkinter import ttk

class SpinboxMonths(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Spinbox - wybór miesiąca")
        self.geometry("300x200")

        # Lista miesięcy
        months = [
            "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]

        tk.Label(self, text='Wybierz miesiąc:', font=("Arial", 12)).pack(pady=10)

        # spinbox z listą tekstową
        self.spin_var = tk.StringVar(value=months[0])
        self.spinbox = ttk.Spinbox(
            self,
            values=months,
            textvariable=self.spin_var,
            width=12,
            state='readonly',
            font=("Arial", 12)
        )
        self.spinbox.pack(pady=10)

        self.button = ttk.Button(self, text='Pokaż wybór', command=self.show_value)
        self.button.pack(pady=10)

        self.result_label = tk.Label(self, text='', font=("Arial", 12))
        self.result_label.pack(pady=10)

    def show_value(self):
        value = self.spinbox.get() # spin_var
        self.result_label.config(text=f'Wybrałeś miesiąc: {value}')

if __name__ == "__main__":
    app = SpinboxMonths()
    app.mainloop()