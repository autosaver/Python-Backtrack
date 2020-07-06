w=[5,10,12,13,15,18]
n=len(w)
maxsum=30
arr=[0]*n
def backtrack(sums,k):
    for i in range(k,n):
        sums+=w[i]
        arr[i]=1
        if sums>maxsum:
            arr[i]=0
            sums-=w[i]
            break
        if sums==maxsum:
            print(arr)
            print("solved")
        backtrack(sums,i+1)
        arr[i]=0
        sums-=w[i]
backtrack(0,0)

