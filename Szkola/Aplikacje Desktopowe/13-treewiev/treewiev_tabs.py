import tkinter as tk
from tkinter import ttk

class TableTabsExample(tk.Tk):
    def __init__(self):
        super().__init__()

        tk.Label(self, text="Liczba samochodów:").pack(pady=10)

        self.title("Treeview w zakładkach")
        self.geometry("600x400")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        frame1 = ttk.Frame(self.notebook)
        self.notebook.add(frame1, text='Zakładka 1')

        frame2 = ttk.Frame(self.notebook)
        self.notebook.add(frame2, text='Pracownicy')

        emp_columns = ['imie', 'nazwisko', 'stanowisko']
        self.emp_table = ttk.Treeview(frame2, columns=emp_columns, show="headings", height=8)
        for emp in emp_columns:
            self.emp_table.heading(emp, text=emp.capitalize())
            self.emp_table.column(emp, width=150, anchor="center")

        self.emp_table.pack(fill="both", expand=True)

        emp_data = [
            ("Jan", "Kowalski", "Inżynier"),
            ("Anna", "Nowak", "Manager"),
            ("Piotr", "Wiśniewski", "Programista"),
            ("Katarzyna", "Wójcik", "Analityk"),
            ("Michał", "Kamiński", "Tester")
        ]

        for emp in emp_data:
            self.emp_table.insert('', tk.END, values=emp)

        #definicja tabeli
        columns = ['marka', 'model', 'rocznik']
        self.table = ttk.Treeview(frame1, columns=columns, show="headings", height=8)

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
    app = TableTabsExample()
    app.mainloop()