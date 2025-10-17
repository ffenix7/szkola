import tkinter as tk
from tkinter import ttk, messagebox
import os

class FileExplorer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Explorer")
        self.geometry("600x400")

        self.tree = ttk.Treeview(self)
        self.tree.heading("#0", text="Pliki i foldery", anchor='w')
        self.tree.pack(fill="both", expand=True)

        #scroll
        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        start_path = os.getcwd()
        root_node = self.tree.insert('', 'end', text=start_path, open=True, values=[start_path])
        self.populate_tree(root_node, start_path)

        #obsługa rozwijania katalogu
        self.tree.bind('<<TreeviewOpen>>', func=self.open_node)

        #obsługa podwójnego kliknięcia
        self.tree.bind('<Double-1>', self.open_file)

    def populate_tree(self, parent, path):
        """dodaje pliki i foldery do drzewa"""
        self.tree.delete(*self.tree.get_children(parent)) #czyszczenie aby uninkąć duplikatów
        try:
            for entry in os.listdir(path):
                full_path = os.path.join(path,entry)
                node = self.tree.insert(parent, 'end', text=entry, values=[full_path])
                if os.path.isdir(full_path):
                    self.tree.insert(node, 'end') #dodanie pustego dziecka aby umożliwić rozwijanie

        except PermissionError:
            messagebox.showwarning("Ostrzeżenie", f"Chciałbyś loool. Nie masz dostępu do {path}")

    def open_node(self, event):
        """Rozwinięcie katalogu"""
        node = self.tree.focus()
        path = self.tree.item(node)['values'][0]
        if os.path.isdir(path):
            self.populate_tree(node,path)

    def open_file(self, event):
        node = self.tree.focus()
        path = self.tree.item(node)['values'][0]
        print(path)
        if os.path.exists(path):
            print(path)
            messagebox.showinfo("Plik", f"Otwieranie pliku: {path}")
        
if __name__ == "__main__":
    app = FileExplorer()
    app.mainloop()