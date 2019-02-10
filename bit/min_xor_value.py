class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, lis):
        lis = sorted(lis)
        min_val = 99999
        i = 0
        arr_len = len(lis)

        while i < arr_len-1:
            val = lis[i]^lis[i+1]
            if min_val > val:
                min_val = val
            i += 1
            
        return min_val

            
x = Solution().findMinXor([0, 4, 7, 9 ])
print(x)

