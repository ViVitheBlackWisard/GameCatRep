from tkinter import *
from tkinter import ttk
from tkinter import messagebox


player = 1

def buttonPressed(buttonNumber):
    global player

    if buttonNumber == 1 and player == 1:
        buttonNW.config(text = "X")
        player = 2
    elif buttonNumber == 2 and player == 1:
        buttonN.config(text = "X")
        player = 2
    elif buttonNumber == 3 and player == 1:
        buttonNE.config(text = "X")
        player = 2
    elif buttonNumber == 4 and player == 1:
        buttonE.config(text = "X")
        player = 2
    elif buttonNumber == 5 and player == 1:
        buttonSE.config(text = "X")
        player = 2
    elif buttonNumber == 6 and player == 1:
        buttonS.config(text = "X")
        player = 2
    elif buttonNumber == 7 and player == 1:
        buttonSW.config(text = "X")
        player = 2
    elif buttonNumber == 8 and player == 1:
        buttonW.config(text = "X")
        player = 2
    elif buttonNumber == 9 and player == 1:
        buttonCentral.config(text = "X")
        player = 2
    elif buttonNumber == 1 and player == 2:
        buttonNW.config(text = "O")
        player = 1
    elif buttonNumber == 2 and player == 2:
        buttonN.config(text = "O")
        player = 1
    elif buttonNumber == 3 and player == 2:
        buttonNE.config(text = "O")
        player = 1
    elif buttonNumber == 4 and player == 2:
        buttonE.config(text = "O")
        player = 1
    elif buttonNumber == 5 and player == 2:
        buttonSE.config(text = "O")
        player = 1
    elif buttonNumber == 6 and player == 2:
        buttonS.config(text = "O")
        player = 1
    elif buttonNumber == 7 and player == 2:
        buttonSW.config(text = "O")
        player = 1
    elif buttonNumber == 8 and player == 2:
        buttonW.config(text = "O")
        player = 1
    elif buttonNumber == 9 and player == 2:
        buttonCentral.config(text = "O")
        player = 1
    wincondition()


def wincondition():
    if (buttonNW["text"] == "X" and buttonN["text"] == "X" and buttonNE["text"] == "X" or
       buttonW["text"] == "X" and buttonCentral["text"] == "X" and buttonE["text"] == "X" or
       buttonSW["text"] == "X" and buttonS["text"] == "X" and buttonSE["text"] == "X" or
       buttonNW["text"] == "X" and buttonW["text"] == "X" and buttonSW["text"] == "X" or
       buttonN["text"] == "X" and buttonCentral["text"] == "X" and buttonS["text"] == "X" or
       buttonNE["text"] == "X" and buttonE["text"] == "X" and buttonSE["text"] == "X" or
       buttonNW["text"] == "X" and buttonCentral["text"] == "X" and buttonSE["text"] == "X" or
       buttonNE["text"] == "X" and buttonCentral["text"] == "X" and buttonSW["text"] == "X"):
           messagebox._show("Winner of the game", "Player 1 - Winner!")
           buttonW.config(text=" ")
           buttonNW.config(text=" ")
           buttonN.config(text=" ")
           buttonNE.config(text=" ")
           buttonE.config(text=" ")
           buttonSE.config(text=" ")
           buttonS.config(text=" ")
           buttonSW.config(text=" ")
           buttonCentral.config(text=" ")

    elif (buttonNW["text"] == "O" and buttonN["text"] == "O" and buttonNE["text"] == "O" or
         buttonW["text"] == "O" and buttonCentral["text"] == "O" and buttonE["text"] == "O"or
         buttonSW["text"] == "O" and buttonS["text"] == "O" and buttonSE["text"] == "O" or
         buttonNW["text"] == "O" and buttonW["text"] == "O" and buttonSW["text"] == "O" or
         buttonN["text"] == "O" and buttonCentral["text"] == "O" and buttonS["text"] == "O" or
         buttonNE["text"] == "O" and buttonE["text"] == "O" and buttonSE["text"] == "O" or
         buttonNW["text"] == "O" and buttonCentral["text"] == "O" and buttonSE["text"] == "O" or
         buttonNE["text"] == "O" and buttonCentral["text"] == "O" and buttonSW["text"] == "O"):
            messagebox._show("Winner of the game", "Player 2 - Winner!")
            buttonW.config(text=" ")
            buttonNW.config(text=" ")
            buttonN.config(text=" ")
            buttonNE.config(text=" ")
            buttonE.config(text=" ")
            buttonSE.config(text=" ")
            buttonS.config(text=" ")
            buttonSW.config(text=" ")
            buttonCentral.config(text=" ")
    elif (buttonNW["text"] != " " and buttonN["text"] != " " and buttonNE["text"] != " " and
         buttonW["text"] != " " and buttonCentral["text"] != " " and buttonE["text"] != " " and
         buttonSW["text"] != " " and buttonS["text"] != " " and buttonSE["text"] != " "):
            messagebox._show("Winner of the game", "It'a Draw!")
            buttonW.config(text=" ")
            buttonNW.config(text=" ")
            buttonN.config(text=" ")
            buttonNE.config(text=" ")
            buttonE.config(text=" ")
            buttonSE.config(text=" ")
            buttonS.config(text=" ")
            buttonSW.config(text=" ")
            buttonCentral.config(text=" ")


root = Tk()
root.geometry("560x375")

buttonNW = ttk.Button(root, text = " ", command = lambda:buttonPressed(1))
buttonNW.grid(row = 0, column = 0, ipadx = 50, ipady = 50)

buttonN = ttk.Button(root, text = " ", command = lambda:buttonPressed(2))
buttonN.grid(row = 0, column = 1, ipadx = 50, ipady = 50)

buttonNE = ttk.Button(root, text = " ", command = lambda:buttonPressed(3))
buttonNE.grid(row = 0, column = 2, ipadx = 50, ipady = 50)

buttonE = ttk.Button(root, text = " ", command = lambda:buttonPressed(4))
buttonE.grid(row = 1, column = 2, ipadx = 50, ipady = 50)

buttonSE = ttk.Button(root, text = " ", command = lambda:buttonPressed(5))
buttonSE.grid(row = 2, column = 2, ipadx = 50, ipady = 50)

buttonS = ttk.Button(root, text = " ", command = lambda:buttonPressed(6))
buttonS.grid(row = 2, column = 1, ipadx = 50, ipady = 50)

buttonSW = ttk.Button(root, text = " ", command = lambda:buttonPressed(7))
buttonSW.grid(row = 2, column = 0, ipadx = 50, ipady = 50)

buttonW = ttk.Button(root, text = " ", command = lambda:buttonPressed(8))
buttonW.grid(row = 1, column = 0, ipadx = 50, ipady = 50)

buttonCentral = ttk.Button(root, text = " ", command = lambda:buttonPressed(9))
buttonCentral.grid(row = 1, column = 1, ipadx = 50, ipady = 50)


root.mainloop()
