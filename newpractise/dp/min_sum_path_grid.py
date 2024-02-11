def solve(arr,i,j,dp):
    if i == 0 and j == 0:
        return arr[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]
    

    c1 = c2 = 99999999999

    if i-1 >= 0:
        c1 = arr[i][j] + solve(arr,i-1,j,dp)
    
    if j-1 >= 0:
        c2 = arr[i][j] + solve(arr,i,j-1,dp)
    
    dp[i][j] = min(c1,c2)
    return dp[i][j]


def minSumPath(grid):
    # Write your code here.
    m = len(grid)
    n = len(grid[0])
    dp = [[-1 for i in range(n)] for i in range(m)]
    return solve(grid, m-1, n-1, dp)

l = [[1, 2, 3],[4 ,5 ,4],[7, 5, 9]]

print(minSumPath(l))