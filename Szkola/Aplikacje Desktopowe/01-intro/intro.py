import tkinter as tk

def hello():
    label.config(text="Dobry chłopiec")

root = tk.Tk()  #tworzenie okna głównego aplikacji
root.geometry("300x150") #szerokość x wysokość
root.title("Hello")

#tworzenie etykiety
label = tk.Label(root, text="Hello world", font=("Arial", 24))
label.pack(pady=20)

#przycisk
button = tk.Button(root, text="Kliknij mnie", command=hello, font = ("Arial", 12))
button.pack(pady=10)

root.mainloop()
