
def solve(arr, i,j,k):
    if i == len(arr)-1:
        if j==k:
            return arr[i][j]
        else:
            return arr[i][j]+arr[i][k]

    

    if i+1 < len(arr):
        if j+1 < len(arr[0]):
            solve(arr, i+1, j+1, k)
        
        if j-1 >= 0:
            solve(arr, i+1, j-1, k)
        
        solve(arr, i+1, j, k)

        if k+1 < len(arr[0]):
            solve(arr, i+1, j, k)
        
        if j-1 >= 0:
            solve(arr, i+1, j-1, k)
        
        solve(arr, i+1, j, k)




    


def maximumChocolates(m,n,grid):
    # write your code here
    pass



l=[[2, 3, 1, 2],[3, 4, 2, 2],[5, 6, 3, 5]]
m=len(l)
n=len(l[0])
print(maximumChocolates(m,n,l))