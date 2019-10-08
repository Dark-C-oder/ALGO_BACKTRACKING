n = int(input("enter size of maze = "))
maze = [list(map(int,input().split(" "))) for i in range(n)]

def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

def isSafe(maze,x,y):
    if x>=0 and y>=0 and x<n and y<n and maze[x][y]==1:
        return True
    return False

def solveMaze(maze,n):
    sol = [[0 for i in range(n)] for j in range(n)]
    if solveMazeUtil(maze,0,0,sol,n) == True:
        printSolution(sol)
        return True
    else:
        print("No sol available !!!!!")
        return False

def solveMazeUtil(maze,x,y,sol,n):
    if x==n-1 and y==n-1:
        sol[x][y]=1
        return True
    if isSafe(maze,x,y) == True:
        sol[x][y]=1

        if solveMazeUtil(maze,x+1,y,sol,n) == True:
            return True
        if solveMazeUtil(maze,x,y+1,sol,n) == True:
            return True

        sol[x][y]=0
        return False


solveMaze(maze,n)


