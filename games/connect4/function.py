"""printGrid FUNCTION"""

grid = [
            ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["___", "___", "___", "___", "___", "___", "___"], 
            [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 "]]

def printGrid() :

    for row in grid :
        print("   |   |   |   |   |   |   |")
        for cell in row :
            print(cell, end="|")
        print("")


"""changeTurn FUNCTION"""

def changeTurn(firstPlayerTurn) :

    if firstPlayerTurn :
        return False, " X "
    else :
        return True, " O "


"""addToken FUNCTION"""

lastTokenIndexColumns = [5, 5, 5, 5, 5, 5]

def addToken(columnNumber, currentToken) :

    while columnNumber < 1 or 7 < columnNumber :
        columnNumber = int(input("Choose your column between 1 and 7 : "))
        if columnNumber < 1 or 7 < columnNumber :
            print("!! Must be between 1 and 7 !!\n")
        else :
            if lastTokenIndexColumns[columnNumber - 1] == -1 :
                print("!! The column", columnNumber, "is FULL !!\n")
                columnNumber = 0
            else :
                grid[lastTokenIndexColumns[columnNumber - 1]][columnNumber - 1] = currentToken
                lastTokenIndexColumns[columnNumber - 1] = lastTokenIndexColumns[columnNumber - 1] - 1


"""victory FUNCTION"""

def alignHorizontally(rowIndex, cellBegin, currentToken) :

    tokenAligned = 0

    for cellIndex in range(cellBegin, 7) :
        if grid[rowIndex][cellIndex] == currentToken :
            tokenAligned += 1
            if tokenAligned == 4 : 
                return True
        else :
            return False

def alignVertically(rowBegin, cellIndex, currentToken) :

    tokenAligned = 0

    for rowIndex in range(rowBegin, 6) :
        if grid[rowIndex][cellIndex] == currentToken :
            tokenAligned += 1
            if tokenAligned == 4 : 
                return True
        else :
            return False

def victory(currentToken) :

    for rowIndex in range(len(grid)) :
        for cellIndex in range(len(grid[rowIndex])) :

            if grid[rowIndex][cellIndex] == currentToken :

                if cellIndex <= 3 :
                    if alignHorizontally(rowIndex, cellIndex, currentToken) :
                        return True

                if rowIndex <= 2 :
                    if alignVertically(rowIndex, cellIndex, currentToken) :
                        return True

    return False
