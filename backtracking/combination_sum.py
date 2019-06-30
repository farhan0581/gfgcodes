class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def _solve(self, arr, res, subset, n, index, tsum):
        s = sum(subset)
        # print(subset)
        if s == n:
            _i = '_'.join([str(e) for e in subset])
            try:
                self.check[_i]
            except:
                self.check[_i] = 1
                res.append(subset[:])
            # print(subset)
            # print('-----------')
            # print(res)
            # res.append(subset[:])
            # tsum = 0
            # print(res)
        

        for i in xrange(index, len(arr)):
            subset.append(arr[i])
            tsum += arr[i]
            if tsum >= n:
                res, tsum = self._solve(arr, res, subset, n, i+1, tsum)
            else:
                res, tsum = self._solve(arr, res, subset, n, i, tsum)
            subset.pop()
            tsum -= arr[i]
        
        return res, tsum
    
    def combinationSum(self, arr, n):
        arr = sorted(arr)
        res = []
        self.check = {}
        res, _ = self._solve(arr, res, [], n, 0, 0)
        return res

print(Solution().combinationSum([ 8, 10, 6, 11, 1, 16, 8 ], 28))
print(Solution().combinationSum([ 2,3,6,7 ], 7))

# [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ] 
# [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 ] 
# [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 8 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 10 ]
#  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 11 ] [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 6 ] 
#  [1 1 1 1 1 1 1 1 1 1 1 1 1 1 6 8 ] [1 1 1 1 1 1 1 1 1 1 1 1 6 10 ] [1 1 1 1 1 1 1 1 1 1 1 1 8 8 ] 
#  [1 1 1 1 1 1 1 1 1 1 1 1 16 ] [1 1 1 1 1 1 1 1 1 1 1 6 11 ] [1 1 1 1 1 1 1 1 1 1 6 6 6 ]
#   [1 1 1 1 1 1 1 1 1 1 8 10 ] [1 1 1 1 1 1 1 1 1 8 11 ] [1 1 1 1 1 1 1 1 6 6 8 ] 
#   [1 1 1 1 1 1 1 1 10 10 ] [1 1 1 1 1 1 1 10 11 ] [1 1 1 1 1 1 6 6 10 ] [1 1 1 1 1 1 6 8 8 ] 
#   [1 1 1 1 1 1 6 16 ] [1 1 1 1 1 1 11 11 ] [1 1 1 1 1 6 6 11 ] [1 1 1 1 6 6 6 6 ]
#    [1 1 1 1 6 8 10 ] [1 1 1 1 8 8 8 ] [1 1 1 1 8 16 ] [1 1 1 6 8 11 ] [1 1 6 6 6 8 ]
#     [1 1 6 10 10 ] [1 1 8 8 10 ] [1 1 10 16 ] [1 6 10 11 ] [1 8 8 11 ] [1 11 16 ] 
#     [6 6 6 10 ] [6 6 8 8 ] [6 6 16 ] [6 11 11 ] [8 10 10 ] 
