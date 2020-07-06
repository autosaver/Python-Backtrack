size=4
attack=[[0]*size]*size
maze=[[0]*size]*size
queen=0
def infect(x,y):
    attack[x]=1
    for i in range(size):
        attack[i][y]=1
    for i in range(size):
        for j in range(size):
            temp=(x-i)/(y-j)
            if abs(temp)==1:
                attack[i][j]=0

infect(0,0)

def backtrack(row,col):
    for i in range(size):
        maze[queen][i]=1
        infect(queen,i)
