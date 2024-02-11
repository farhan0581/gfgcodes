'''
Problem statement
You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

Note:
You have an infinite number of elements of each type.
For example
If N=3 and X=7 and array elements are [1,2,3]. 
Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
Hence the output is 3.

The difference is only in the base case of tabulation
'''
INT_MAX=9999999999
def solve(arr, i, k, dp):
    if k == 0:
        return 0
    if i == 0:
        if arr[0] <= k:
            # print(k,k//arr[0])
            # return 1
            if k%arr[0] == 0:
                return k//arr[0]
            else:
                return INT_MAX
        else:
            return INT_MAX

    if dp[i][k] != -1:
        return dp[i][k]
    
    tk=nt=INT_MAX
    
    if k-arr[i] >= 0:
        #take
        tk = 1 + solve(arr, i, k-arr[i],dp)

    if i-1 >= 0:
        #notake
        nt = 0 + solve(arr, i-1, k,dp)
    
    dp[i][k] = min(tk, nt)
    return dp[i][k]



def _minimumElements(num, x):
    # Write your code here.
    dp = [[-1 for i in range(x+1)] for i in range(len(num))]
    ans = solve(num, len(num)-1, x,dp)
    if ans == INT_MAX:
        return -1
    return ans


def minimumElements(num, x):
    # Write your code here.
    n = len(num)
    dp = [[INT_MAX for i in range(x+1)] for i in range(n)]
    
    for i in range(n):
        dp[i][0] = 0
    

    for j in range(x+1):
        if j%num[0] == 0:
            dp[0][j] = j//num[0]
        else:
            dp[0][j] = INT_MAX

    # if x >= num[0]:
    #     dp[0][num[0]] = INT_MAX
    #     if x%num[0] == 0:
    #         dp[0][num[0]] = x//num[0]


    for i in range(1, n):
        for k in range(x+1):
            tk=INT_MAX
            if k-num[i] >= 0:
                #take
                tk = 1 + dp[i][k-num[i]]

            #notake
            nt = dp[i-1][k]
    
            dp[i][k] = min(tk, nt)

    ans=dp[n-1][x]
    print(dp)
    if ans == INT_MAX:
        return -1
    return ans


l = [12,1, 3]
n=4
print(minimumElements(l,n))