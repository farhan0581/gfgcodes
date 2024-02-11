mod = 1000000000 + 7
def _mazeObstacles(n, m, mat):
    dp = [[0 for i in range(m)] for i in range(n)]
    if mat[0][0] == -1:
        return 0
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == -1:
                continue
            if i-1 >= 0 and mat[i-1][j] != -1:
                dp[i][j] += dp[i-1][j]
            if j-1 >= 0 and mat[i][j-1] != -1:
                dp[i][j] += dp[i][j-1]
    return dp[n-1][m-1]

def solve(i,j, arr,dp):
    if arr[i][j] == -1:
        dp[i][j] = 0
        return 0
    if i==0 and j==0:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]
    
    w1=w2=0
    if i-1 >= 0:
        w1 = solve(i-1,j,arr,dp)
    if j-1 >= 0:
        w2 = solve(i,j-1,arr,dp)
    dp[i][j] = w1+w2
    return w1+w2

def mazeObstacles(n, m, mat):
    dp = [[-1 for i in range(m)] for i in range(n)]
    return solve(n-1,m-1,mat,dp)
    
    



l = [[0,0,-1],[0,0,0],[0,0,0]]
n = len(l)
m = len(l[0])
print(mod)
print(mazeObstacles(n,m,l))