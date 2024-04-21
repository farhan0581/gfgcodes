from typing import List

def solve(arr, i, prev):
    if i > len(arr)-1:
        return 0
    
    if prev == -1 or arr[i] % arr[prev] == 0:
        return max(1 + solve(arr, i+1, i),solve(arr, i+1, prev))
    else:
        return solve(arr, i+1, prev)
    

def divisibleSet(arr: List[int]) -> List[int]:
    # write your code here
    arr = sorted(arr)
    n = len(arr)
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    res = {}
    for i in range(n-1, -1, -1):
        for prev in range(i-1, -2, -1):

            if prev == -1 or arr[i] % arr[prev] == 0:
                m1 = 1+dp[i+1][i]
                m2 = dp[i+1][prev+1]
                if m1 > m2:
                    res[i] = None
                dp[i][prev+1] = max(m1,m2)
            else:
                dp[i][prev+1] = dp[i+1][prev+1]
    
    print(dp, res)
    return dp[0][0]



    
    return solve(arr, 0, -1)


def divisibleSet(arr: List[int]) -> List[int]:
    n = len(arr)
    arr = sorted(arr)
    dp = [1 for i in range(n)]
    res = {0:0}
    maxi = 0
    maxind = 0
    for i in range(1,n):
        res[i] = i
        for prev in range(0, i):
            if arr[i] % arr[prev] == 0 and 1+dp[prev] > dp[i]:
                dp[i] =1+dp[prev]
                res[i] = prev
                if maxi < dp[i]:
                    maxi= dp[i]
                    maxind = i
                
    # print(dp)
    # print(res)
    # print(maxind)
    # print(temp)

    temp = [arr[maxind]]
    i = maxind
    # print(i)
    while True:
        if i == 0:
            break
        i = res[i]
        temp.append(arr[i])
        


    
    

    return temp[::-1]


l = [1, 16, 7, 8, 4, 2, 9, 13]
# l = [20, 19, 11, 25, 21]

print(divisibleSet(l))