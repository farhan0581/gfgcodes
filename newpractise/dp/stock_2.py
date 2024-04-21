'''
can buy and sell multiple times
'''
def solve(arr, i, buy, dp):

    if i >= len(arr):
        return 0
        
    if dp[i][buy] != -1:
        return dp[i][buy]
    
    # we have bought, we can sell now
    if buy == 1:
        m1 = arr[i] + solve(arr, i+1, 0, dp) # sell
        m2 = 0 + solve(arr, i+1, 1, dp) # move
        dp[i][buy] = max(m1, m2)

    # we have to buy
    elif buy == 0:
        m3 = -arr[i] + solve(arr, i+1, 1, dp) # buy
        m4 = 0 + solve(arr, i+1, 0, dp) # move
        dp[i][buy] = max(m3, m4)
    
    return dp[i][buy]
    


# recur
def _getMaximumProfit(values, n) :
    #Your code goes here
    if n == 0:
        return 0
    dp = [[-1 for i in range(2)] for i in range(len(values))]
    return solve(values, 0, 0, dp)

# tabulation
def _getMaximumProfit(values, n) :
    #Your code goes here
    if n == 0:
        return 0
    dp = [[-1 for i in range(2)] for i in range(n+1)]
    dp[n][0] = dp[n][1] = 0
    i = n-1
    for i in range(n-1, -1, -1):
        for j in range(2):
            p = 0
            if j == 1:
                p = max(values[i] + dp[i+1][0], dp[i+1][1])

            # we have to buy
            elif j == 0:
                p = max(-values[i] + dp[i+1][1], dp[i+1][0])
            dp[i][j] = p
        # i -= 1
            
    # print(dp)
    return dp[0][0]


# space op
def getMaximumProfit(values, n) :
    #Your code goes here
    if n == 0:
        return 0
    # dp = [[-1 for i in range(2)] for i in range(n+1)]
    sp = [0 for i in range(2)]
    i = n-1
    ans = 0
    for i in range(n-1, -1, -1):
        for j in range(2):
            p = 0
            if j == 1:
                p = max(values[i] + sp[0], sp[1])

            # we have to buy
            elif j == 0:
                p = max(-values[i] + sp[1], sp[0])
            sp[j] = p

        # i -= 1
            
    # print(dp)
    return sp[0]

    

l = [1, 2, 3, 4, 5, 6, 7]
# l = l[::-1]

print(getMaximumProfit(l, len(l)))