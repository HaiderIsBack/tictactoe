from random import randint
from rich import print
import time, sys

board = [i for i in range(1,10)]

cpu = "X"
player = "O"

turn = player
#CPU first turn
board[4] = cpu

def printBoard(p):
    print("[red]\nComputer's Turn (X)\n[/red]") if p == cpu else print("[blue]\nPlayer's Turn (O)\n[/blue]")
    # top line
    for _ in range(17):
        print("-",end="")
    print()  
    for i in range(0, len(board)):
        if i % 3 == 0 and i != 0:
            print()
            for _ in range(17):
                print("-",end="")
            print()
        print("|",board[i],"|",end=" ")
    print()
    # Bottom line
    for _ in range(17):
        print("-",end="")
    print()

def getUserInput():
    while True:
        try:
            move = int(input("Enter a move: "))
            if type(board[move - 1]) == int:
                break
        except:
            print("[red]Invalid Input![/red]")
    return move - 1

def getCPUInput():
    while True:
        randomNum = randint(0,9)
        if type(board[randomNum - 1]) == int:
            print("[red]Thinking...[/red]")
            time.sleep(max(randomNum - 1, 0))
            break
    return randomNum - 1

def checkForWin(currPlayer):
    # check rows
    if board[0] == currPlayer and board[1] == currPlayer and board[2] == currPlayer:
        return True
    elif board[3] == currPlayer and board[4] == currPlayer and board[5] == currPlayer:
        return True
    elif board[6] == currPlayer and board[7] == currPlayer and board[8] == currPlayer:
        return True
    # check columns
    if board[0] == currPlayer and board[3] == currPlayer and board[6] == currPlayer:
        return True
    elif board[1] == currPlayer and board[4] == currPlayer and board[7] == currPlayer:
        return True
    elif board[2] == currPlayer and board[5] == currPlayer and board[8] == currPlayer:
        return True
    #check diagonal
    if board[0] == currPlayer and board[4] == currPlayer and board[8] == currPlayer:
        return True
    elif board[2] == currPlayer and board[4] == currPlayer and board[6] == currPlayer:
        return True
    
    return False

def isDraw():
    for i in board:
        if type(i) == int:
            return False
    return True

#Main Loop
while True:
    #Printing Board
    printBoard(turn)
    
    if turn == player:
        playMove = getUserInput()
    else:
        playMove = getCPUInput()
    board[playMove] = turn

    won = checkForWin(turn)
    if won:
        printBoard(turn)
        print("[red]\nComputer (X) won!!![/red]") if turn == cpu else print("[blue]\nPlayer (O) won!!![blue]")
        break

    if isDraw():
        printBoard(turn)
        print("[green]\nDraw nobody won![/green]")
        break

    turn = cpu if turn == player else player

sys.exit()