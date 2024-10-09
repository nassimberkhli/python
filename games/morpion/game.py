from display import printElement

def thereIsAnAlignement(points):
    return points == -3 or points == 3

def thereIsAWinner(data):
    for line in data[0]:
        result = sum(line)
        if thereIsAnAlignement(result):
            return True

    for column in range(3):
        result = sum(data[0][row][column] for row in range(3))
        if thereIsAnAlignement(result):
            return True

    diag1 = data[0][0][0] + data[0][1][1] + data[0][2][2]
    diag2 = data[0][0][2] + data[0][1][1] + data[0][2][0]
    
    return thereIsAnAlignement(diag1) or thereIsAnAlignement(diag2)

def incorrectPosition(data, x, y):
    if x < 0 or data[1] < x:
        print(f"x must be between 0 and {data[1]}")
    elif y < 0 or data[2] < y:
        print(f"y must be between 0 and {data[2]}")
    elif data[0][y][x] != 0:
        print("This position is occupied")
    else:
        return False
    print()
    return True

def choosePosition(data):
    x = int(input("Choose the x point: ")) - 1
    y = int(input("Choose the y point: ")) - 1
    y = (data[2] - 1) - y

    while incorrectPosition(data, x, y):
        x = int(input("Choose the x point: ")) - 1
        y = int(input("Choose the y point: ")) - 1
        y = (data[2] - 1) - y
    
    return x, y

