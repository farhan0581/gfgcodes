def solve(arr, i, s, dp):
    if s == 0:
        return True
    if dp[i][s] != -1:
        return dp[i][s]
    
    
    c1=c2=False
    if i+1 < len(arr):
    #take
        c1=solve(arr, i+1, s-arr[i], dp)
        #not
        c2=solve(arr, i+1, s, dp)

    dp[i][s] = c1 or c2
    return c1 or c2



def canPartition(arr, n):
    # Write your code here.
    
    s = sum(arr)
    if s%2 == 0:
        hsum = s//2
        dp = [[-1 for i in range(hsum+1)] for i in range(n)]
        return solve(arr, 0, hsum, dp)
    else:
        return False


l = [3, 1, 1, 2, 2, 1]
l=[1, 5, 6, 98, 84]
n=len(l)
print(canPartition(l,n))