import tkinter as tk
from tkinter import messagebox

buttons = [[]]
board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
num_of_clicks = 0
finished = False

DARK_BG = "#121212"
FG = "#FFFFFF"
BUTTON_BG = "#1F1F1F"
ACTIVE_BG = "#333333"
NEW_GAME_BG = "#2e8b57"

def check(i, j):
    global num_of_clicks, finished

    if entry_1_var.get() == "" or entry_2_var.get() == "":
        messagebox.showwarning("Uwaga!", "Podaj oba imiona!")
        return
    
    if board[i][j] != "0" or finished:
        return

    num_of_clicks +=1

    if num_of_clicks % 2:
        buttons[i][j].config(text="X")
        board[i][j] = "1"
    else:
        buttons[i][j].config(text="O")
        board[i][j] = "2"
    current_player = entry_1_var.get() if num_of_clicks % 2 else entry_2_var.get()
    check_board(current_player)

def check_board(current_player):
    global board, finished
    #horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "0":
            label.config(text=f"Wygrana {current_player}")
            finished = True
            return
    #vertical
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "0":
            label.config(text=f"Wygrana {current_player}")
            finished = True
            return
    
    #diagonal 1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "0":
        label.config(text=f"Wygrana {current_player}")
        finished = True
        return
    
    #diagonal 2
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != "0":
        label.config(text=f"Wygrana {current_player}")
        finished = True
        return
    
    # draw
    if num_of_clicks == 9:
        label.config(text="Remis!")
        finished = True

def new_game():
    global board, finished, num_of_clicks
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")
    finished = False
    label.config(text="")
    num_of_clicks = 0


root = tk.Tk()

root.geometry("300x500")
root.title("Tic Tac Toe")
root.configure(bg=DARK_BG)

label = tk.Label(root, text="", bg=DARK_BG, fg=FG)
label.pack(pady=10)

entry_1_var = tk.StringVar(root, value="")
entry_1 = tk.Entry(root, textvariable=entry_1_var, bg=BUTTON_BG, fg=FG, insertbackground=FG)
entry_1.pack(pady=10)

entry_2_var = tk.StringVar(root, value="")
entry_2 = tk.Entry(root, textvariable=entry_2_var, bg=BUTTON_BG, fg=FG, insertbackground=FG)
entry_2.pack(pady=10)

frame_1 = tk.Frame(root, bg=DARK_BG)
frame_1.pack(pady=10)


for i in range(3):
    buttons.append([])
    for j in range(3):
        button = tk.Button(frame_1, text="", width=10, height=5, bg=BUTTON_BG, fg=FG, activebackground=ACTIVE_BG, activeforeground=FG, command=lambda i=i, j=j: check(i, j))
        button.grid(row=i, column=j)
        buttons[i].append(button)

new_game_button = tk.Button(root, text="nowa gra", command=new_game, bg=NEW_GAME_BG, fg=FG, activebackground="#27664a")
new_game_button.pack(pady=10)


root.mainloop()