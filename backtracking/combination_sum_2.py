class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def _solve(self, arr, res, subset, index, n):
        s = sum(subset)
        if s == n:
            _i = '_'.join([str(e) for e in subset])

            try:
                self.check[_i]
            except:
                self.check[_i] = 1
                res.append(subset[:])
        
        for i in xrange(index, len(arr)):
            subset.append(arr[i])
            self._solve(arr, res, subset, i+1,n)
            subset.pop()
        
        return res

    
    def combinationSum(self, arr, n):
        arr = sorted(arr)
        res = []
        self.check = {}
        return self._solve(arr, res, [], 0, n)

print(Solution().combinationSum([10,1,2,7,6,1,5],8))
