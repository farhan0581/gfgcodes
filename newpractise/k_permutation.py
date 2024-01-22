class Solution(object):
    def fact(self, n):
        if n == 1 or n == 0:
            return 1
        return n*self.fact(n-1)
    

    def recur(self, nums, k, res):
        if len(nums) == 1:
            res.append(str(nums[0]))
            return
        
        n = len(nums)
        f = self.fact(n-1)
        i = k//f

        res.append(str(nums[i]))
        del nums[i]
        k = k%f
        
        return self.recur(nums, k, res)


    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1,n+1)]
        res = []
        self.recur(nums, k-1, res)
        return ''.join(res)

'''
1. [1, 2, 3, 4]
2. [1, 2, 4, 3]
3. [1, 3, 2, 4]
4. [1, 3, 4, 2]
5. [1, 4, 2, 3]
6. [1, 4, 3, 2]
7. [2, 1, 3, 4]
8. [2, 1, 4, 3]
9. [2, 3, 1, 4]
10. [2, 3, 4, 1]
11. [2, 4, 1, 3]
12. [2, 4, 3, 1]
13. [3, 1, 2, 4]
14. [3, 1, 4, 2]
15. [3, 2, 1, 4]
16. [3, 2, 4, 1]
17. [3, 4, 1, 2]
18. [3, 4, 2, 1]
19. [4, 1, 2, 3]
20. [4, 1, 3, 2]
21. [4, 2, 1, 3]
22. [4, 2, 3, 1]
23. [4, 3, 1, 2]
24. [4, 3, 2, 1] 
'''


n = 4
k = 23
print(Solution().getPermutation(n,k))