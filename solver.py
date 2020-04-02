import os

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
    for row in theGrid:
        nums = ""
        for col in row:
            nums += ' ' #Sapces make it cleaner to read.
            nums += str(col)
        print(nums)
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
    #floor division to maintain integer to use as a counter
    xSub = (x//3)*3
    ySub = (y//3)*3
    #Test the 3x3 that the tile belongs to.
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
    #return to mainMenu
    #nextSolutionIfAvailable
    #exit

def keyGrid() :
    print("Manual user input of grid.\nEnter row by row your puzzle, use 0 as blanks.")
    #todo: Ignore white space in lines, '1 2 3 4 5' AND '12345' should be equally valid input. Still print with the spaces though..
    newGrid = []

    i = 0
    for row in grid :
        line = input("")
        newRow = []
        for nums in line :
            newRow.append(int(nums))
        grid[i] = newRow
        i += 1

    #Grid is input, but prints, unsolvably (regurgitates input)


def mainMenu() :
    """
    userChoice = 420
    while (userChoice != 0):
        print("")
        print("1 -Show the Grid")    #Show Grid to be solved.
        print("2 -Enter a new Grid") #Manually Input Grid. Line By Line
        #print("3 -Import a grid from file.") #Import Grid from File & Export Solution(s) to a File
        print("4 -Solve the Puzzle") #Solve grid if one has been input.
        print("0 -Exit") #Exit menu loop.


        userChoice = input("")
    """
    #Revise the Loaded Grid (Allow user to fix errors.)
    keyGrid()
    solve(grid)


#####
mainMenu()
