def printElement(e):
    if e == 1:
        return 'O'
    elif e == -1:
        return 'X'
    return ' '

def printGrid(data):
    y = data[2]

    for line in data[0]:
        print(f"{y} | ", end="")
        for column in line:
            print(f"{printElement(column)} | ", end="")
        y -= 1
        print()

    print("  |", end="")
    for x in range(1, data[1] + 1):
        print(f" {x} |", end="")
    print()
