# TIC TAC TOE GAME DEVELOPED BY KHALIFA BL
# THIS IS A 1D PRESENTATION OF THE GAME TIC TAC TOE
from IPython.display import clear_output
# NameSPACE
player1 = ''
player2 = ''
starter = ''
counter = 0
mapTTT = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

# RULES AND WELCOMING FUNCTION


def start():
    print('Hello and Welcome to TIC TAC TOE!')
    print('Rules are Simple make 3 in a row of your symbol and BOOM you are a WINNER!')
    print("Player1 symbol is 'X' and Player2 symbol is 'O' \n\n")


def printBoard(mapTTT):
    print(f'{mapTTT["7"]} | {mapTTT["8"]} | {mapTTT["9"]}')
    print(f'{mapTTT["4"]} | {mapTTT["5"]} | {mapTTT["6"]}')
    print(f'{mapTTT["1"]} | {mapTTT["2"]} | {mapTTT["3"]}\n')


def getPlayerNames():
    print("So let's go ahead and start! ")
    player1 = input("Player 1 enter your name please: ")
    player2 = input("Player 2 your turn: ")
    starter = input("Who is going to start? 'Type 1 or 2' : ")
    return player1, player2, starter


def checkWinner():
    if(mapTTT['1'] == mapTTT['2'] == mapTTT['3']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['4'] == mapTTT['5'] == mapTTT['6']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['7'] == mapTTT['8'] == mapTTT['9']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['1'] == mapTTT['2'] == mapTTT['3']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['1'] == mapTTT['5'] == mapTTT['9']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['7'] == mapTTT['5'] == mapTTT['3']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['1'] == mapTTT['4'] == mapTTT['7']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['2'] == mapTTT['5'] == mapTTT['8']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2
    elif(mapTTT['3'] == mapTTT['4'] == mapTTT['9']):
        if(mapTTT['1'] == 'X'):
            return 1
        else:
            return 2

    else:
        return 0


def getInput(player1, player2, starter, mapTTT):
    nextTurn = 0
    turn = 1
    mapTTT = {
        "1": " ",
        "2": " ",
        "3": " ",
        "4": " ",
        "5": " ",
        "6": " ",
        "7": " ",
        "8": " ",
        "9": " ",
    }
    if starter == '1':
        choice = input(f'{player1}, Choose a number between 1 and 9: ')
        nextTurn = 2
        mapTTT[choice] = 'X'
        printBoard(mapTTT)
    else:
        choice = input(f'{player2}, Choose a number between 1 and 9: ')
        nextTurn = 1
        mapTTT[choice] = 'O'

        printBoard(mapTTT)

    for turn in range(8):
        if (checkWinner() == 0):
            turn += 1
            if(nextTurn == 1):
                choice = input(f'{player1}, Choose a number between 1 and 9: ')
                nextTurn = 2
                mapTTT[choice] = 'X'
                clear_output()
                printBoard(mapTTT)
            else:
                choice = input(f'{player2}, Choose a number between 1 and 9: ')
                nextTurn = 1
                mapTTT[choice] = 'O'
                clear_output()
                printBoard(mapTTT)

        elif (checkWinner() == 1):

            clear_output()
            print(f'Congrats {player1} you won!')
            printBoard(mapTTT)
            break
        elif(checkWinner() == 2):
            clear_output()
            print(f'Congrats {player2} you won!')
            printBoard(mapTTT)
            break


start()
printBoard(mapTTT)
player1, player2, starter = getPlayerNames()
getInput(player1, player2, starter, mapTTT)
