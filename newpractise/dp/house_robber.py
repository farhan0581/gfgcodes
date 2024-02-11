'''
Problem statement
Mr. X is a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden.



All houses along this street are arranged in a circle. That means the first house is the neighbour of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses are broken into on the same night.



You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house. Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.



Note:
It is possible for Mr. X to rob the same amount of money by looting two different sets of houses. Just print the maximum possible robbed amount, irrespective of sets of houses robbed.


For example:
(i) Given the input array arr[] = {2, 3, 2} the output will be 3 because Mr X cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses. So, he’ll rob only house 2 (money = 3)

(ii) Given the input array arr[] = {1, 2, 3, 1} the output will be 4 because Mr X rob house 1 (money = 1) and then rob house 3 (money = 3).

(iii) Given the input array arr[] = {0} the output will be 0 because Mr. X has got nothing to rob.
'''

def _solve(arr,n,i,dp):
    # print(i,n)
    
    if i == n-1:
        return arr[i]
    if i >= n:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    

    # print("i=",i)

    s1 = arr[i] + solve(arr,n,i+2,dp) #take


    # not take
    s2 = 0 + solve(arr,n,i+1,dp)

    dp[i] = max(s1,s2)
    return dp[i]

# tabulation
# here we have to always consider negative index, dp[i+2] wont work
def solve(arr):
    dp = [-1 for i in range(len(arr))]
    dp[0] = arr[0]
    dp[1] = max(arr[0],arr[1])

    # m1 = m2 = -1
    # i = 2
    for i in range(1, len(arr)):
        
        #take
        if i-2 >= 0:
            m1 = arr[i] + dp[i-2]
        else:
            m1 = arr[i]
        

        #nottake
        if i-1 >= 0:
            m2 = 0 + dp[i-1]
        else:
            m2 = 0
        dp[i] = max(m1, m2)
        
    return dp[len(arr)-1]

# tabulation
def houseRobber(valueInHouse):
    # Write your function here.
    if len(valueInHouse) == 1:
        return valueInHouse[0]
    m1 = solve(valueInHouse[0:-1])
    m2 = solve(valueInHouse[1:])
    return max(m1,m2)

# recursion
def _houseRobber(valueInHouse):
    # Write your function here.
    dp = [-1 for i in range(5050)]
    dp2 = [-1 for i in range(5050)]
    if len(valueInHouse) == 1:
        return valueInHouse[0]
    m1 = solve(valueInHouse, len(valueInHouse)-1,0,dp)
    m2 = solve(valueInHouse, len(valueInHouse),1,dp2)
    return max(m1,m2)

l = [1, 5, 1, 2, 6]
l = [2, 3, 5]
l  = [100]
# l=[1, 7, 14, 21, 13]
# l=[6, 5, 4, 3, 2, 1, 7]
print(l[0:-1])
print(houseRobber(l))
# print(_solve(l))
    