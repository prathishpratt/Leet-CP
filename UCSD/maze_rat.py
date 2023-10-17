# Question 3: Write a function solveMaze that returns a solved maze.

# Every maze (NxN) starts at (0,0) and ends at (N-1,N-1), you can traverse in empty cells (" ") but cannot travel through cells that have X in them.
# You cannot move diagonally in the maze.
# Maze has only one path and no dead ends.
# If a maze can be solved, there will be only one possible path. You need to return a solved maze that highlights this path. The path in the solved MAZE should be returned as shown below. Cells that are a part of the path should have value "-"
# If a maze cannot be solved, return -1.
# Ex:
# [[" ","X","X"],
# [" "," "," "],
# ["X","X"," "]]

# Ans:
# [["-","X","X"],
# ["-","-","-"],
# ["X","X","-"]]

def solveMaze(maze):
    """
    input: 2D array
    output: solved 2D array
    """
    #maze and n will be inherited
    n = len(maze)
    def isright(x, y):
        #Check if the cell is correct or not
        return 0<=x<n and 0<=y<n and maze[x][y] == " "
    
    def solver(x, y):
        if x == n-1 and y == n-1:  #Check if its the end
            if maze[x][y] != "X":
                maze[x][y] = "-"
                return True
        if isright(x,y) == True:
            maze[x][y] = "-" #Add as the mark for path
            #Check if any left or right or up or down path exists
            if solver(x, y - 1) or solver(x, y + 1) or solver(x - 1, y) or solver(x + 1, y):
                return True
            maze[x][y] = " "
        return False
          
    #Start at (0,0) and traverse through recursion   
    if solver(0, 0):
        return maze
    else:
        return -1