class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, arr):
        res = 0
        for elem in arr:
            res = res^elem
        return res

Solution().singleNumber([2,2,1,16,1])
