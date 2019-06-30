class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def _solve(self, res, subset, index, arr):
        res.append(subset[:])
        
        for i in range(index, len(arr)):
            subset.append(arr[i])
            self._solve(res, subset, i+1, arr)
            subset.pop() # backtrack step
        
        return

    def subsets(self, arr):
        arr = sorted(arr)
        subset = []
        res = []
        self._solve(res, subset, 0 , arr)
        return res

print(Solution().subsets([1,2,3,4]))
