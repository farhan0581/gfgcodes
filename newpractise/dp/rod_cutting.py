INT_MIN = -999999999
def solve(arr, i, k, dp):
    if k == 0:
        return 0
    
    if i == 0:
        if k >= 1:
            return k*arr[0]
        else:
            return INT_MIN

    if dp[i][k] != -1:
        return dp[i][k]

    
    tk = INT_MIN
    if k-(i+1) >= 0:
        #take
        tk = arr[i] + solve(arr, i, k-(i+1), dp)
    
    #nottake
    nt = 0 + solve(arr, i-1, k, dp)
    dp[i][k] = max(tk, nt)
    return  dp[i][k]

def _cutRod(price, n):
    dp = [[-1 for i in range(n+1)] for i in range(len(price))]
    # Write your code here.
    return solve(price, len(price)-1, n, dp)
    


def cutRod(price, n):
    dp = [[INT_MIN for i in range(n+1)] for i in range(len(price))]
    # Write your code here.

    for i in range(len(price)):
        dp[i][0] = 0

    
    for i in range(n+1):
        dp[0][i] = i*price[0]



    for i in range(len(price)):
        for k in range(n+1):
            tk=INT_MIN
            if k-(i+1) >= 0:
                tk = price[i] + dp[i][k-i-1]
            nt = 0 + dp[i-1][k]
            dp[i][k] = max(tk, nt)

    return dp[len(price)-1][n]



price = [2, 5, 7, 8, 10]
price = [3, 5, 8, 9, 10, 17, 17, 20]
n = 8

print(cutRod(price, n))