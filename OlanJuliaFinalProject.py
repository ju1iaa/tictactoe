"""
Author: Julia 
Module: Final Project
Date: 09/13/23
Info: 
Tic-Tac-Toe is a classic two-player game on a 3x3 grid. Players take turns 
placing Xs and Os to form a line of their 
symbol horizontally, vertically, or diagonally. 
The game is won when a player achieves this, 
and it's a draw if the grid is filled without a winner.

"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

clicked = True
count = 0

# create the buttons as a 2D list for easier access
buttons = [[None, None, None], [None, None, None], [None, None, None]]

# function to check if a player has won and update button colors
def check_winner(player):
    for row in buttons:
        if all(cell["text"] == player for cell in row):
            for cell in row:
                cell.config(bg="red")
            return True
    for col in range(3):
        if all(buttons[row][col]["text"] == player for row in range(3)):
            for row in range(3):
                buttons[row][col].config(bg="red")
            return True
    if all(buttons[i][i]["text"] == player for i in range(3)):
        for i in range(3):
            buttons[i][i].config(bg="red")
        return True
    if all(buttons[i][2 - i]["text"] == player for i in range(3)):
        for i in range(3):
            buttons[i][2 - i].config(bg="red")
        return True
    return False

# function to handle button clicks
def b_click(b):
    global clicked, count
    if b["text"] == "" and clicked:
        b["text"] = "X"
        count += 1
        if check_winner("X"):
            messagebox.showinfo("Tic Tac Toe", "Congrats! X is the winner")
            disable_all_buttons()
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            disable_all_buttons()
        clicked = not clicked
    elif b["text"] == "" and not clicked:
        b["text"] = "O"
        count += 1
        if check_winner("O"):
            messagebox.showinfo("Tic Tac Toe", "Congrats! O is the winner")
            disable_all_buttons()
        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            disable_all_buttons()
        clicked = not clicked
    elif count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")

# function to disable all buttons
def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

# function to reset the game
def reset():
    global buttons, clicked, count
    clicked = True
    count = 0
    buttons = [[None, None, None], [None, None, None], [None, None, None]]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = Button(root, text="", font=("Comics", 20), height=3, width=6, bg="SystemButtonFace", command=lambda i=i, j=j: b_click(buttons[i][j]))
            buttons[i][j].grid(row=i, column=j)

# create the buttons and grid
reset()

# create the menu
MainMenu = Menu(root)
root.config(menu=MainMenu)

# add options to the menu
OptionMenuTwo = Menu(MainMenu, tearoff=False)
MainMenu.add_cascade(label="How to play", menu=OptionMenuTwo)
OptionMenuTwo.add_command(label="Needs two players. Get three in a row to win.")

OptionMenu = Menu(MainMenu, tearoff=False)
MainMenu.add_cascade(label="Options", menu=OptionMenu)
OptionMenu.add_command(label="Reset game", command=reset)

root.mainloop()
