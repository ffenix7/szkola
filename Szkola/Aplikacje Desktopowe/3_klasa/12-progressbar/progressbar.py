import tkinter as tk
from tkinter import ttk
import time
import threading

class ProgressBar(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Progressbar")
        self.geometry("400x300")

        tk.Label(self, text='Postęp zadania', font=('Arial', 14)).pack(pady=10)

        # pasek postępu
        self.progress = ttk.Progressbar(self, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=10)

        tk.Label(self, text='Tryb animacji', font=('Arial', 14)).pack(pady=10)
        self.progress_ind = ttk.Progressbar(self, orient='horizontal', length=300, mode='indeterminate')
        self.progress_ind.pack(pady=10)

        ttk.Button(self, text='Start zadania', command=self.start_task).pack(pady=10)
        ttk.Button(self, text='Start animacji', command=self.start_indeterminate).pack(pady=10)
        ttk.Button(self, text='Stop animacji', command=self.stop_indeterminate).pack(pady=10)

    def start_task(self):
        """symulacja zadania krok po kroku w osobnym wątku"""
        def task():
            self.progress['value'] = 0
            for i in range(101):
                time.sleep(0.05)
                self.progress['value'] = i
        threading.Thread(target=task, daemon=True).start()

    def start_indeterminate(self):
        self.progress_ind.start(50)

    def stop_indeterminate(self):
        self.progress_ind.stop()


if __name__ == "__main__":
    app = ProgressBar()
    app.mainloop()