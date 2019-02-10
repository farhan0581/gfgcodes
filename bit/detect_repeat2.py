class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, arr):
        INT_SIZE = 32
        result = 0
        for i in range(INT_SIZE):
            sum = 0
            for num in arr:
                if (num >> i) & 1:
                    sum += 1
            sum %= 3
            result = result | (sum << i)
        
        return result
                
print(Solution().singleNumber([3989,2,2,2,4,4,4]))