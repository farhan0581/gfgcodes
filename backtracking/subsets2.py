class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def _solve(self, subset, arr, res, index, check):
        _i = '_'.join([str(e) for e in subset])
        try:
            check[_i]
        except:
            check[_i] = 1
            res.append(subset[:])
        for i in range(index, len(arr)):
            subset.append(arr[i])
            res = self._solve(subset, arr, res, i+1, check)
            subset.pop()
        
        return res
        

    def subsetsWithDup(self, arr):
        res = []
        arr = sorted(arr)
        check = {}

        return self._solve([], arr, res, 0, check)

print(Solution().subsetsWithDup([1,2,2]))