# https://takeuforward.org/data-structure/subset-sum-equal-to-target-dp-14/
'''
Problem statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.



Steps to convert Recursive Solution to Tabulation one.

To convert the memoization approach to a tabulation one, create a dp array with the same size as done in memoization. We can set its type as bool and initialize it as false.


First, we need to initialize the base conditions of the recursive solution.

If target == 0, ind can take any value from 0 to n-1, therefore we need to set the value of the first column as true.

The first row dp[0][] indicates that only the first element of the array is considered, therefore for the target value equal to arr[0], only cell with that target will be true, so explicitly set dp[0][arr[0]] =true, (dp[0][arr[0]] means that we are considering the first element of the array with the target equal to the first element itself). Please note that it can happen that arr[0]>target, so we first check it: if(arr[0]<=target) then set dp[0][arr[0]] = true.

After that , we will set our nested for loops to traverse the dp array and following the logic discussed in the recursive approach, we will set the value of each cell. Instead of recursive calls, we will use the dp array itself.
At last we will return dp[n-1][k] as our answer.

/Users/ba-00023252/Desktop/gfgcodes/data/rec-6.jpg
/Users/ba-00023252/Desktop/gfgcodes/data/rec-7.jpg
/Users/ba-00023252/Desktop/gfgcodes/data/rec-8.jpg



'''

def solve(arr, i, s, k,dp):
    if s == k:
        return True
    if s > k:
        return False
    if i > len(arr):
        return False
    
    if dp[s][i] != -1:
        return dp[s][i]
    
    c1 = c2 = False
    
    if i < len(arr):
        #take
        c1 = solve(arr, i+1, s+arr[i], k,dp)

            
        #nottake
        c2 =   solve(arr, i+1, s, k,dp)
    dp[s][i] = c1 or c2
    return c1 or c2


def _subsetSumToK(n, k, arr):
    s = sum(arr)
    dp = [[-1 for i in range(n+1)] for i in range(s+1)]
    # print(dp)
    # print(dp)
    return solve(arr, 0, 0, k,dp)


# tabulatiion
# number of loops=number of variables
def subsetSumToK(n, k, arr):
    # s = sum(arr)
    dp = [[False for i in range(n)] for i in range(k+1)]
    # print(dp)
    # print(dp)
    
    for i in range(n):
        dp[0][i] = True

    
    dp[arr[0]][0] = True
    

    for s in range(1,k+1):
        for i in range(1,n):
            
            if i-1>= 0:
                dp[s][i] = dp[s-arr[i]][i-1] or dp[s][i-1]
    
    print(dp)
    
    return dp[k][n-1]
        

    




k=5
l = [1, 7, 10,2]
# l = [2,5,6,7]
# l = [6,1,2,1]
l = [4,3,2,1]

print(subsetSumToK(len(l),k,l))