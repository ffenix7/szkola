import tkinter as tk
from tkinter import ttk

class TableExample(tk.Tk):
    def __init__(self):
        super().__init__()

        tk.Label(self, text="Liczba samochodów:").pack(pady=10)

        #definicja tabeli
        columns = ['marka', 'model', 'rocznik']
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=8)

        #naglówki kolumn 
        self.table.heading('marka', text='Marka')
        self.table.heading('model', text='Model')
        self.table.heading('rocznik', text='Rocznik')

        #szerokość kolumn
        self.table.column('marka', width=200, anchor="center")
        self.table.column('model', width=200, anchor="center")
        self.table.column('rocznik', width=100, anchor="center")

        #dodanie danych do tabeli
        cars = [
            ("Toyota", "Corolla", 2020),
            ("Honda", "Civic", 2019),
            ("Ford", "Focus", 2018),
            ("Chevrolet", "Malibu", 2021),
            ("Nissan", "Sentra", 2020)
        ]

        for car in cars:
            self.table.insert('', tk.END, values=car)

        #scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True, padx=20, pady=10)
        scrollbar.pack(side="right", fill="y")


if __name__ == "__main__":
    app = TableExample()
    app.mainloop()