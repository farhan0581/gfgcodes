class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bsearch(self, arr, val):
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = (start+end)/2
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                end = mid-1
            else:
                start = mid+1
        return None

        
    def diffPossible(self, arr, k):

        for j in xrange(len(arr)):
            val = arr[j]+k
            x = self.bsearch(arr, val)
            if x and x != j:
                return 1
        return 0


print(Solution().diffPossible([1],1))