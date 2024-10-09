def thereIsAnAlignement(points) :
    
    if points == -3 or points == 3 :
            return True
    return False        
    
def thereIsAWinner(data) :
    
    result = 0
    
    for line in data[0] :
        result = 0
        
        for column in line :
            result += (column)
            
        if thereIsAnAlignement(result) :
            return True
            
    for column in range(3) :
        result = 0
        
        for row in range(3) :
            result += (data[0][row][column])
            
        if thereIsAnAlignement(result) :
            return True
            
    result = (data[0][0][0]) + (data[0][1][1]) + (data[0][2][2])
    if thereIsAnAlignement(result) :
            return True
            
    result = (data[0][0][2]) + (data[0][1][1]) + (data[0][2][0])
    if thereIsAnAlignement(result) :
            return True
    
    return False
    
def printElement(e) :
     
     if e == 1 :
         return 'O'
     elif e == -1 :
         return 'X'
     else :
         return ' '        
        
def printGrid(data) :
    
    y = data[2]
    
    for line in data[0] :
        print(y, end=" | ")
        
        for column in line :
            print(printElement(column), end=" | ")
            
        y -= 1
        print()
        
    for x in range(1, data[1] + 1) :
        if x == 1 :
            print("  |", x, end=" | ")
            
        else :    
            print(x, end=" | ")
            
    print()
    
def incorrectPosition(data, x, y) :
     
    if x < 0 or data[1] < x :
        print("x must be between 0 and", data[1])
         
    elif y < 0 or data[2] < y:
        print("y must be between 0 and", data[2])
         
    elif data[0][y][x] != 0 :
        print("this position is occupated")
         
    else :
        return False
         
    print()    
    return True    
         
def choosePosition(data) :
    
    x = int(input("choose the x point : ")) - 1
    y = int(input("choose the y point : ")) - 1
    
    y = (data[2] - 1) - y
    
    while incorrectPosition(data, x, y) :
        x = int(input("choose the x point : "))
        y = int(input("choose the y point : "))
    
    print()    
    return x, y    

def setGame() :
        
        columns = 3
        lines = 3
        """
        while columns < 3 :
            columns = int(input("insert the column number (minimum 3) >> "))
            
        while lines < 3 :    
            lines = int(input("insert the line number (minimum 3) >> "))
            
        print()""" 
        
        grid = [[0 for _ in range(columns)] for _ in range(lines)]
        
        return [grid, columns, lines]
        
    
def letsPlay(data, token) :
    
    x, y = choosePosition(data)
    data[0][y][x] = token
    
    if thereIsAWinner(data) :
        return "finish"
        
    # -1 : X | 0 : ' ' | 1 : O
        
    elif token == 1 :
        return -1
    else :
        return 1
        
def main() :
    
    data = setGame()
    printGrid(data)
    
    isNotFinish = True
    token = 1
    
    while token != "finish" :
        
        token = letsPlay(data, token)
        printGrid(data)
    
main()    