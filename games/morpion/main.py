from game import choosePosition, thereIsAWinner
from display import printGrid

def setGame():
    columns, lines = 3, 3
    grid = [[0 for _ in range(columns)] for _ in range(lines)]
    return [grid, columns, lines]

def letsPlay(data, token):
    x, y = choosePosition(data)
    data[0][y][x] = token

    if thereIsAWinner(data):
        return "finish"
    return -1 if token == 1 else 1

def main():
    data = setGame()
    printGrid(data)

    token = 1  # 1: O | -1: X

    while token != "finish":
        token = letsPlay(data, token)
        printGrid(data)

if __name__ == "__main__":
    main()
