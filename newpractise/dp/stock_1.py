'''
buy and sell only once
diff between max and local is the ans
'''
def maximumProfit(arr):
    # Write your code here
    min_so_far = arr[0]
    profit = 0

    for i in range(len(arr)):
        cur_profit = arr[i] - min_so_far
        profit = max(profit, cur_profit)
        min_so_far = min(min_so_far, arr[i])
    return profit


l = [ 2, 100, 150, 120]
print(maximumProfit(l))