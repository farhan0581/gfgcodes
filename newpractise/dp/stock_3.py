from typing import List

def solve(arr, i, buy, k, dp):

    if i >= len(arr) or k <= 0:
        return 0
    if dp[i][k][buy] != -1:
        return dp[i][k][buy]
    
    if buy == 0:
        m1 = -arr[i] + solve(arr, i+1, 1,  k, dp)
        m2 = 0 + solve(arr, i+1, 0, k, dp)
        dp[i][k][buy] = max(m1,m2)
    elif buy == 1:
        m3 = arr[i] + solve(arr, i+1, 0, k-1, dp) # sell
        m4 = 0 + solve(arr, i+1, 1, k, dp)
        dp[i][k][buy] = max(m3,m4)
    
    return dp[i][k][buy]

# recursive
def _maxProfit(prices: List[int]) -> int:
    # Write your code here.
    k = 2
    dp = [[[-1 for i in range(2)] for i in range(k+1)] for i in range(len(prices))]
    return solve(prices, 0, 0, k, dp)


#tabulation
def maxProfit(prices: List[int]) -> int:
    # Write your code here.
    k = 2
    n = len(prices)
    dp = [[[-1 for i in range(2)] for i in range(k+1)] for i in range(n+1)]

    # if i >= len(arr) or k <= 0:
    #     return 0
    # when i == n, k or buy anything its 0
    # when k == 0, i and buy can be anything

    for i in range(n+1):
        for j in range(2):
            dp[i][0][j] = 0
    

    for i in range(k+1):
        for j in range(2):
            dp[n][i][j] = 0



    
    for i in range(n-1, -1, -1):
        for j in range(1,k+1): # leave k == 0, its base case
            for buy in range(2):
                if buy == 0:
                    dp[i][j][buy] = max(-prices[i] + dp[i+1][j][1], dp[i+1][j][0])
                elif buy == 1:
                    dp[i][j][buy] = max(prices[i] + dp[i+1][j-1][0], dp[i+1][j][1])
    
    # print(dp)
    return dp[0][2][0]

# space optimized
def maxProfit(prices: List[int]) -> int:
    # Write your code here.
    k = 2
    n = len(prices)
    # dp = [[-1 for i in range(2)] for i in range(k+1)]

    prev = [[0 for i in range(2)] for i in range(k+1)]
    cur = [[0 for i in range(2)] for i in range(k+1)]

    # if i >= len(arr) or k <= 0:
    #     return 0
    # when i == n, k or buy anything its 0
    # when k == 0, i and buy can be anything

    
    for i in range(n-1, -1, -1):
        for j in range(1,k+1): # leave k == 0, its base case
            for buy in range(2):
                if buy == 0:
                    cur[j][buy] = max(-prices[i] + prev[j][1], prev[j][0])
                elif buy == 1:
                    cur[j][buy] = max(prices[i] + prev[j-1][0], prev[j][1])
                
                prev = cur
    
    # print(cur[2])
    return cur[2][0]




l = [3, 3, 5, 0, 3, 1, 4]
l = [1, 3, 1, 2, 4, 8]
l = [5,4,3,2,1]
print(maxProfit(l))