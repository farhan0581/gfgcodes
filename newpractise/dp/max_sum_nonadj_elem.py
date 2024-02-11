
def solve(arr,i):
    
    if i == len(arr)-1:
        return arr[i]
    
    if i >= len(arr):
        return 0 
    
    # cost1 = cost2 = -999999
    
    # take
    # if i+2 < len(arr):
    cost1 = solve(arr, i+2) + arr[i]

    # not take
    # if i+1 < len(arr):
    cost2 = solve(arr, i+1)

    return max(cost1, cost2)
    
    
    
    


def maximumNonAdjacentSum(nums):    
    # Write your code here.
    l = [1, 2, 3, 5, 4]
    l=[1, 2, 3, 1, 3, 5, 8, 1, 9]

    
    return solve(l, 0)



print(maximumNonAdjacentSum([]))
