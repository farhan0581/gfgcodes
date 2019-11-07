class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, arr):
        profit = 0
        start = 0
        end = 0

        for i in xrange(len(arr)-1):
            if arr[i] > arr[i+1]:
                profit += arr[end] - arr[start]
                start = end = i+1
            else:
                end += 1
    
        if arr[end] > arr[start]:
            profit += arr[end] - arr[start]

        return profit

print(Solution().maxProfit([5,2,10]))