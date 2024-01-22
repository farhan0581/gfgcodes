class Solution(object):
    result = []
    def recur(self, arr, i, ):
        
    
    
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.result = []
        arr = [i for i in range(1, n+1)]
        nums = arr[:]
        self.recur(0, nums)
        return self.result
        

n = 3
k = 1

print(Solution().getPermutation(n,k))