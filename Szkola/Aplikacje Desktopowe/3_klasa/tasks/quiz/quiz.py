import tkinter as tk
import tkinter.ttk as ttk

def show_summary():
    name = entry_1.get()
    difficulty = combo_1.get()
    topics = []

    if var_1.get():
        topics.append("Sieci komputerowe")
    if var_2.get():
        topics.append("Systemy operacyjne")
    if var_3.get():
        topics.append("Bazy danych")
    if var_4.get():
        topics.append("Programowanie")
    
    language = ''
    if var_radio.get() == 1:
        language = "HTML"
    elif var_radio.get() == 2:
        language = "Python"
    elif var_radio.get() == 3:
        language = "CSS"

    time = slider_1.get()
    summary = (f"Imię: {name}\n"
               f"Poziom trudności: {difficulty}\n"
               f"Wybrane tematy: {', '.join(topics)}\n"
               f"Język programowania: {language}\n"
               f"Czas na odpowiedź: {time} sekund")
    
    label_summary.config(text=summary)

root = tk.Tk()
root.title("Quiz Informatyczny")
root.geometry("800x800")

label_summary = tk.Label(root, text="", justify='left')
label_summary.pack()

label_1 = tk.Label(root, text="Imię:")
entry_1 = tk.Entry(root)
label_1.pack()
entry_1.pack()

label_2 = tk.Label(root, text="Poziom trudności")
label_2.pack()
combo_1 = ttk.Combobox(root, values=["Łatwy", "Średni", "Trudny"], state="readonly")
combo_1.pack()

label_3 = tk.Label(root, text="Wybierz tematy")

var_1 = tk.BooleanVar()
var_2 = tk.BooleanVar()
var_3 = tk.BooleanVar()
var_4 = tk.BooleanVar()
select_1 = tk.Checkbutton(root, text="Sieci komputerowe", variable=var_1)
select_2 = tk.Checkbutton(root, text="Systemy operacyjne", variable=var_2)
select_3 = tk.Checkbutton(root, text="Bazy danych", variable=var_3)
select_4 = tk.Checkbutton(root, text="Programowanie", variable=var_4)
label_3.pack()
select_1.pack()
select_2.pack()
select_3.pack()
select_4.pack()


label_4 = tk.Label(root, text="Który język nadaje się do programowania?")
var_radio = tk.IntVar()
radio_1 = tk.Radiobutton(root, text="HTML", value=1, variable=var_radio)
radio_2 = tk.Radiobutton(root, text="Python", value=2, variable=var_radio)
radio_3 = tk.Radiobutton(root, text="CSS", value=3, variable=var_radio)
label_4.pack()
radio_1.pack()
radio_2.pack()
radio_3.pack()


label_5 = tk.Label(root, text="Czas na odpowiedź")
slider_1 = tk.Scale(root, from_=0, to=100, orient='horizontal', tickinterval=10, length=400)
label_5.pack()
slider_1.pack()

button_1 = tk.Button(root, text="Pokaż podsumowanie", command=show_summary)
button_1.pack(pady=20)
root.mainloop()