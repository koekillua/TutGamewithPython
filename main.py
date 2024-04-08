from tkinter import *
import random

def whoseturn(row, column):
    global player

    if buttons[row][column]['text'] == "" and checkwinner == False:

        if player == player[0]:

            buttons[row][column]['text'] = player

            if checkwinner == False:
                player = players[1]
                label.config(text = (players[1] +"'s Turn"))

            elif checkwinner == True:
                label.config(text = (players[0] + "Wins"))

            elif checkwinner == "Tie":   
                label.config(text = ("No one wins."))

        else:

            buttons[row][column]['text'] = player

            if checkwinner == False:
                player = players[0]
                label.config(text = (players[0] +"'s Turn"))

            elif checkwinner == True:
                label.config(text = (players[1] + "Wins"))

            elif checkwinner == "Tie":   
                label.config(text = ("No one wins."))


def checkwinner():
    pass

def emptyslots():
    pass

def newgame():
    pass

window = Tk()
window.title('Tic - Tac - Toe')

players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0], [0,0,0], [0,0,0]]

label = Label(text = player + " turn's ", font = ('comic sans', 40))
label.pack(side = "top")


reset_button = Button(text = "restart", font = ('consolas',20), command = newgame)
reset_button.pack(side = "bottom")

frame = Frame(window)
frame.pack()


for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = ('consolas',20), width = 5, height = 2,
                                command = lambda row = row, column = column: whoseturn(row,column))
        buttons[row][column].grid(row= row, column= column)

window.mainloop()