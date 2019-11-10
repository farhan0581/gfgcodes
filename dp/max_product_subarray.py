# https://www.geeksforgeeks.org/maximum-product-subarray-set-3/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, arr):
        if not len(arr):
            return 0
        
        maxval = arr[0]
        minval = arr[0]
        maxprod = arr[0]

        for i in xrange(1, len(arr)):
            if arr[i] < 0:
                maxval, minval = minval, maxval
            
            maxval = max(arr[i], maxval*arr[i])
            minval = min(arr[i], minval*arr[i])

            maxprod = max(maxprod, maxval)
        
        return maxprod


print(Solution().maxProduct([-2, -3, 0, -2, -40]))
