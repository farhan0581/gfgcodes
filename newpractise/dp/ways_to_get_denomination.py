def solve(arr, i, k, dp):
    if i == 0:
        if k == 0:
            return 1
        else:
            if arr[0] <= k and k%arr[0] == 0:
                return 1
            return 0
    
    if dp[i][k] != -1:
        return dp[i][k]

    
    tk = 0
    if k-arr[i] >= 0:
        tk = solve(arr, i, k-arr[i])
    
    nt = solve(arr, i-1, k)
    dp[i][k] = tk+nt
    return tk + nt
    


def countWaysToMakeChange(denominations, value) :
    dp = [[-1 for i in range(value+1)] for i in range(len(denominations))]
	# Your code goes here
    return solve(denominations, len(denominations)-1, value, dp)


l = [1,2,3]
n=4
print(countWaysToMakeChange(l,n))