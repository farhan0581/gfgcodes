
def uniquePaths(m, n):
    # Write your code here.
    dp = [[0 for i in range(n)] for i in range(m)]
    
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i-1 >= 0:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 0:
                dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]

def solve(m,n,i,j,dp):
    if i == m-1 and j == n-1:
        return 1
    
    w1 = w2 = 0
    if i+1 < m:
        w1 = solve(m,n,i+1,j,dp)
    if j+1 < n:
        w2 = solve(m,n,i,j+1,dp)

    return w1+w2
    

def _uniquePaths(m, n):
    return solve(m,n,0,0,[])




m = n = 1
print(uniquePaths(m,n))