'''
Problem statement
You have been given an N*M matrix filled with integer numbers, find the maximum sum that can be obtained from a path starting from any cell in the first row to any cell in the last row.

From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right. So from a particular cell (row, col), we can move in three directions i.e.

Down: (row+1,col)
Down left diagonal: (row+1,col-1)
Down right diagonal: (row+1, col+1)
'''
def solve(arr, i, j, dp):
    if i == len(arr)-1:
        return arr[i][j]

    if dp[i][j] != -1:
        return dp[i][j]
    
    m1=m2=m3=-999999999

    if i+1 < len(arr):
        m1 = arr[i][j] + solve(arr,i+1,j,dp)

        if j+1 < len(arr[0]):
            m2 = arr[i][j] + solve(arr,i+1,j+1,dp)
        
        if j-1 >= 0:
            m3 = arr[i][j] + solve(arr,i+1,j-1,dp)
    

    dp[i][j] = max(m1,m2,m3)
    return dp[i][j]
    




def _getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[-1 for i in range(n)] for i in range(m)]

    m = -999999999
    for k in range(n):
        m = max(m, solve(matrix, 0,  k, dp))
    
    return m

# tabulation
def getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[-1 for i in range(n)] for i in range(m)]
    # dp[0] = matrix[0]

    # m = -999999999
    
    # print(m,n)
    for i in range(m):
        for j in range(n):
            m1=m2=m3=-999999999
            if i-1 >= 0:
                m1 = matrix[i][j] + dp[i-1][j]

                if j+1 < n:
                    m2 = matrix[i][j] + dp[i-1][j+1]
                
                if j-1 >= 0:
                    m3 = matrix[i][j] + dp[i-1][j-1]
                
                dp[i][j] = max(m1,m2,m3)    
            else:
                # print('df')
                dp[i][j] = matrix[i][j]
            
            
    return max(dp[m-1])






l = [[10, 2, 3],[3, 7, 2],[8, 1, 5]]

print(getMaxPathSum(l))