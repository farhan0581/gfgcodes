def solve(arr, i , k, dp):

    if i >= len(arr) or k <= 0:
        return 0
    
    if dp[i][k] != -1:
        return dp[i][k]
    
    if k % 2 == 0:
        m1 = -arr[i] + solve(arr, i+1, k-1, dp)
        m2 = 0 + solve(arr, i+1, k, dp)
        dp[i][k] = max(m1,m2)
    else:
        m3 = arr[i] + solve(arr, i+1, k-1, dp) # sell
        m4 = 0 + solve(arr, i+1, k, dp)
        dp[i][k] = max(m3,m4)
    
    return dp[i][k]

# recursive
def maximumProfit(prices,n,k):
    # Write your code here.
    # k = 2
    # lets use txn number hxere
    k = 2*k
    dp = [[-1 for i in range(k+1)] for i in range(n)]
    return solve(prices, 0, k, dp)


#tabulation
def maximumProfit(prices,n,k):
    # Write your code here.
    # k = 2
    # lets use txn number hxere
    k = 2*k
    dp = [[0 for i in range(k+1)] for i in range(n+1)]

    
    for i in range(n-1, -1, -1):
        for j in range(1, k+1):
            
            if j%2==0:
                dp[i][j] = max(-prices[i]+dp[i+1][j-1], dp[i+1][j])
            else:
                dp[i][j] = max(prices[i]+dp[i+1][j-1], dp[i+1][j])
    
    return dp[0][k]


#space opt
def maximumProfit(prices,n,k):
    # Write your code here.
    # k = 2
    # lets use txn number hxere
    k = 2*k
    prev = [0 for i in range(k+1)]
    cur = [0 for i in range(k+1)]

    
    for i in range(n-1, -1, -1):
        for j in range(1, k+1):
            
            if j%2==0:
                cur[j] = max(-prices[i]+prev[j-1], prev[j])
            else:
                cur[j] = max(prices[i]+prev[j-1], prev[j])
            
            prev = cur
    
    return cur[k]



l = [8, 5, 1, 3, 10]
k = 2

print(maximumProfit(l, len(l),k))