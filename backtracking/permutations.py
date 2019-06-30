# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

class Solution:
    
    def _permute(self, arr, res, start, end):
        if start == end:
            _r = arr[:]
            res.append(_r)
        
        else:
            for i in xrange(start, end):
                arr[start], arr[i] = arr[i], arr[start] # swap
                res = self._permute(arr, res, start+1, end)
                arr[start], arr[i] = arr[i], arr[start] # backtrack
        return res

    def permute(self, arr):
        res = []
        res = self._permute(arr, res, 0, len(arr))
        return res

print(Solution().permute([1,2,3]))
