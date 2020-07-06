maze=[[1,1,1,0,0],[0,0,1,1,0],[1,0,0,1,0],[0,1,0,1,1],[0,0,0,0,1]]
w=h=len(maze)
path=[[0]*w]*w
def backtrack(x,y):
    #left
    if x+1<w and maze[x+1][y]:
        x+=1
        path[x][y]=1
        backtrack(x,y)
        path[x][y]=0
        x-=1
    #down
    if y+1<h and maze[x][y+1]:
        y+=1
        path[x][y]=1
        backtrack(x,y)
        path[x][y]=0
        y-=1
    if x==w and y==h:
        print(path)
backtrack(0,0)
