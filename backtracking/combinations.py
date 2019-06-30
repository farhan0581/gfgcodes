class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def _solve(self,res, arr, subset, k, index):
        if len(subset) == k:
            res.append(subset[:])

        for i in xrange(index, len(arr)):
            subset.append(arr[i])
            res = self._solve(res, arr, subset, k, i+1)
            subset.pop()
        return res
    
    def combine(self, n, k):
        arr = [i+1 for i in xrange(n)]

        res = []

        return self._solve(res, arr, [], k, 0)

print(Solution().combine(4,4))