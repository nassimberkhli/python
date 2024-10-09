from function import * 

game = True
firstPlayerTurn = True
columnNumber = 0
currentToken = " O "

print("\n\n\n******[ WELCOME IN POWER 4 ]******\n\n\n")

while game :

    print("")
    printGrid()
    print("")

    if firstPlayerTurn :
        print("First Player Turn\n")
    else :
        print("Second Player Turn\n")

    addToken(columnNumber, currentToken)

    if victory(currentToken) :

        print("")
        printGrid()
        print("")

        if firstPlayerTurn :
            print("First Player WIN !!!\n")
        else :
            print("Second Player WIN !!!\n")
        break

    firstPlayerTurn, currentToken = changeTurn(firstPlayerTurn)
    columnNumber = 0
