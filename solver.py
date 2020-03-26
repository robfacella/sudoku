
#vol266#page39#puzzle30
global grid
grid = [ [0,0,0,3,0,8,7,0,0],
         [1,0,0,5,0,0,0,3,2],
         [0,0,9,4,6,0,0,0,0],
         [5,4,2,0,0,0,0,8,0],
         [6,0,0,0,0,0,0,0,1],
         [0,8,0,0,0,0,2,4,7],
         [0,0,0,0,5,7,1,0,0],
         [8,9,0,0,0,6,0,0,3],
         [0,0,5,9,0,3,0,0,0]]

def printGrid(theGrid):
    for line in theGrid:
        print(line)

def possibleMove(x, y, n):
    #Tests if choice of <n> is valid at location x,y in the grid
    grid
    #Test Columns and rows
    for i in range(0,9) :
        if grid[y][i] == n :
            return False
    for i in range(0,9) :
        if grid[i][x] == n :
            return False
    #Test the 3x3 that the tile belongs to.
    xSub = (x//3)*3
    ySub = (y//3)*3
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[ySub+i][xSub+i] == n:
                return False
    #Otherwise the move is possible.
    return True

def solve(grid):
    print(possibleMove(2,1,1))
solve(grid)
