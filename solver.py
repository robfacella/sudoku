
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
        if grid[x][i] == n :
            return False
    for i in range(0,9) :
        if grid[i][y] == n :
            return False
    #Test the 3x3 that the tile belongs to.
    xSub = (x//3)*3
    ySub = (y//3)*3
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[xSub+i][ySub+j] == n:
                return False
    #Otherwise the move is possible.
    return True
def solve(grid):
    #Solves Puzzle through all possible solutions
    for x in range(9) :
        for y in range(9) :
            #If this point on the board is blank.
            if grid[x][y] == 0 :
                #1 through 9
                for i in range(1, 10) :
                    if possibleMove(x,y,i) :
                        grid[x][y] = i
                        solve(grid)
                        grid[x][y] = 0
                return
    printGrid(grid)
    input("More?")

def keyGrid() :
    print("Manual user input of grid.\nEnter row by row your puzzle, use 0 as blanks.")
    
def mainMenu() :
    #Manually Input Grid. Line By Line
    #Revise the Loaded Grid (Allow user to fix errors.)
    ###show Grid to be solved.
    #Solve grid if one has been input.
    #Import Grid from File & Export Solution(s) to a File
    keyGrid()
    solve(grid)
#####
mainMenu()
