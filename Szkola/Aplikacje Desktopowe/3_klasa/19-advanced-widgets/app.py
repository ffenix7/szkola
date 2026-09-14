import tkinter as tk
from tkinter import ttk, messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.title("Task Manager")
        self.root.geometry("400x300")

        #lewa i prawa część okna 
        self.paned = ttk.Panedwindow(self.root, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #lewy panel - lista zadań
        left_frame = ttk.Frame(self.paned)

        #prawy panel - idk
        right_frame = ttk.Frame(self.paned)

        self.paned.add(left_frame)
        self.paned.add(right_frame)

        #listbox z paskiem przewijania
        self.task_list = tk.Listbox(left_frame, height=15)
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.task_list.yview)
        self.task_list.config(yscrollcommand=scrollbar.set)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #dodawanie zadań
        ttk.Label(right_frame, text="New Task:").pack(pady=5)
        self.entry = tk.Entry(right_frame)
        self.entry.pack(pady=5)

        ttk.Button(right_frame, text="Add Task", command=self.add_task).pack(pady=5)
        ttk.Button(right_frame, text="Remove Task", command=self.delete_task).pack(pady=5)
        ttk.Button(right_frame, text="Info", command=self.show_details).pack(pady=5)
        status_button = tk.Button(self.root, text="Change task status", command=self.change_status)
        status_button.pack(pady=5)

        self.on_open()
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def show_details(self):
        selected = self.task_list.curselection()
        if not selected:
            messagebox.showinfo("Task Info", "No task selected.")
            return
        task_name = self.task_list.get(selected)

        #nowe okno (toplevel)
        top = tk.Toplevel(self.root)
        top.title("Task Details")
        top.geometry("250x150")

        ttk.Label(top, text=f"Task: {task_name}").pack(pady=10)
        ttk.Button(top, text="Close", command=top.destroy).pack(pady=10)

    def change_status(self):
        selected = self.task_list.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to change status.")
            return

        idx = selected[0]
        task = self.task_list.get(idx)

        if task.startswith("[Done] "):
            new = "[Pending] " + task[6:]
            color = "orange"
        elif task.startswith("[Pending] "):
            new = "[TODO] " + task[10:]
            color = "red"
        elif task.startswith("[TODO] "):
            new = "[Done] " + task[6:]
            color = "green"
        else:
            new = "[Done] " + task
            color = "green"

        self.task_list.delete(idx)
        self.task_list.insert(idx, new)

        self.task_list.itemconfig(idx, bg=color)

    def save_to_json(self, filename="tasks.json"):
        import json
        tasks = self.task_list.get(0, tk.END)
        with open(filename, 'w') as f:
            json.dump(tasks, f)

    def read_from_json(self, filename="tasks.json"):
        import json
        try:
            with open(filename, 'r') as f:
                tasks = json.load(f)
                for task in tasks:
                    self.task_list.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def on_open(self):
        self.read_from_json()

    def on_close(self):
        self.save_to_json()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
