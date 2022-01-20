# 0: null
# 1: white
# 2: black

#grid 8x8

grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

def selectCell(row,col,player):
    valicion = invalido(row,col)
    if(valicion == True):
        if ((player==1) and (grid[row][col]==0)):
            grid[row][col] = 1
            isValid(row, col,player)
            return "OK"
        elif((player==2) and (grid[row][col]==0)):
            grid[row][col] = 2
            isValid(row, col,player)
            return "OK"
    else:
        return "ok"

#redirecciona a los posibles movimientos
def isValid(row,col,player):
        horizontal(row,col,player)
        vertical(row, col, player)
        diagonal(row, col, player)

def horizontal(row,col,player):
        lenG = lenGrid()
        if(row<=lenG-1 and col<=lenG-1):
            if(player==1):
                if (col+1 <= lenG-1):
                    if(grid[row][col+1]==2):
                        grid[row][col+1] = 1
                        horizontal(row, col+1, player)
                else:
                    if (grid[row][col] == 2):
                        grid[row][col] = 1
                        horizontal(row, col, player)

            if (player == 2):
                if (col+1 <= lenG-1):
                    if (grid[row][col+1] == 1):
                        grid[row][col+1] = 2
                        horizontal(row, col+1, player)
                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 2
                        horizontal(row,col, player)

        if(row>=0 and col>=0):
            if(player==1):
                if (col-1 >= 0):
                    if(grid[row][col-1]==2):
                        grid[row][col-1] = 1
                        horizontal(row, col-1, player)
                else:
                    if (grid[row][col] == 2):
                        grid[row][col] = 1
                        horizontal(row, col, player)
            if (player == 2):
                if(col-1 >= 0):
                    if (grid[row][col-1] == 1):
                        grid[row][col-1] = 2
                        horizontal(row, col-1, player)
                else:
                    if (grid[row][col] == 1):
                        grid[row][col] = 2
                        horizontal(row,col, player)

def vertical(row,col,player):
    lenG=lenGrid()
    if(row>= 0 and col>=0 ):
        up=grid[row-1][col]
        if (player == 1):
            if (up == 2):
                grid[row-1][col] = 1
                vertical(row-1,col, player)
        if (player == 2):
            if (up == 1):
                grid[row-1][col] = 2
                vertical(row-1, col, player)
    if(row <= lenG-1 and col <= lenG-1):
        if(row+1 <= lenG-1):
            dow=grid[row+1][col]
            if (player == 1):
                if (dow == 2):
                    grid[row+1][col] = 1
                    vertical(row+1,col, player)
            if (player == 2):
                if (dow == 1):
                    grid[row+1][col] = 2
                    vertical(row+1,col, player)
        else:
            actual = grid[row][col]
            if (player == 1):
                    if (actual == 2):
                        grid[row][col] = 1
                        vertical(row, col, player)
            if (player == 2):
                if (actual == 1):
                    grid[row][col] = 2
                    vertical(row, col, player)

def diagonal(row,col,player):
    lenG = lenGrid()
    if (player == 1):
        if (row >= 0 and col >= 0):
            if(row-1 >= 0 and col+1 <= lenG-1):
                    upDer = grid[row - 1][col + 1]
                    if (upDer  == 2):
                        grid[row-1][col+1] = 1
                        diagonal(row-1,col+1,player)
        if (row >= 0 and col >= 0):
            if (row-1>= 0 and col-1>=0):
                upIzq = grid[row-1][col-1]
                if (upIzq == 2):
                    grid[row-1][col-1] = 1
                    diagonal(row-1,col-1,player)
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row+1<= lenG-1 and col+1 <= lenG-1):
                dowDer = grid[row+1][col+1]
                if (dowDer == 2):
                    grid[row+1][col+1] = 1
                    diagonal(row+1,col+1,player)
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row + 1 <= lenG-1 and col - 1 >= 0):
                dowIzq = grid[row + 1][col - 1]
                if (dowIzq == 2):
                    grid[row+1][col-1] = 1
                    diagonal(row+1,col-1,player)

    if (player == 2):
        if (row >= 0 and col >= 0):
            if(row-1 >= 0 and col+1 <= lenG-1):
                    upDer = grid[row - 1][col + 1]
                    if (upDer  == 1):
                        grid[row-1][col+1] = 2
                        diagonal(row-1,col+1,player)
        if (row >= 0 and col >= 0):
            if (row-1>= 0 and col-1>=0):
                upIzq = grid[row-1][col-1]
                if (upIzq == 1):
                    grid[row-1][col-1] = 2
                    diagonal(row-1,col-1,player)
        if (row <= lenG - 1 and col <= lenG - 1):
            if (row+1<= lenG-1 and col+1 <= lenG-1):
                dowDer = grid[row+1][col+1]
                if (dowDer == 1):
                    grid[row+1][col+1] = 2
                    diagonal(row+1,col+1,player)

        if (row <= lenG - 1 and col <= lenG - 1):
            if (row + 1 <= lenG-1 and col - 1 >= 0):
                dowIzq = grid[row + 1][col - 1]
                if (dowIzq == 1):
                    grid[row+1][col-1] = 2
                    diagonal(row+1,col-1,player)

def invalido(row,col):
    lenG=lenGrid()
    if (row >= 0):
        if(row-1 >= 0):
            if(grid[row-1][col]!=0 ):
                return True
    if(row <= lenG-1):
        if(row+1 <= lenG-1):
            if(grid[row+1][col]):
                return True
    if(col <= lenG-1):
        if(col+1 <= lenG-1):
            if(grid[row][col+1] != 0):
                return True
    if(col >= 0):
        if(col-1 >= 0):
            if(grid[row][col-1] != 0):
                return True
    if(row >= 0 and col >= 0):
        if(row-1 >= 0 and col-1 >= 0):
            if(grid[row-1][col-1] != 0):
                return True
    if (row <= lenG-1 and col  <= lenG-1):
        if (row + 1 <= lenG-1 and col + 1 <= lenG-1):
            if (grid[row + 1][col + 1] != 0):
                return True
    if (row >= 0 and col <= lenG - 1):
        if (row - 1 >=  0 and col + 1 <= lenG - 1):
            if (grid[row - 1][col + 1] != 0):
                return True

    if (row <= lenG-1 and col >= 0):
        if (row + 1 <= lenG-1 and col - 1 >= 0):
            if (grid[row + 1][col - 1] != 0):
                return True

def lenGrid():
    cont=0
    for x in grid:
        cont+=1
    return cont





